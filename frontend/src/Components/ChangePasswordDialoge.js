import { Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, Slide, TextField } from '@mui/material';
import React, { forwardRef, useState } from 'react';
// import { useParams } from 'react-router-dom';
// import useFetch from './AuthComponents/UseFetch';

const Transition = forwardRef(function Transition(props, ref) {
    return <Slide direction="up" ref={ref} {...props} />;
  });
export default function ChangePasswordDialoge({newPasswordClick}) {
  const [open, setOpen] = useState(false);
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };
  const handleSubmitClick = (e) =>{
    e.preventDefault();
    const data = {
      old_password: oldPassword,
      new_password: newPassword
    };
    newPasswordClick(data);
    handleClose(); 
  }
  
  return (
    <>
      <button className='text-xl border border-solid border-primary text-white font-semibold px-8 py-2 hover:bg-secondary hover:border-secondary bg-primary rounded ' onClick={handleClickOpen}>
        Change Password
      </button>
      <Dialog
        open={open}
        TransitionComponent={Transition}
        keepMounted
        onClose={handleClose}
        onSubmit={handleSubmitClick}
        PaperProps={{
          component: 'form',
        }}
      >
        <DialogTitle>Change your password</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Enter Your Old Password
          </DialogContentText>
          <TextField
            autoFocus
            required
            margin="dense"
            id="oldPass"
            name="oldPass"
            label="Old Password"
            type="text"
            fullWidth
            variant="standard"
            onChange={(e) => setOldPassword(e.target.value)}
          />
        </DialogContent>
        <DialogContent>
          <DialogContentText>
            Enter Your New Password
          </DialogContentText>
          <TextField
            autoFocus
            required
            margin="dense"
            id="newPass"
            name="newPass"
            label="New Password"
            type="text"
            fullWidth
            variant="standard"
            onChange={(e) => setNewPassword(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button type="submit">Edit</Button>
        </DialogActions>
      </Dialog>
    </>
  );
}
