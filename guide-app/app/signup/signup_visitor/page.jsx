"use client";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import axios from "axios";

export default function Signup() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    gender: "",
    country: "",
    phone: "",
    password: "",
    confirm_password: "",
    otp: "",
    profile_pic: null,
  });
  const [previewUrl, setPreviewUrl] = useState(null);
    const [step, setStep] = useState(0)

  const countries = [
    "United States", "United Kingdom", "Canada", "Australia", "India", 
    "Germany", "France", "Japan", "China", "Brazil", "Mexico", 
    "South Africa", "Spain", "Italy", "Russia","Nepal","other"
  ].sort();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setFormData({ ...formData, profile_pic: file });
    
    // Create preview URL for the selected image
    if (file) {
      const url = URL.createObjectURL(file);
      setPreviewUrl(url);
    }
  };

  // Add cleanup for preview URL
  useEffect(() => {
    return () => {
      if (previewUrl) {
        URL.revokeObjectURL(previewUrl);
      }
    };
  }, [previewUrl]);
    
   const sendOtp = async () => {
       if(formData.email != ""){
           const data = new FormData();
           data.append('email', formData.email)
           const res = await fetch('http://localhost:8000/users/verify',{
               method: 'POST',
               body: data
           }); 
           console.log(res.status);
           if(res.status === 422){
               alert('Invalid email');
           }else if(res.status === 202){
               setStep(1);
               alert('check email for OTP');
           }else{
              alert("something went woron cannot send OTP");
           }
       }
   }; 
     
  const handleSubmit = async (e) => {
      console.log(formData)
        e.preventDefault();
        const data = new FormData();
        Object.keys(formData).forEach((key) => {
        data.append(key, formData[key]);
    });

    try {
      const response = await axios.post("http://localhost:8000/users/visitor", data);
      router.push("/verify_otp");
    } catch (error) {
      alert('An error occurred during signup');
    }

 }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50 px-4 py-8">
      <div className="p-8 bg-white rounded-lg shadow-md w-full max-w-md">
        <h2 className="text-2xl font-bold mb-6 text-center text-black">Create Account</h2>
        <form className="space-y-4">
      {!step ? (<>
          <input
            type="text"
            name="name"
            placeholder="Full Name"
            autoComplete="off"
            onChange={handleChange}
            className="w-full p-3 border text-black border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            autoComplete="off"
            onChange={handleChange}
            className="w-full p-3 border text-black border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
            required
          />
          <select
            name="gender"
            onChange={handleChange}
            className="w-full p-3 border text-black border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all bg-white"
            required
          >
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>
          <select
            name="country"
            onChange={handleChange}
            className="w-full p-3 border text-black border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all bg-white"
            required
          >
            <option value="">Select Country</option>
            {countries.map((country) => (
              <option key={country} value={country}>
                {country}
              </option>
            ))}
          </select>
          <input
            type="tel"
            name="phone"
            placeholder="Phone"
            minLength={10}
            maxLength={10}
            autoComplete="off"
            onChange={handleChange}
            className="w-full p-3 border text-black border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            minLength={4}
            autoComplete="off"
            onChange={handleChange}
            className=" w-full p-3 border text-black border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
            required
          />
          <input
            type="password"
            name="confirm_password"
            placeholder="Repeat Password"
            minLength={4}
            autoComplete="off"
            onChange={handleChange}
            className="w-full p-3 border text-black  border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
            required
          />

           <div className="w-full">
            <label className="block text-sm font-medium text-gray-700 mb-2">Profile Picture</label>
            <div className="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-lg hover:border-blue-500 transition-colors">
              <div className="space-y-2 text-center">
                {previewUrl ? (
                  <div className="mx-auto w-24 h-24 mb-4">
                    <img
                      src={previewUrl}
                      alt="Profile preview"
                      className="w-full h-full rounded-full object-cover"
                    />
                  </div>
                ) : (
                  <svg
                    className="mx-auto h-12 w-12 text-gray-400"
                    stroke="currentColor"
                    fill="none"
                    viewBox="0 0 48 48"
                    aria-hidden="true"
                  >
                    <path
                      d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
                      strokeWidth={2}
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    />
                  </svg>
                )}
                <div className="flex text-sm text-gray-600">
                  <label
                    htmlFor="profile-upload"
                    className="relative cursor-pointer bg-white rounded-md font-medium text-blue-600 hover:text-blue-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-blue-500"
                  >
                    <span>Upload a photo</span>
                    <input
                      id="profile-upload"
                      name="profile_pic"
                      type="file"
                      accept="image/*"
                      className="sr-only"
                      onChange={handleFileChange}
                      required
                    />
                  </label>
                  <p className="pl-1">or drag and drop</p>
                </div>
                <p className="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
              </div>
            </div>
          </div>
              </>
      ):(<>
          <input
            type="text"
            name="otp"
            value=""
            placeholder="OTP"
            minLength={4}
            autoComplete="off"
            onChange={handleChange}
            className=" w-full p-3 border text-black  border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
            required
          />
              </>)}

      </form>
        <button
            onClick={!step ? sendOtp : handleSubmit}
            className="mt-4 :w
            w-full bg-blue-500 text-white p-3 rounded-md hover:bg-blue-600 transition-colors font-medium"
        >
            Sign Up
          </button>
      </div>
    </div>
  );
}
