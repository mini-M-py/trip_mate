import styles from './GuideCard.module.css';

interface Guide{
    id:number;
    name: string;
    place: string;
    rating: number;
}

export default function GuideCard({id, name, place, rating}: Guide){
    return(
      <div className="border-4 border-red-300 sm:max-w-xs bg-white rounded-2xl shadow-lg overflow-hidden text-center ">
      <img
        className="w-24 h-24 mx-auto rounded-full border-4 border-gray-300"
        src="https://shorturl.at/7DULv"
        alt="Profile"
      />
      <h2 className=" text-black text-xl font-semibold mt-4">{name}</h2>
      <p className="text-black text-sm">{place}</p>
      <button className="mt-4 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition">
        Follow
      </button>
    </div>
    )
}
