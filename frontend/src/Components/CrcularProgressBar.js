import React from 'react'
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar'

export default function CrcularProgressBar({value}) {
  return (
    <CircularProgressbar
    className='w-[150px] h-[150px] font-semibold'
      value={value}
      text={`${value}%`}
      strokeWidth='20'
      styles={buildStyles({
        pathColor: `#3F6188`,
        pathTransitionDuration: 2,
        trailColor: '#d6d6d6',
        textColor: 'black'
      })}
    />
  )
}
