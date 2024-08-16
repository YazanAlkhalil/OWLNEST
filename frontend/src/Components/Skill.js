import React from 'react'
import LinearProgress, { linearProgressClasses } from '@mui/material/LinearProgress';
import { styled } from '@mui/material/styles';
const BorderLinearProgress = styled(LinearProgress)(({ theme }) => ({
    height: 10,
    borderRadius: 5,
    [`&.${linearProgressClasses.colorPrimary}`]: {
        backgroundColor: theme.palette.grey[theme.palette.mode === 'light' ? 200 : 800],
    },
    [`& .${linearProgressClasses.bar}`]: {
        borderRadius: 5,
        backgroundColor: theme.palette.mode === 'light' ? '#1a90ff' : '#308fe8',
    },
}));

function Skill({ name, value }) {
    return (
        <div className='flex py-4 mb-3 border-b items-center justify-between'>
            <h1 className=''>{name}</h1>
            <div className='flex-grow flex items-center justify-end'>
                <div className='mr-4'>{value}%</div>
                <BorderLinearProgress className='w-3/4' variant="determinate" value={value} />
            </div>
        </div>
    )
}

export default Skill
