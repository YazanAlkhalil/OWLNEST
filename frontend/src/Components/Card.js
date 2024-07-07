import React from 'react'

function Card({title,value}) {
  return (
    <div className=' text-xl px-10 my-4 shadow-md p-2 rounded text-white bg-secondary flex flex-col items-center'>
      <div className='mb-2'>{title}</div>
      <div>{value}</div>
    </div>
  )
}

export default Card
