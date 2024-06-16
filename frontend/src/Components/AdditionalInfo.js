import React, { useEffect, useRef } from 'react'
import { IoMdClose } from "react-icons/io";
function AdditionalInfo({close}) {
    const textareaRef = useRef(null);

  useEffect(() => {
    const adjustHeight = () => {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    };

    adjustHeight(); 

    const textarea = textareaRef.current;
    textarea.addEventListener('input', adjustHeight);

    return () => {
      textarea.removeEventListener('input', adjustHeight);
    };
  }, []);
  return (
    <div className='flex flex-col'>
    <IoMdClose className='self-end hover:cursor-pointer size-7' onClick={close}/>
      <button className='mb-6 h-auto self-start text-xl border border-solid border-secondary p-3 hover:bg-secondary hover:text-white rounded  text-secondary'>skills</button>
      <textarea
      className='p-2 border-solid border border-gray-400'
      ref={textareaRef}
      rows="4"
      placeholder="Add additional resources..."
      style={{ resize: 'none' }}
    />
    </div>
  )
}

export default AdditionalInfo
