import { Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, TextField } from '@mui/material';
import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import useFetch from './AuthComponents/UseFetch';

export default function AddComment({ addNewComment }) {
  const [open, setOpen] = useState(false);
  const [text, setText] = useState('');
  const { fetchData } = useFetch();
  const { id } = useParams();

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const dataToSend = { text: text };
    const res = await fetchData({ url: 'http://127.0.0.1:8000/api/course/' + id + '/comments', method: 'post', data: dataToSend });
    if (res) {
      addNewComment(res);
    }
    handleClose();
  };

  return (
    <>
      <button className='text-xl border border-solid border-secondary font-semibold px-8 py-2 hover:bg-secondary hover:text-white rounded text-secondary' onClick={handleClickOpen}>
        Comment
      </button>
      <Dialog
        open={open}
        onClose={handleClose}
        PaperProps={{
          component: 'form',
          onSubmit: handleSubmit,
        }}
      >
        <DialogTitle>New Comment</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Enter Your Comment
          </DialogContentText>
          <TextField
            autoFocus
            required
            margin="dense"
            id="Comment"
            name="Comment"
            label="Comment"
            type="text"
            fullWidth
            variant="standard"
            onChange={(e) => setText(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button type="submit">Add</Button>
        </DialogActions>
      </Dialog>
    </>
  );
}
