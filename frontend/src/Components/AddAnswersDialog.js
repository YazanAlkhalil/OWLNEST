import * as React from 'react';
import { useState } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import AnswerList from './AnswerList';
import { v4 as uuidv4 } from 'uuid';
import toast from 'react-hot-toast'


export default function FormDialog({question,addQuestion}) {
    const [questionData,setQuestionData] = useState(question)
    const [open,setOpen]= useState(false)
    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };
    function reset(){
        setQuestionData({
            id:uuidv4(),
            text:"",
            grade:"",
            answers:[
                {
                    id:uuidv4(),
                    text:"",
                    isCorrect: false,
                },
                {
                    id:uuidv4(),
                    text:"",
                    isCorrect: false,
                },
            ]
        })
        handleClose()
    }
    function handleSubmit(){
        if(questionData.answers.length <= 1)
            return toast.error('there should be at least two answers')
         if(questionData.text == "" || questionData.grade == '')
            return toast.error('please fill in all fields')
        let isEmptyAnswer = questionData.answers.find(answer => answer.text == '');
        if(isEmptyAnswer){
           return toast.error('there should not be an empty answers')
        }
        addQuestion(questionData)
        reset()
        handleClose();
    }
    return (
        <React.Fragment>
            <button className='self-end mb-6 h-auto text-xl border border-solid border-secondary p-3 hover:bg-secondary hover:text-white rounded  text-secondary sticky top-1' onClick={handleClickOpen}>
                Add question
            </button>
            <Dialog
                open={open}
                onClose={handleClose}
                PaperProps={{
                    component: 'form',
                    onSubmit: (event) => {
                        event.preventDefault();

                        
                    },
                }}
            >
                <DialogTitle>Question</DialogTitle>
                <DialogContent >
                    <div className='flex'>

                        <div className="flex w-min items-center border-b border-primary-500 py-2">
                            <input value={questionData.text} onChange={e => setQuestionData({...questionData,text:e.target.value})} className="appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="Question" aria-label="question" />
                        </div>
                        <div className="flex w-min items-center border-b border-primary-500 py-2">
                            <input value={questionData.grade} onChange={e => setQuestionData({...questionData,grade:e.target.value})} className="appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="number" placeholder="Grade" aria-label="grade" />
                        </div>
                    </div>
                    <AnswerList answers={questionData.answers} updateAnswers={(updateAnswers) => setQuestionData({...questionData,answers:updateAnswers})}/>
                </DialogContent>
                <DialogActions>
                    <Button onClick={reset}>Cancel</Button>
                    <Button onClick={handleSubmit} type="submit">Add</Button>
                </DialogActions>
            </Dialog>
        </React.Fragment>
    );
}
