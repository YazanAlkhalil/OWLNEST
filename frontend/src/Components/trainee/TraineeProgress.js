import React from "react";
import "react-circular-progressbar/dist/styles.css";
import CrcularProgressBar from "../CrcularProgressBar";
import QuizPassed from "../QuizPassed";
export default function TraineeProgress() {
  const value = 60;
  const value2 = 80;
  return (
    <div>
      <div className="pt-6 flex justify-evenly text-center">
        <div>
          <h1 className="font-semibold text-xl mb-3">Completion</h1>
          <CrcularProgressBar value={value} />
        </div>
        <div>
          <h1 className="font-semibold text-xl mb-3">XP</h1>
          <CrcularProgressBar value={value2} />
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
