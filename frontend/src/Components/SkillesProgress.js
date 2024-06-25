import React from "react";
import ProgressBar from "@ramonak/react-progress-bar";

export default function SkillesProgress({value , title}) {
  return (
    <div className="flex flex-wrap justify-between p-5">
      <h1 className="text-2xl w-1/2 font-semibold">{title} :</h1>
      <div className="flex w-1/2">
      <ProgressBar
        completed={value}
        labelColor="#FFFFFF"
        bgColor="#001f34"
        transitionDuration="2s"
        transitionTimingFunction="linear"
        animateOnRender
        className="w-[85%] mt-1"
      />
      <h1 className="text-xl font-semibold ml-2">{value}%</h1>
      </div>
    </div>
  );
}
