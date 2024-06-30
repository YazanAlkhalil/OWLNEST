import { Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, TextField } from '@mui/material';
import React, { useState } from 'react'

export default function AddReply() {
    const [open, setOpen] = useState(false);
    const handleClickOpen = () => {
        setOpen(true)
    }
    const handleClose = () => {
        setOpen(false)
    }
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
          onSubmit: (event) => {
            event.preventDefault();
            const formData = new FormData(event.currentTarget);
            const formJson = Object.fromEntries(formData.entries());
            const email = formJson.email;
            handleClose();
          },
        }}
      >
        <DialogTitle>New Comment</DialogTitle>
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
