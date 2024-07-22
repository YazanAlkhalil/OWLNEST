import React from 'react'
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar'
import { useSelector } from 'react-redux';

export default function CrcularProgressBar({value}) {
  const isDarkMode = useSelector((state) => state.theme.isDarkMode);

  return (
    <CircularProgressbar
    className='w-[150px] h-[150px] font-semibold'
      value={value}
      text={`${value}%`}
      strokeWidth='20'
      styles={buildStyles({
        pathColor: !isDarkMode ? "#001F34" :`#3F6188`,
        pathTransitionDuration: 2,
        trailColor: !isDarkMode? "#DBF2FF" :'#d6d6d6',
        textColor: !isDarkMode ? 'white' : 'black'
      })}
    />
  )
}
