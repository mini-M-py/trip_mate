


export default function Plan(){

    return(
            <div tabIndex={0} className="collapse collapse-plus border-base-300 bg-base-200 border">
              <div className="collapse-title text-xl font-medium items-center flex gap-5">
                <strong> Quick Bharatpur Visit</strong>
                <div className="rating">
                    <input disabled type="radio" name="rating-2" className="mask mask-star-2 bg-orange-400" />
                    <input disabled type="radio" name="rating-2" className="mask mask-star-2 bg-orange-400" defaultChecked />
                    <input disabled type="radio" name="rating-2" className="mask mask-star-2 bg-orange-400" />
                    <input disabled type="radio" name="rating-2" className="mask mask-star-2 bg-orange-400" />
                    <input disabled type="radio" name="rating-2" className="mask mask-star-2 bg-orange-400" />
                    </div>
                  </div>
              <div className="collapse-content">
               <div className="absolute right-2 flex gap-2">
                        <button className="text-white px-3 py-1 rounded-full">
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
                    </div>
                   <div className="avatar">
                    <div className="w-24 rounded-full">
                        <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                    </div>
                  </div>
                  <br/>
                  <strong>Name</strong>
                  <div className="border-black border-2 p-5 rounded">
                  <p className="absolute right-7 flex">Reviews: 100</p>
                  <p>Short discription about trip</p>
                  <p>Trip Type: </p>
                  <p>Trip length: </p>
                  <button className="btn glass absolute top-60 right-7">
                  Rs: 500.00
                  </button>
                  </div>
 
              </div>
            </div>
                   );
};
