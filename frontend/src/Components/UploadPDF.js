import React, { useState } from 'react'
import VideoDropzone from './VideoDropZone'

function UploadPDF({ submit }) {
  const [name,setName]= useState('')
  return (
    <div className='flex flex-col'>
      <h1 className='text-3xl mb-4'>Enter lesson content</h1>
      <div className="flex w-min items-center border-b border-primary-500 py-2">
        <input value={name} onChange={e => setName(e.target.value)} className="text-xl appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="lesson name" aria-label="lesson name" />
      </div>
      <VideoDropzone type={{
        'application/pdf': ['.pdf'],
      }} />
      <button onClick={submit} className='bg-primary p-3 self-end text-white rounded mt-10 text-xl hover:bg-hover'>Submit</button>

    </div>
  )
}

export default UploadPDF
