import React, { useState } from 'react';
import { MdDelete } from "react-icons/md";

const Answer = ({ answerData, updateAnswer,deleteAnswer }) => {
  const updateText = (e) => {
    updateAnswer({...answerData, text: e.target.value });
  };
  const updateIsCorrect = (e) => {
    updateAnswer({ ...answerData, isCorrect:e.target.checked });
  };

  return (
    <div className='mb-4'>
      <div className='flex items-end justify-between gap-5'>
        <div className="flex w-min items-center border-b border-primary-500 py-2">
          <input placeholder="answer" value={answerData.text} onChange={updateText} className="text-xl appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" aria-label="lesson name" />
        </div>
        <div className="flex items-center ">
          <input onChange={updateIsCorrect} checked={answerData.isCorrect} id="default-checkbox" type="checkbox" value="" className="w-4 h-4 text-secondary bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-secondary dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
          <label htmlFor="default-checkbox" className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Correct</label>
        </div>
        <MdDelete onClick={deleteAnswer} className='hover:bg-slate-200 bg-slate-50 rounded-2xl p-2 box-content hover:cursor-pointer'/>
      </div>
    </div>
  );
};
export default Answer