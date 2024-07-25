import React, { useEffect } from "react";
import Card from "../Card";
import ChartExample from "../Chart";
import SimpleCard from "../SimpleCard";
import SkillesProgress from "../SkillesProgress";
import useFetch from "../AuthComponents/UseFetch";

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
  const { fetchData, resData } = useFetch();
  const companyId = localStorage.getItem('companyId');

  useEffect(()=>{
    async function getData() {
      const res = await fetchData({ url: 'http://127.0.0.1:8000/api/trainee/company/'+companyId+'/dashboard', method: 'get' });
      console.log(res);
    }
    getData();
    },[])

  return (
    <>
      <div className="flex justify-evenly flex-wrap gap-7">
        <Card title={'XP'} value={resData?.xp} />
        <Card title={'Training Time'} value={resData?.training_time} />
        <Card title={'Rank'} value={resData?.rank} />
      </div>
      <div className="mt-6">
        <ChartExample
          options={{
            height: 380,
            title: {
              text: "Daily XP Gains",
            },
            data: resData?.daily_xp.map((item)=>{
              return { xp: item.day, Xp: item.xp }

            }),
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
        <SimpleCard title={"finished courses"} value={resData?.finished_courses} />
        <SimpleCard title={"in progress courses"} value={resData?.in_progress_courses} />
        <SimpleCard title={"pending courses"} value={resData?.pending_courses} />
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
