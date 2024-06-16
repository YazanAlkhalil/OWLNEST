import * as React from 'react';
import { useState } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import AnswerList from './AnswerList';
import { MdEdit } from "react-icons/md";

import toast from 'react-hot-toast'


export default function FormDialog({ question, updateQuestionData }) {
    const [questionData, setQuestionData] = useState(question)
    const [open, setOpen] = useState(false)
    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };
   
    function handleSubmit() {
        if (questionData.answers.length <= 1)
            return toast.error('there should be at least two answers')
       let isEmptyAnswer = questionData.answers.find(answer => answer.grade == '' || answer.text == '');
        if (isEmptyAnswer) {
            return toast.error('there should not be an empty answers')
        }
        updateQuestionData(questionData)
        handleClose();
    }
    return (
        <React.Fragment>
            <MdEdit onClick={handleClickOpen} className='ml-2 box-content p-2 mt-4 size-6 text-white rounded-full bg-secondary hover:bg-hover' />
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
                <DialogTitle className='-mb-5'>Answers</DialogTitle>
                <DialogContent >
                    <AnswerList answers={questionData.answers} updateAnswers={(updateAnswers) => setQuestionData({ ...questionData, answers: updateAnswers })} />
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose}>Cancel</Button>
                    <Button onClick={handleSubmit} type="submit">Save</Button>
                </DialogActions>
            </Dialog>
        </React.Fragment>
    );
}
