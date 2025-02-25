"use client"
import { useParams} from "next/navigation";

export default function Edit(){
    const params = useParams();
    const id = params.id;
    return (
        <div>Editing the {id} plan</div>
    );
};
