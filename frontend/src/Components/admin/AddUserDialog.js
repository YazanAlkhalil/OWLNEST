import * as React from 'react';
import { useState } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import toast from 'react-hot-toast'
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

export default function FormDialog() {
    const [name, setName] = useState('')
    const [role, setRole] = useState('')
    const [open, setOpen] = useState(false)

    const handleChange = (event) => {
        setRole(event.target.value);
    };

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };
    function reset() {
        setName('')
        setRole('')
        handleClose()
    }
    function handleSubmit() {

    }
    return (
        <React.Fragment>
            <div onClick={handleClickOpen}
                className='bg-primary self-end mb-5 hover:bg-hover hover:cursor-pointer text-white p-3 rounded'>Add user</div>

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
                <DialogTitle>Add User</DialogTitle>
                <DialogContent >
                    <div className="w-96 flex items-center border-b border-primary-500 py-2 mb-5">
                        <input  value={name} onChange={e => {
                            const value = e.target.value;
                            if(value.length <=50){
                                setName( value )}} 
                            }
                            className="w-full appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="Name" aria-label="Name" />
                    </div>
                    <Box sx={{ maxWidth: 100 }}>
                    <FormControl fullWidth>
                        <InputLabel id="demo-simple-select-label">Role</InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            value={role}
                            label="Role"
                            onChange={handleChange}
                        >
                            <MenuItem value={"trainee"}>Trainee</MenuItem>
                            <MenuItem value={"trainer"}>Trainer</MenuItem>
                            <MenuItem value={"admin"}>Admin</MenuItem>
                        </Select>
                    </FormControl>
                </Box>
                    
                </DialogContent>
                <DialogActions>
                    <Button onClick={reset}>Cancel</Button>
                    <Button onClick={handleSubmit} type="submit">Add</Button>
                </DialogActions>
            </Dialog>
        </React.Fragment>
    );
}
