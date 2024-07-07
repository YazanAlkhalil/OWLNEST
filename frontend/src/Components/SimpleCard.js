import React from 'react'

export default function SimpleCard(props) {
  return (
    <>
      <div className='rounded w-[150px] h-[100px] text-center flex flex-col items-center justify-center content-center shadow-xl'>
        <h1 className='font-semibold text-2xl'>{props.values.value}</h1>
        <h1 className='font-semibold text-xl '>{props.values.title}</h1>
      </div>
    </>
  )
}
