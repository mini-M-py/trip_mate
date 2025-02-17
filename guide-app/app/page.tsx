import Link from "next/link";
import GuideCard from "./components/GuideCard"
interface User{
    id: number,
    name: string,
    username: string,
    email: string,
    address: {
      street: string,
      suite: number,
      city: string,
      zipcode: number,
      geo: {
        lat: string,
        lng:string 
      }
    }
};
 
export default async function Home() {
    const res = await fetch('https://jsonplaceholder.typicode.com/users', {cache : 'no-store'});
    let isLogedIn = 0;
    if(res.status === 200)
        isLogedIn = 1;
    const users: User [] = await res.json();
  return (
      <>
      {isLogedIn ? ( 
              <div className=" grid lg:grid-cols-5 
                md:grid-cols-4 
                sm:grid-cols-3
                gap-4">
               <div><GuideCard name="manish" id={200} place="Chitwan" rating={5}/></div>
               <div><GuideCard name="Hari" id={500} place="Butwal" rating={7}/></div>
               <div><GuideCard name="Suman" id={600} place="Kathmandu" rating={7}/></div>
               <div><GuideCard name="Anil" id={400} place="Butwal" rating={7}/></div>
               <div><GuideCard name="Anil" id={400} place="Butwal" rating={7}/></div>
            </div>          
           ):(
        <div className="flex items-center justify-center h-screen">
            <div className="w -1/2">
                <p className="text-center">
                    Join now to explore hidden gems or monetize your local
                    Knowledge! Signup Today and dive into authentic travel
                    experience.
                <br/>
                 </p>
                 <div className="items-center justify-center flex m-8">
                <button className="bg-sky-500 p-3 border-none rounded-xl m-4">
                     <Link href={'/login/login_visitor'}>Login</Link>
                </button>
                <button className="bg-sky-500 p-3 border-none rounded-xl m-4">
                    <Link href={'/signup/signup_visitor'}> Sign Up</Link>
                </button>
                 </div>

            </div>
            </div> 
        )}
      </>
  )
  
}
