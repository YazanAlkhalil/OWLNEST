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
        {
          resData?.quizzes.map((quizz)=>{
            return <QuizPassed  title={quizz.title} score={quizz.score} passed={quizz.passed} time={quizz.taken_at} />
          })
        }
      </div>
    </div>
  );
}
