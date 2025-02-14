"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import axios from "axios";

// Use environment variable
const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function VerifyOTP() {
  const router = useRouter();
  const [otp, setOtp] = useState("");
  const [message, setMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [timeLeft, setTimeLeft] = useState(300); // 5 minutes

  const validateInput = () => {
    if (!otp || otp.length !== 6) {
      setMessage("Please enter a valid 6-digit OTP");
      return false;
    }
    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateInput()) return;
    
    setIsLoading(true);
    try {
      const response = await axios.post(`${API_URL}/verify-otp`, {
        otp: otp ? parseInt(otp) : ''
      });
      setMessage("Verification successful! Redirecting...");
      setTimeout(() => {
        router.push("/login/login_visitor");
      }, 2000);
    } catch (error) {
      if (error.response?.status === 400) {
        setMessage("Invalid OTP. Please try again.");
      } else {
        setMessage("An error occurred. Please try again later.");
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleResendOTP = async () => {
    setIsLoading(true);
    try {
      await axios.post(`${API_URL}/resend-otp`);
      setTimeLeft(300); // Reset timer
      setMessage("New OTP has been sent to your email");
    } catch (error) {
      setMessage("Failed to resend OTP. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  // Add OTP timer
  useEffect(() => {
    if (timeLeft > 0) {
      const timer = setInterval(() => {
        setTimeLeft(prev => prev - 1);
      }, 1000);
      return () => clearInterval(timer);
    }
  }, [timeLeft]);

  // Controlled input handler with type checking
  const handleOtpChange = (e) => {
    const value = e.target.value;
    // Only allow numbers and limit to 6 digits
    if ((value === '' || /^\d+$/.test(value)) && value.length <= 6) {
      setOtp(value);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50 px-4">
      <div className="p-8 bg-white rounded-lg shadow-md w-full max-w-md">
        <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">Verify OTP</h2>
        <p className="text-sm text-gray-600 text-center mb-6">
          Please enter the 6-digit code sent to your email
        </p>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <input
              type="text"
              inputMode="numeric"
              pattern="\d*"
              placeholder="Enter 6-digit OTP"
              value={otp || ''}
              onChange={handleOtpChange}
              className="w-full p-3 border text-black border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
              required
              maxLength={6}
            />
          </div>
          <button
            type="submit"
            disabled={isLoading}
            className="w-full bg-blue-500 text-white p-3 rounded-md hover:bg-blue-600 transition-colors font-medium disabled:bg-gray-400"
          >
            {isLoading ? "Verifying..." : "Verify"}
          </button>
          {timeLeft === 0 && (
            <button
              type="button"
              onClick={handleResendOTP}
              disabled={isLoading}
              className="w-full mt-2 text-blue-500 hover:text-blue-600"
            >
              Resend OTP
            </button>
          )}
          {timeLeft > 0 && (
            <p className="text-sm text-gray-500 text-center">
              Resend OTP in {Math.floor(timeLeft / 60)}:{(timeLeft % 60).toString().padStart(2, '0')}
            </p>
          )}
        </form>
        {message && <p className="mt-4 text-center text-sm text-red-500">{message}</p>}
      </div>
    </div>
  );
}
