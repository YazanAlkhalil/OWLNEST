import React, { useEffect, useRef, useState } from 'react'
import VideoDropzone from './VideoDropZone'

function UploadVideo({ submit }) {
  const [name, setName] = useState('')

  const textareaRef = useRef(null);

  useEffect(() => {
    const adjustHeight = () => {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight + 2}px`;
    };

    adjustHeight();

    const textarea = textareaRef.current;
    textarea.addEventListener('input', adjustHeight);

    return () => {
      textarea.removeEventListener('input', adjustHeight);
    };
  }, []);
  return (
    <div className='flex flex-col '>
      <h1 className='text-3xl mb-4'>Enter lesson content</h1>
      <div className="flex w-min items-center border-b border-primary-500 py-2">
        <input value={name} onChange={e => setName(e.target.value)} className="text-xl appearance-none bg-transparent border-none text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none" type="text" placeholder="lesson name" aria-label="lesson name" />
      </div>
      <VideoDropzone type={{
        'video/*': ['.mp4', '.mov', '.avi', '.mkv'],
      }} />
      <h1>Add a description</h1>
      <textarea
        className='p-2 border-solid border border-gray-400'
        ref={textareaRef}
        rows="4"
        placeholder="Description..."
        style={{ resize: 'none' }}
      />
      <button onClick={submit} className='bg-primary p-3 self-end text-white rounded mt-10 text-xl hover:bg-hover'>Submit</button>
    </div>
  )
}

export default UploadVideo
