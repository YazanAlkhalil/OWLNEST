import React, { useState } from 'react'
import Question from './Question';
import { v4 as uuidv4 } from 'uuid';
import toast from 'react-hot-toast';
import FormDialog from './AddAnswersDialog';
import useFetch from './AuthComponents/UseFetch';
import { useParams } from 'react-router-dom';


function CreateQuiz({ backendContent }) {
    const { fetchData } = useFetch()
    const { id } = useParams()
    const companyId = localStorage.getItem('companyId')
    const unitId = localStorage.getItem('unitId').slice(4)
    const [quizName, setQuizName] = useState('')
    const [questions, setQuestions] = useState([])

    const addQuestion = (question) => {
        setQuestions([...questions, question]);
    };
    function updateQuestionData(index, updatedQuestionData) {
        const tempQuestionData = [...questions];
        tempQuestionData[index] = updatedQuestionData;
        setQuestions(tempQuestionData);
    }
    function deleteQuestion(id) {
        if (questions.length > 1) {
            const tempQuestionData = [...questions];
            const index = tempQuestionData.findIndex((q) => q.id === id);
            tempQuestionData.splice(index, 1);
            setQuestions(tempQuestionData);
        }
        else {
            toast.error('There should be at least one question')
        }
    }
    async function submit() {
        let order = backendContent.find(unit => unit.id.toString() == unitId)?.contents.length
        const res = await fetchData({
            url: "/trainer/company/" + companyId + "/courses/" + id + "/unit/" + unitId + "/content/create", method: "POST", data: {
                title: quizName,
                order,
                questions,
                type:"quizz"
            }
        })
    }
    return (
        <div className='flex flex-col'>
            <div className='flex'>
                <div className="flex items-center border-b dark:border-DarkGray border-primary-500 py-2">
                    <input value={quizName} onChange={e => setQuizName(e.target.value)} className="appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="Quiz name" aria-label="quiz name" />
                </div>
            </div>
            <FormDialog
                question={
                    {

                        id: uuidv4(),
                        feedback: "",
                        question: "",
                        mark: "",
                        answers: [
                            {
                                id: uuidv4(),
                                answer: "",
                                is_correct: false,
                            },
                            {
                                id: uuidv4(),
                                answer: "",
                                is_correct: false,
                            },
                        ]
                    }
                }
                addQuestion={(question) => addQuestion(question)}
            />
            {questions && questions.map((question, index) => (
                <Question
                    key={question.id}
                    questionData={question}
                    updateQuestionData={(updatedQuestionData) => {
                        updateQuestionData(index, updatedQuestionData)
                    }}
                    deleteQuestion={() => deleteQuestion(question.id)}
                />
            ))}
            <div className='flex justify-end mt-10'>
                <button className='btn-inner mr-2'>Cancel</button>
                <button onClick={submit} className='btn-inner'>Save</button>
            </div>
        </div>
    );
};



export default CreateQuiz
