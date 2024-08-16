import React, { useState, useEffect } from 'react';
import { useLocation, NavLink, useParams } from 'react-router-dom';
import useFetch from './AuthComponents/UseFetch';
import toast from 'react-hot-toast';

export default function TraineeQuiz() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const { state } = useLocation();
  const [LessonId,setLessonId] = useState(0);
  const [showScore, setShowScore] = useState(false);
  const [score,setScore] = useState(0)
  const [review,setReview] = useState([])
  const { fetchData } = useFetch();
  const [questions, setQuestions] = useState([]);
  const [userAnswers, setUserAnswers] = useState([]);
  const {id} = useParams()
  const [selectedAnswers, setSelectedAnswers] = useState([]);
  const [quizResults, setQuizResults] = useState(null);

  const handleAnswerToggle = (answerId) => {
    setSelectedAnswers(prev => {
      if (prev.includes(answerId)) {
        return prev.filter(id => id !== answerId);
      } else {
        return [...prev, answerId];
      }
    });
  };

  const handleNextQuestion = async () => {
    if (selectedAnswers.length > 0) {
      setUserAnswers(prevAnswers => [
        ...prevAnswers,
        {
          id: questions[currentQuestion].id,
          answers: selectedAnswers,
        },
      ]);

      setSelectedAnswers([]);
      
      const nextQuestion = currentQuestion + 1;
      if (nextQuestion < questions.length) {
        setCurrentQuestion(nextQuestion);
      } else {
        const finalAnswers = [
          ...userAnswers,
          {
            id: questions[currentQuestion].id,
            answers: selectedAnswers,
          }
        ];
        
        //here i get the response after answer submission
        const response = await fetchData({url:"/course/"+id+"/test/"+LessonId,method:"POST",data:{questions: finalAnswers}});
        setQuizResults(response);
        setShowScore(true);
      }
    } else {
      toast.error("Please select an answer");
    }
  };

  useEffect(() => {
    const getQuiz = async () => {
      const res = await fetchData({
        url: "http://127.0.0.1:8000/api/trainee/content/" + state,
        method: "get",
      });
      setLessonId(res.id)
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
    if(currentQuestion === questions.length)
      console.log(currentQuestion);

  }, [userAnswers]);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-xl p-8 bg-white rounded shadow-md">
        {showScore ? (
          <div className="text-center">
            <h2 className="text-2xl font-bold mb-4">Quiz Results</h2>
            <p className="text-xl mb-4">Your Score: {quizResults?.score.toFixed(2)}%</p>
            <div className="mb-6">
              {quizResults?.questions.map((q, index) => (
                <div key={q.id} className={`mb-4 p-4 rounded ${q.passed ? 'bg-green-100' : 'bg-red-100'}`}>
                  <p className="font-semibold">{index + 1}. {q.question}</p>
                  <p>Mark: {q.mark}</p>
                  {!q.passed && <p className="text-red-600">Feedback: {q.feedback}</p>}
                </div>
              ))}
            </div>
            <NavLink
              to={`/trainee/courses/${id}/content`}
              className="px-8 py-4 bg-primary dark:bg-DarkGray rounded dark:hover:bg-DarkSecondary text-xl font-semibold text-white hover:bg-secondary cursor-pointer">
              Back to Course
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
                      ? 'bg-secondary dark:bg-slate-800'
                      : 'bg-primary dark:bg-Gray hover:bg-secondary dark:hover:bg-slate-700'
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