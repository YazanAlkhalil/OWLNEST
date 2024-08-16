import React, { useEffect, useState } from 'react';
import { MdDelete } from "react-icons/md";
import FormDialog from './EditQuestionDialog';


const Question = ({ questionData, updateQuestionData, deleteQuestion }) => {

  
  const handleAnswerTextChange = (e) => {
    updateQuestionData({
      ...questionData,
      question:e.target.value
    })
  };
  const handleGradeChange = (e) => {
    updateQuestionData({
      ...questionData,
      mark:e.target.value
    })
  };

    console.log(questionData);
  return (
    <div className='flex items-center mb-2'>
      <div className="flex flex-grow items-center border-b border-primary-500 dark:border-DarkGray py-2">
        <label className='mr-2' htmlFor='question'>Question</label>
        <input id='question' placeholder="Question.." value={questionData.question} onChange={handleAnswerTextChange} className="text-xl appearance-none bg-transparent border-non mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" aria-label="Question" />
      </div>
      <div className="flex items-center border-b border-primary-500 dark:border-DarkGray py-2">
        <label className='mr-2' htmlFor='grade'>Mark</label>
        <input id='grade' placeholder="grade" value={questionData.mark} onChange={handleGradeChange} className="text-xl appearance-none bg-transparent border-non mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" aria-label="Question" />
      </div>
      <FormDialog question={questionData} updateQuestionData={(updatedQuestionData) => {
        updateQuestionData(updatedQuestionData)}}/>
      <MdDelete onClick={deleteQuestion} className='ml-2 box-content p-2 mt-4 size-6 text-white rounded-full bg-red-300 hover:bg-red-500' />
    </div>
  );
};
export default Question