import React, { useState, useEffect } from 'react';
import { useLocation, NavLink } from 'react-router-dom';
import useFetch from './AuthComponents/UseFetch';

export default function TraineeQuiz() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const { state } = useLocation();
  const [showScore, setShowScore] = useState(false);
  const { fetchData } = useFetch();
  const [questions, setQuestions] = useState([]);
  const [userAnswers, setUserAnswers] = useState([]);
  const id = localStorage.getItem("courseID");
  const [selectedAnswers, setSelectedAnswers] = useState([]);

  const handleAnswerToggle = (answerId) => {
    setSelectedAnswers(prev => {
      if (prev.includes(answerId)) {
        return prev.filter(id => id !== answerId);
      } else {
        return [...prev, answerId];
      }
    });
  };

  const handleNextQuestion = () => {
    setUserAnswers(prevAnswers => [
      ...prevAnswers,
      {
        questionId: questions[currentQuestion].id,
        answerIds: selectedAnswers,
      },
    ]);

    setSelectedAnswers([]);

    const nextQuestion = currentQuestion + 1;
    if (nextQuestion < questions.length) {
      setCurrentQuestion(nextQuestion);
    } else {
      setShowScore(true);
    }
  };

  useEffect(() => {
    const getQuiz = async () => {
      const res = await fetchData({
        url: "http://127.0.0.1:8000/api/trainee/content/" + state,
        method: "get",
      });

      if (res && res.questions) {
        const parsedQuestions = res?.questions.map((q) => ({
          id: q.id,
          questionText: q.question,
          answerOptions: q.answers.map((answer) => ({
            answerText: answer.answer,
            id: answer.id,
          })),
        }));
        setQuestions(parsedQuestions);
      }
    };
    getQuiz();
  }, [state, fetchData]);

  useEffect(() => {
    console.log("Updated answers:", userAnswers);
  }, [userAnswers]);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-xl p-8 bg-white rounded shadow-md">
        {showScore ? (
          <div className="text-center flex align-center justify-center h-[70px]">
            <NavLink
              to={`/trainee/courses/${id}/content`}
              className="px-8 py-4 bg-primary dark:bg-DarkGray dark:hover:bg-DarkGrayHover text-xl font-semibold text-white hover:bg-secondary cursor-pointer">
              Submit Test
            </NavLink>
          </div>
        ) : (
          <div className='flex flex-col'>
            <div className="mb-4">
              <h2 className="text-xl font-semibold">
                Question {currentQuestion + 1}/{questions.length}
              </h2>
              <div className="w-full bg-gray-200 rounded-full h-2.5 mb-4">
                <div
                  className="dark:bg-DarkGray bg-primary h-2.5 rounded-full"
                  style={{
                    width: `${((currentQuestion + 1) / questions.length) * 100}%`,
                  }}></div>
              </div>
              <p className="mt-2 text-gray-700">
                {questions[currentQuestion]?.questionText}
              </p>
            </div>
            <div className="flex flex-col space-y-3">
              {questions[currentQuestion]?.answerOptions.map((option) => (
                <button
                  key={option.id}
                  onClick={() => handleAnswerToggle(option.id)}
                  className={`px-4 py-2 text-white rounded ${
                    selectedAnswers.includes(option.id)
                      ? 'bg-secondary dark:bg-DarkSecondary'
                      : 'bg-primary dark:bg-Gray hover:bg-secondary dark:hover:bg-DarkGrayHover'
                  }`}>
                  {option.answerText}
                </button>
              ))}
            </div>
            <button
              onClick={handleNextQuestion}
              className="mt-4 self-end px-4 py-2 bg-secondary text-white rounded hover:bg-hover">
              {currentQuestion === questions.length - 1 ? 'Finish' : 'Next Question'}
            </button>
          </div>
        )}
      </div>
    </div>
  );
}