import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

import { BsClockHistory } from "react-icons/bs";




import { PiPlus, PiMinus } from 'react-icons/pi'
function UserInCourse({ user, index }) {

    const [role, setRole] = React.useState(user.role);

    const handleChange = (event) => {
        setRole(event.target.value);
    };



    return (
        <>
            <div className={`${index % 2 == 0 ? 'bg-gray-200' : 'bg-white'}  p-2 rounded-l`}>{user.name}</div>
            <div className={`${index % 2 == 0 ? 'bg-gray-200' : 'bg-white'}  p-2 `}>
                <Box sx={{ maxWidth: 100 }}>
                    <FormControl fullWidth>
                        <InputLabel id="demo-simple-select-label">Role</InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            value={role}
                            label="Age"
                            onChange={handleChange}
                        >
                            <MenuItem value={"trainee"}>Trainee</MenuItem>
                            {user.role == 'trainer' && <MenuItem value={"trainer"}>Trainer</MenuItem>}
                        </Select>
                    </FormControl>
                </Box>
            </div>
            <div className={`${index % 2 == 0 ? 'bg-gray-200' : 'bg-white'}  p-2  `}> {user.completionDate }</div>
            <div className={`${index % 2 == 0 ? 'bg-gray-200' : 'bg-white'} p-2 rounded-r pl-10`}>{user.isParticipant ? <PiMinus className=' hover:cursor-pointer bg-white   p-2 box-content rounded' /> : <PiPlus className=' hover:cursor-pointer bg-white p-2 box-content rounded' />}</div>
        </>
    )
}

export default UserInCourse
