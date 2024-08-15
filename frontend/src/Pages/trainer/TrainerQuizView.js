import React, { useEffect, useState } from 'react'
import { FaLightbulb } from "react-icons/fa";
import useFetch from '../../Components/AuthComponents/UseFetch';

function TrainerQuizView() {
    const {fetchData} = useFetch()
    const [quiz,setQuiz] = useState({title:"",questions:[]})
    const lessonId = localStorage.getItem('lessonId').slice(6)
    const getQuizData = async ()=>{
        const res = await fetchData({url:"/content/"+lessonId})
        console.log(res);
        setQuiz(res)
    }
    useEffect(()=>{
        getQuizData()
    },[])
    // const quiz = {
    //     name: "Sample Quiz",
    //     questions: [
    //       {
    //         name: "What is the capital of France?",
    //         grade: 10,
    //         feedback: "This question tests basic geography knowledge.",
    //         answers: [
    //           { text: "London", isCorrect: false },
    //           { text: "Paris", isCorrect: true },
    //           { text: "Berlin", isCorrect: false },
    //           { text: "Madrid", isCorrect: false }
    //         ]
    //       },
    //       // More questions...
    //     ]
    //   };



    return (
        <div className="max-w-3xl mx-auto shadow-lg rounded-lg">
            <h1 className="text-3xl font-bold mb-6 ">{quiz.title}</h1>

            {quiz.questions.map((question, index) => (
                <div key={index} className="mb-8 p-4 border border-gray-200 rounded-lg">
                    <h2 className="text-xl font-semibold mb-2">{question.question}</h2>
                    <p className="text-sm text-gray-600 mb-2">Grade: {question.mark}</p>
                    <div className='flex mt-5'>

                    <FaLightbulb/>
                    <p className="ml-2 text-sm italic mb-4">{question.feedback}</p>
                    </div>

                    <h3 className="font-medium mb-2">Answers:</h3>
                    <ul className="space-y-2">
                        {question.answers.map((answer, ansIndex) => (
                            <li
                                key={ansIndex}
                                className={`p-2 rounded ${answer.is_correct ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                                    }`}
                            >
                                {answer.answer}
                                {answer.is_correct && (
                                    <span className="ml-2 text-xs font-semibold">(Correct)</span>
                                )}
                            </li>
                        ))}
                    </ul>
                </div>
            ))}
        </div>
    );
}

export default TrainerQuizView
