import React from 'react'

export default function SimpleCard({title,value}) {
  return (
    <>
      <div className='dark:bg-DarkSecondary rounded w-[150px] h-[100px] text-center flex flex-col items-center justify-center content-center shadow-xl'>
        <h1 className='font-semibold text-2xl'>{value}</h1>
        <h1 className='font-semibold text-xl '>{title}</h1>
      </div>
    </>
  )
}
