import { Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, TextField } from '@mui/material';
import React, { useState } from 'react'
import useFetch from './AuthComponents/UseFetch';
import { useParams } from 'react-router-dom';

export default function AddReply({commentId,addNewReply}) {
    const [open, setOpen] = useState(false);
    const [text, setText] = useState('');
    const { fetchData  } = useFetch();
    const { id } = useParams();
    const handleClickOpen = () => {
        setOpen(true)
    }
    const handleClose = () => {
        setOpen(false)
    }
    const handleNewReplyClick = async (event) => {
      event.preventDefault();
      console.log(text);
      const data = {
        comment: commentId,
        text : text
      }
      const res = await fetchData({url: 'http://127.0.0.1:8000/api/course/'+id+'/comments/reply', method: 'post',data: data}) 
      console.log(res);
      if(res){
        addNewReply(res);
      }
      handleClose();
    };
  return (
    <>
      <button className='text-xl font-semibold text-white bg-gray-400 px-6 py-2' onClick={handleClickOpen}>
        Reply
      </button>
      <Dialog
        open={open}
        onClose={handleClose}
        PaperProps={{
          component: 'form',
          onSubmit: handleNewReplyClick
        }}
      >
        <DialogTitle>New Reply</DialogTitle>
        <DialogContent>
          <DialogContentText>
           Enter Your Reply
          </DialogContentText>
          <TextField
            autoFocus
            required
            margin="dense"
            id="Reply"
            name="Reply"
            label="Reply"
            type="text"
            fullWidth
            variant="standard"
            onChange={(e)=> setText(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button type="submit">Add</Button>
        </DialogActions>
      </Dialog>
    </>
  )
}
