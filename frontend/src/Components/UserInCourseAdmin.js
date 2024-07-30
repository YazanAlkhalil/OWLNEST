import { Box, FormControl, InputLabel, MenuItem, Select } from '@mui/material'
import { MdClose } from 'react-icons/md'
import { CgDetailsMore } from "react-icons/cg";
import React from 'react'
import useFetch from './AuthComponents/UseFetch';
import toast from 'react-hot-toast';

function UserInCourseAdmin({ user, index, fetchUsers, isOwner }) {

    const { fetchData } = useFetch()
    async function deleteUser() {
        fetchData({ url: "http://127.0.0.1:8000/api/delete_user/" + user.id + "/", method: "POST" })
        fetchUsers()
    }
    async function changeRole() {
        if (user.roles.includes("admin")) {
            if(user.roles.length ===1){
                toast.custom((t) => (
                    <div
                        className={`${t.visible ? 'animate-enter' : 'animate-leave'
                            } max-w-md w-full bg-white shadow-lg rounded-lg pointer-events-auto flex ring-1 ring-black ring-opacity-5`}
                    >
                        <div className="flex-1 w-0 p-4">
                            <p>This user doesn't have any other rolls he will be removed from the company after this action do you wish to proceed</p>
                        </div>
                        <div className="flex border-l border-gray-200">
                            <button
                                onClick={
                                    () => {
                                        fetchData({ url: "http://127.0.0.1:8000/api/delete_admin/" + user.id + "/", method: "POST" })
                                        fetchUsers()
                                        toast.dismiss(t.id)
                                    }}
                                    className="w-full border border-transparent rounded-none rounded-r-lg p-4 flex items-center justify-center text-sm font-medium text-indigo-600 hover:text-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                                    >
                                Delete
                            </button>
                        </div>
                    </div>
                ))
            }
            else{
                fetchData({ url: "http://127.0.0.1:8000/api/delete_admin/" + user.id + "/", method: "POST" })
            }
        }
        else
            fetchData({ url: "http://127.0.0.1:8000/api/add_admin/" + user.id + "/", method: "POST" })
        fetchUsers()
    }
    return (
        <>
            <div className={`${index % 2 === 0 ? 'dark:bg-gray-700 bg-gray-200' : 'bg-white dark:bg-gray-900'} p-2 flex items-center rounded-l`}>
                {user.username}
            </div>
            <div className={`${index % 2 === 0 ? 'dark:bg-gray-700 bg-gray-200' : 'bg-white dark:bg-gray-900'} p-2`}>
                <Box sx={{ maxWidth: 200 }}>
                    <FormControl fullWidth>
                        <InputLabel id="roles-label">Roles</InputLabel>
                        <Select
                            labelId="roles-label"
                            id="roles-select"
                            value={user.roles}
                            label="Roles"
                            multiple
                            renderValue={(selected) => selected.join(', ')}
                            inputProps={{ readOnly: true }}
                        >
                            {user.roles.map((role) => (
                                <MenuItem key={role} value={role}>
                                    {role}
                                </MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                </Box>
            </div>
            <div className={`${index % 2 === 0 ? 'bg-gray-200 dark:bg-gray-700' : 'bg-white dark:bg-gray-900'} flex items-center p-2`}>
                {user.last_login ? new Date(user.last_login).toLocaleString() : 'Never'}
            </div>
            <div className={`${index % 2 === 0 ? 'bg-gray-200 dark:bg-gray-700' : 'bg-white dark:bg-gray-900'} p-2 rounded-r pl-0 flex items-center gap-6 justify-start`}>
                <CgDetailsMore className='size-6 dark:hover:bg-transparent hover:bg-white hover:cursor-pointer rounded-full p-2 box-content' />

                {isOwner =="true" && <MdClose onClick={deleteUser} className='size-6 dark:hover:bg-transparent hover:bg-white hover:cursor-pointer rounded-full p-2 box-content' />}
                {isOwner =="true" && <button onClick={changeRole} className='border dark:border-gray-200 dark:hover:border-white hover:border-2 rounded p-2'>{!user.roles.includes("admin") ? "Make Admin" : "Remove Admin"}</button>}
            </div>
        </>
    );
}
export default UserInCourseAdmin
