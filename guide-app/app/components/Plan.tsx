import {EditButton, DeleteButton} from "./Button"
interface Prop {
    index: number;
    name: string;
};


export default function Plan({index, name} : Prop){

    return(
            <details className=" mt-2 collapse collapse-plus border-base-300 bg-base-200 border">
              <summary className="collapse-title text-xl font-medium items-center flex gap-5">
                <strong> Quick Bharatpur Visit</strong>
                <div className="rating">
                    <input disabled type="radio" name="rating-2" className="mask mask-star-2 bg-orange-400" />
                    <input disabled type="radio" name="rating-2" className="mask mask-star-2 bg-orange-400" defaultChecked />
                    <input disabled type="radio" name="rating-2" className="mask mask-star-2 bg-orange-400" />
                    <input disabled type="radio" name="rating-2" className="mask mask-star-2 bg-orange-400" />
                    <input disabled type="radio" name="rating-2" className="mask mask-star-2 bg-orange-400" />
                    </div>
                  </summary>
              <div className="collapse-content">
               <div className="absolute right-2 flex gap-2">
                <EditButton/>
                <DeleteButton/>
              </div>
                   <div className="avatar">
                    <div className="w-20 rounded-full">
                        <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
                    </div>
                  </div>
                  <br/>
                  <strong>{name}</strong>
                  <div className="border-black border-2 p-5 rounded">
                    <p className="absolute right-7 flex">Reviews: 100</p>
                    <p> Trip Discription </p>
                    <p>Trip Type: group | 3</p>
                    <p>Trip length: 2 days</p>
                    <p>Transportation: Public</p>
                    <button className="btn glass absolute right-7">
                     Rs: 500.00
                  </button>
                  <br/>
                  </div>
 
              </div>
            </details>
                   );
};
