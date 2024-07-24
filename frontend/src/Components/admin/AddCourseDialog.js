import * as React from 'react';
import { useState } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import toast from 'react-hot-toast'
import useFetch from '../AuthComponents/UseFetch';
import { useSelector } from 'react-redux';


export default function FormDialog() {
    const { fetchData } = useFetch()
    const companyId = localStorage.getItem('companyId')
    const isDarkMode = useSelector((state) => state.theme.isDarkMode);

    const [info, setInfo] = useState({
        name: "",
        pref_description: "",
    })
    const [open, setOpen] = useState(false)
    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };
    function reset() {
        setInfo({
            name: "",
            pref_description: "",
        })
        handleClose()
    }

    return (
        <React.Fragment>
            <div onClick={handleClickOpen}
                className='bg-primary dark:bg-DarkGray  dark:hover:bg-DarkGrayHover self-end mb-5 hover:bg-hover hover:cursor-pointer text-white p-3 rounded'>Add course</div>

            <Dialog
                open={open}
                onClose={handleClose}
                PaperProps={{
                    component: 'form',
                    onSubmit: async (event) => {
                        event.preventDefault();
                        let res = await fetchData({ url: 'http://127.0.0.1:8000/api/admin/company/' + companyId + '/courses/create', method: 'POST', data: info })
                        console.log(res, "res");
                        if (res?.id) {
                            toast.success('Course added successfully')
                            reset()
                        }
                    },
                }}
            >
                <DialogTitle>Add course</DialogTitle>
                <DialogContent >
                    <div className="w-96 flex items-center border-b dark:border-DarkGray border-primary-500 py-2 mb-5">
                        <input value={info.name} onChange={e => {
                            const value = e.target.value;
                            if (value.length <= 50) {

                                setInfo({ ...info, name: value })
                            }
                        }
                        }
                            className="w-full appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="Name" aria-label="Name" />
                        <span className='ml-1 w-4'>{50 - info.name.length}</span>
                    </div>
                    <div className='flex items-end'>

                        <textarea
                            value={info.pref_description}
                            onChange={e => {
                                const value = e.target.value; if (value.length <= 350)
                                    setInfo({ ...info, pref_description: e.target.value })
                            }}
                            className={`${!isDarkMode ? "bg-[rgb(56,56,56)]" : ""} p-2 flex-grow  border-solid border border-gray-400`}
                            
                            rows="4"
                            maxLength={350}
                            placeholder="Description (max 350 characters)"
                            style={{ resize: 'none' }}
                        />
                        <span className='ml-1 w-4'>{350 - info.pref_description.length}</span>

                    </div>
                </DialogContent>
                <DialogActions>
                    <Button onClick={reset}>Cancel</Button>
                    <Button type="submit">Add</Button>
                </DialogActions>
            </Dialog>
        </React.Fragment>
    );
}
