import React, { useEffect, useState } from 'react';
import { MdDelete } from "react-icons/md";
import FormDialog from './EditQuestionDialog';


const Question = ({ questionData, updateQuestionData, deleteQuestion }) => {

  
  const handleAnswerTextChange = (e) => {
    updateQuestionData({
      ...questionData,
      text:e.target.value
    })
  };
  const handleGradeChange = (e) => {
    updateQuestionData({
      ...questionData,
      grade:e.target.value
    })
  };

  
  return (
    <div className='flex items-center mb-2'>
      <div className="flex flex-grow w-min items-center border-b border-primary-500 py-2">
        <label className='mr-2' htmlFor='question'>Question</label>
        <input id='question' placeholder="Question.." value={questionData.text} onChange={handleAnswerTextChange} className="text-xl appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" aria-label="Question" />
      </div>
      <div className="flex w-min items-center border-b border-primary-500 py-2">
        <label className='mr-2' htmlFor='grade'>Grade</label>
        <input id='grade' placeholder="grade" value={questionData.grade} onChange={handleGradeChange} className="text-xl appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="number" aria-label="Question" />
      </div>
      <FormDialog question={questionData} updateQuestionData={(updatedQuestionData) => {
        updateQuestionData(updatedQuestionData)}}/>
      <MdDelete onClick={deleteQuestion} className='ml-2 box-content p-2 mt-4 size-6 text-white rounded-full bg-red-300 hover:bg-red-500' />
    </div>
  );
};
export default Question