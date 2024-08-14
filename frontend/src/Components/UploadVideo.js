import React, { useEffect, useRef, useState } from 'react'
import VideoDropzone from './VideoDropZone'
import { TextField } from '@mui/material';
import useFetch from './AuthComponents/UseFetch';
import { useParams } from 'react-router-dom';

function UploadVideo({ submit, backendContent }) {
  const [uploadedFile, setUploadedFile] = useState(null);
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const unitId = localStorage.getItem('unitId').slice(4)
  const companyId = localStorage.getItem('companyId')
  const { id } = useParams()
  const { fetchData } = useFetch()

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

  async function sendVideo() {
    let order = backendContent.find(unit => unit.id.toString() === unitId)?.contents.length
    const formData = new FormData()
    formData.append("type", "video")
    formData.append("title", name)
    formData.append("description", description)
    formData.append("file", uploadedFile)
    formData.append("order", order)
    await fetchData({ url: "http://127.0.0.1:8000/api/trainer/company/" + companyId + "/courses/" + id + "/unit/" + unitId + "/content/create", method: "POST", data: formData })
    submit()
  }



  return (
    <div className='flex flex-col '>
      <h1 className='text-3xl mb-4'>Enter lesson content</h1>
      <div className='w-1/4'>

        <TextField
          autoFocus
          margin="dense"
          id="name"
          name="email"
          label="Lesson name"
          type="text"
          fullWidth
          variant="standard"
          value={name}
          onChange={e => setName(e.target.value)}
        />
      </div>
      <VideoDropzone uploadedFile={uploadedFile} setUploadedFile={setUploadedFile} type={{
        'video/*': ['.mp4', '.mov', '.avi', '.mkv'],
      }} />
      <h1>Add a description</h1>
      <textarea
        className='p-2 border-solid border dark:bg-DarkGray border-gray-400'
        ref={textareaRef}
        rows="4"
        placeholder="Description..."
        style={{ resize: 'none' }}
        value={description}
        onChange={e => setDescription(e.target.value)}
      />
      <button onClick={sendVideo} className='hover:bg-accentHover bg-accent p-3 self-end text-white rounded mt-10 text-xl '>Submit</button>
    </div>
  )
}

export default UploadVideo
