import React from "react";
import Card from "../Card";
import ChartExample from "../Chart";
import SimpleCard from "../SimpleCard";
import SkillesProgress from "../SkillesProgress";

const finshidCourse = {
    id: 1,
    title: "Finished Courses",
    value: "5",
}
const inProgressCourse = {
    id: 1,
    title: "In Progress Courses",
    value: "2",
}
const pendingCourse = {
    id: 1,
    title: "Pending Courses",
    value: "3",
}

export default function TranieeDashboard() {
  return (
    <>
      <div className="flex justify-evenly flex-wrap gap-7">
        <Card title={'XP'} value={'246'} />
        <Card title={'Training Time'} value={'1h 34m'} />
        <Card title={'Rank'} value={'#5'} />
      </div>
      <div className="mt-6">
        <ChartExample
          options={{
            height: 380,
            title: {
              text: "Daily XP Gains",
            },
            data: [
              { xp: "MON", Xp: 2000 },
              { xp: "TUE", Xp: 1500 },
              { xp: "WED", Xp: 1000 },
              { xp: "THU", Xp: 500 },
              { xp: "FRI", Xp: 600 },
              { xp: "sat", Xp: 700 },
              { xp: "sun", Xp: 800 },
            ],
            series: [
              {
                type: "area",
                xKey: "xp",
                yKey: "Xp",
                yName: "Xp",
              },
            ],
          }}
        />
      </div>
      <div className="flex mt-20 justify-evenly flex-wrap gap-7">
        <SimpleCard values={finshidCourse} />
        <SimpleCard values={inProgressCourse} />
        <SimpleCard values={pendingCourse} />
      </div>
      <div className="mt-20 p-10">
        <h1 className="text-3xl font-black">Skills :</h1>
        <SkillesProgress value={'50'} title={'HTML'}/>
        <SkillesProgress value={'40'} title={'CSS'}/>
        <SkillesProgress value={'80'} title={'TYPESCRIPT'}/>
        <SkillesProgress value={'20'} title={'JAVASCRIPT'}/>
        <SkillesProgress value={'66'} title={'ENGLISH'}/>
      </div>
    </>
  );
}
