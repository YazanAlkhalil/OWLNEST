import React, { useState } from 'react'
import { NavLink } from 'react-router-dom';

export default function TraineeQuiz() {
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [score, setScore] = useState(0);
    const [showScore, setShowScore] = useState(false);
  
    const questions = [
      {
        questionText: 'What is the capital of France?',
        answerOptions: [
          { answerText: 'Berlin', isCorrect: false },
          { answerText: 'Madrid', isCorrect: false },
          { answerText: 'Paris', isCorrect: true },
          { answerText: 'Lisbon', isCorrect: false },
        ],
      },
      {
        questionText: 'What is the capital of Germany?',
        answerOptions: [
          { answerText: 'Berlin', isCorrect: true },
          { answerText: 'Madrid', isCorrect: false },
          { answerText: 'Paris', isCorrect: false },
          { answerText: 'Lisbon', isCorrect: false },
        ],
      },
      {
        questionText: 'What is the capital of Span?',
        answerOptions: [
          { answerText: 'Berlin', isCorrect: false },
          { answerText: 'Madrid', isCorrect: true },
          { answerText: 'Paris', isCorrect: false },
          { answerText: 'Lisbon', isCorrect: false },
        ],
      },
      {
        questionText: 'What is the capital of Lisi?',
        answerOptions: [
          { answerText: 'Berlin', isCorrect: false },
          { answerText: 'Madrid', isCorrect: false },
          { answerText: 'Paris', isCorrect: false },
          { answerText: 'Lisbon', isCorrect: true },
        ],
      },
     
    ];
  
    const handleAnswerButtonClick = (isCorrect) => {
      if (isCorrect) {
        setScore(score + 1);
      }
  
      const nextQuestion = currentQuestion + 1;
      if (nextQuestion < questions.length) {
        setCurrentQuestion(nextQuestion);
      } else {
        setShowScore(true);
      }
    };
  
    return (
      <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
        <div className="w-full max-w-xl p-8 bg-white rounded shadow-md">
          {showScore ? (
            <div className="text-center h-[90px] ">
              <h2 className="text-2xl mb-5 font-semibold">You scored {score} out of {questions.length}</h2>
              <NavLink to={'/trainee/courses/:id/content'} className='px-8 py-4 bg-primary text-xl font-semibold text-white hover:bg-secondary cursor-pointer' >Go to next item</NavLink>
            </div>
          ) : (
            <>
              <div className="mb-4">
                <h2 className="text-xl font-semibold">
                  Question {currentQuestion + 1}/{questions.length}
                </h2>
                <div className="w-full bg-gray-200 rounded-full h-2.5 mb-4">
                  <div className="bg-primary h-2.5 rounded-full" style={{ width: `${((currentQuestion + 1) / questions.length) * 100}%` }}></div>
                </div>
                <p className="mt-2 text-gray-700">{questions[currentQuestion].questionText}</p>
              </div>
              <div className="flex flex-col space-y-3">
                {questions[currentQuestion].answerOptions.map((option, index) => (
                  <button
                    key={index}
                    onClick={() => handleAnswerButtonClick(option.isCorrect)}
                    className="px-4 py-2 text-white bg-primary rounded hover:bg-secondary"
                  >
                    {option.answerText}
                  </button>
                ))}
              </div>
            </>
          )}
        </div>
      </div>
    );
}
