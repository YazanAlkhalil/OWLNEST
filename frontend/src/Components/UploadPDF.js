import React, { useState } from 'react'
import VideoDropzone from './VideoDropZone'
import { TextField } from '@mui/material'
import { useParams } from 'react-router-dom'
import useFetch from './AuthComponents/UseFetch'

function UploadPDF({ submit,backendContent}) {
  const [uploadedFile, setUploadedFile] = useState(null);
  const [order, setOrder] = useState(0);
  const [name, setName] = useState('')
  const unitId = localStorage.getItem('unitId').slice(4)
  const companyId = localStorage.getItem('companyId')
  const {id} = useParams()
  const {fetchData} = useFetch()

  async function sendPdf(){
    let order = backendContent.find(unit => unit.id.toString() === unitId)?.contents.length

    const formData = new FormData()
    formData.append("type","pdf")
    formData.append("title",name)
    formData.append("file",uploadedFile)
    formData.append("order", order)
    await fetchData({url:"http://127.0.0.1:8000/api/trainer/company/"+companyId+"/courses/"+id+"/unit/"+unitId+"/content/create",method:"POST",data:formData})
    submit()
  }


  return (
    <div className='flex flex-col'>
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
        'application/pdf': ['.pdf'],
      }} />
      <button onClick={sendPdf} className=' bg-accent p-3 self-end text-white rounded mt-10 text-x hover:bg-accentHover'>Submit</button>

    </div>
  )
}

export default UploadPDF
