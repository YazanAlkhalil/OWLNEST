import React from "react";
import Instructor from "../Instructor";

const trainers = [
  {
    id: 1,
    name: "John Doe",
  },
  {
    id: 2,
    name: "Jane Doeeee",
  },
  {
    id: 3,
    name: "sara king",
  },
];

export default function TraineeInfor() {
  return (
    <div>
      <div className="px-8 ">
        <h1 className="text-2xl font-black">Course Instructor</h1>
        {trainers.map((trai) => {
          return <Instructor key={trai.id} name={trai.name} />;
        })}
      </div>
      <div className="w-[200px] bg-slate-950 h-[3px] mx-auto my-8 "></div>
      <div className="px-8">
        <h1 className="text-2xl font-black my-8">Description</h1>
        <h1 className="text-xl font-bold w-[90%] mx-auto ">
          lorem lorem loremloremloremloremloremlorem
          loremloremloremloremloremloremlorem
          loremloremloremloremloremloremloremloremlorem
          loremloremloremloremloremloremloremloremlorem
          loremloremloremloremloremloremloremloremloremloremlorem
          loremloremloremloremloremloremloremloremloremloremloremlorem
          loremloremloremloremloremloremloremloremloremlorem
        </h1>
      </div>
      <div className="w-[200px] bg-slate-950 h-[3px] mx-auto my-10"></div>
      <div className="px-8">
        <h1 className="text-2xl font-black my-8">Additional Resources</h1>
        <h1 className="text-xl font-bold w-[90%] mx-auto ">https://sdgdgsdf</h1>
      </div>
    </div>
  );
}
