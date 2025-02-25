"use client"
import { useRouter } from "next/navigation";
export function EditButton(){
    const router = useRouter();
    return(
        <>
            <button className="text-white px-3 py-1 rounded-full" 
                onClick={() => router.push(`/dashboard/edit?id=${2}`)}>
                  <svg xmlns="http://www.w3.org/2000/svg" 
                                fill="none" 
                                viewBox="0 0 24 24" 
                                strokeWidth={2} 
                                stroke="black" 
                                className="w-4 h-4">
                                <path strokeLinecap="round" 
                                strokeLinejoin="round" 
                                d="M16.862 3.487a2.25 2.25 0 113.182 3.182L7.011 19.703a4.5 4.5 0 01-2.04 1.14l-3.225.853a.375.375 0 01-.457-.457l.853-3.225a4.5 4.5 0 011.14-2.04L16.862 3.487z" />
                  </svg>
            </button>
        </>
    );
}

export function DeleteButton(){
   return(
       <>
        <button className="text-white px-3 py-1 rounded-full">
                            <svg xmlns="http://www.w3.org/2000/svg" 
                                fill="none" 
                                viewBox="0 0 24 24" 
                                strokeWidth={2} 
                                stroke="black" 
                                className="w-4 h-4">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
    </>
   ); 
}


