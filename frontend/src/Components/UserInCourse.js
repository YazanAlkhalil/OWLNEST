import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

import { BsClockHistory } from "react-icons/bs";




import { PiPlus, PiMinus } from 'react-icons/pi'
import useFetch from './AuthComponents/UseFetch';
import { useParams } from 'react-router-dom';
import toast from 'react-hot-toast';
function UserInCourse({ user, index,getUsers }) {

    const [role, setRole] = React.useState(user.role ? user.role : '');
    const {fetchData}=useFetch()
    const {id} = useParams()

    const handleChange = (event) => {
        if(!user.is_participant)
            setRole(event.target.value);
        
    };

    async function handleDelete(){
        await fetchData({url:"http://127.0.0.1:8000/api/course/"+id+"/remove-user",method:"DELETE",data:{ user_id:user.id}})
        getUsers()
        setRole("")
    }
    async function handleAdd(){
        if(role){
            await fetchData({url:"http://127.0.0.1:8000/api/course/"+id+"/users",method:"POST",data:{email:user.email, role}})
            getUsers()
        }
        else
            toast.error('Choose a role')
    }
    console.log(user.role ? user.role : role,"role");
    return (
        <>
            <div className={`${index % 2 == 0 ? 'bg-gray-200 dark:bg-gray-700' : 'bg-white dark:bg-gray-900'}  p-2 rounded-l`}>{user.username}</div>
            <div className={`${index % 2 == 0 ? 'bg-gray-200 dark:bg-gray-700' : 'bg-white dark:bg-gray-900'}  p-2 `}>
                <Box sx={{ maxWidth: 100 }}>
                    <FormControl fullWidth>
                        <InputLabel id="demo-simple-select-label">Role</InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            value={user.role ? user.role : role}
                            label="Age"
                            onChange={handleChange}
                        >
                            <MenuItem value={"trainee"}>Trainee</MenuItem>
                            <MenuItem value={"trainer"}>Trainer</MenuItem>
                        </Select>
                    </FormControl>
                </Box>
            </div>
            <div className={`${index % 2 == 0 ? 'bg-gray-200 dark:bg-gray-700' : 'bg-white dark:bg-gray-900'}  p-2  `}> {user.completion_date? user.completion_date :"Not yet"}</div>
            <div className={`${index % 2 == 0 ? 'bg-gray-200 dark:bg-gray-700' : 'bg-white dark:bg-gray-900'} p-2 rounded-r pl-10`}>{user.is_participant ? <PiMinus onClick={handleDelete} className=' hover:cursor-pointer bg-white dark:bg-transparent  p-2 box-content rounded' /> : <PiPlus onClick={handleAdd} className=' hover:cursor-pointer bg-white dark:bg-transparent  p-2 box-content rounded' />}</div>
        </>
    )
}

export default UserInCourse
