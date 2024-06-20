import { Box, FormControl, InputLabel, MenuItem, Select } from '@mui/material'
import { MdClose} from 'react-icons/md'
import { CgDetailsMore } from "react-icons/cg";
import React from 'react'

function UserInCourseAdmin({user,index}) {
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
                            <MenuItem value={"trainer"}>Trainer</MenuItem>
                            <MenuItem value={"admin"}>Admin</MenuItem>
                        </Select>
                    </FormControl>
                </Box>
            </div>
            <div className={`${index % 2 == 0 ? 'bg-gray-200' : 'bg-white'}  p-2  `}> {user.completionDate }</div>
            <div className={`${index % 2 == 0 ? 'bg-gray-200' : 'bg-white'} p-2 rounded-r pl-0 flex items-center gap-6 justify-start`}>
                <CgDetailsMore  className='size-6 hover:bg-white hover:cursor-pointer rounded-full p-2 box-content'/>
                <MdClose className='size-6 hover:bg-white hover:cursor-pointer rounded-full p-2 box-content'/>
            </div>
        </>
  )
}

export default UserInCourseAdmin
