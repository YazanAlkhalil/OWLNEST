import React from 'react';
import Answer from './Answer';
import { v4 as uuidv4 } from 'uuid';
import toast from 'react-hot-toast';

const AnswerList = ({ answers, updateAnswers }) => {
  const addAnswer = () => {
    if (answers.length < 4) {
      updateAnswers([...answers, {id:uuidv4(), text: '', isCorrect: false, feedback: '' }]);
    }
  };
  const updateAnswer = (index, updatedAnswer) => {
    const updatedAnswers = [...answers];
    updatedAnswers[index] = updatedAnswer;
    updateAnswers(updatedAnswers);
  };
  const deleteAnswer = (id)=>{
    if(answers.length > 2){
      const updatedAnswers = [...answers];
      const index = updatedAnswers.findIndex((a) => a.id === id);
      updatedAnswers.splice(index, 1);
      updateAnswers(updatedAnswers);
    }
    else{
      toast.error('Answers should at least be 2')
    }
  }
  return (
    <div className='mt-10'>
      {answers.map((answer, index) => (
        <Answer
          key={answer.id}
          answerData={answer}
          updateAnswer={(updatedAnswer) => updateAnswer(index, updatedAnswer)}
          deleteAnswer={()=>deleteAnswer(answer.id)}
        />
      ))}
      {answers.length < 4 && <button className='border p-2 hover:bg-slate-50' onClick={addAnswer}>Add Answer</button>}
    </div>
  );
};

export default AnswerList;