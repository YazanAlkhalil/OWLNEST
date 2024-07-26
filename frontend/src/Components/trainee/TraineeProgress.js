import React, { useEffect } from "react";
import "react-circular-progressbar/dist/styles.css";
import CrcularProgressBar from "../CrcularProgressBar";
import QuizPassed from "../QuizPassed";
import useFetch from "../AuthComponents/UseFetch";
import { useParams } from "react-router-dom";

export default function TraineeProgress() {
  const { fetchData , resData } = useFetch();
  const { id } = useParams();

  useEffect(()=>{
    const getProgress = async () => {
      const res = await fetchData({url: 'http://127.0.0.1:8000/api/trainee/course/'+id+'/dashboard', method: 'get'}) 
      console.log(res);
    }
      getProgress();
  },[])

  return (
    <div>
      <div className="pt-6 flex justify-evenly text-center">
        <div>
          <h1 className="font-semibold text-xl mb-3">Completion</h1>
          <CrcularProgressBar value={resData?.completion} />
        </div>
        <div>
          <h1 className="font-semibold text-xl mb-3">XP</h1>
          <CrcularProgressBar value={resData?.xp_avg} />
        </div>
      </div>
      <div>
        <QuizPassed title={'Quiz 1'} score={'15/16'} type={'PASSED'} time={'12/2/2022'} />
        <QuizPassed title={'Quiz 1'} score={'15/16'} type={'FAILED'} time={'12/2/2022'} />
        <QuizPassed title={'Quiz 1'} score={'15/16'} type={'PASSED'} time={'12/2/2022'} />
        <QuizPassed title={'Quiz 1'} score={'15/16'} type={'FAILED'} time={'12/2/2022'} />
      </div>
    </div>
  );
}
