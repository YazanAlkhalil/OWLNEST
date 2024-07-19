import { Box, FormControl, InputLabel, MenuItem, Select } from '@mui/material'
import { MdClose } from 'react-icons/md'
import { CgDetailsMore } from "react-icons/cg";
import React from 'react'

function UserInCourseAdmin({ user, index }) {
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
                <CgDetailsMore className='size-6 hover:bg-white hover:cursor-pointer rounded-full p-2 box-content' />
                <MdClose className='size-6 hover:bg-white hover:cursor-pointer rounded-full p-2 box-content' />
            </div>
        </>
    );
}
export default UserInCourseAdmin
