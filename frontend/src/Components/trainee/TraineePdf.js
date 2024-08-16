import React, { useEffect } from 'react'
import PdfViewer from '../PdfViewer '
import TrainerPDFView from '../../Pages/trainer/TrainerPDFView'
import useFetch from '../AuthComponents/UseFetch'
import { useNavigate, useParams } from 'react-router-dom'

export default function TraineePdf() {
  const {fetchData} = useFetch()
  const lessonId = localStorage.getItem("lessonId")
  const {id} = useParams()
  const navigate = useNavigate()
  async function mark(){
    const res = await fetchData({url:`/course/${id}/mark-content/${lessonId}`,method:"POST"})
    navigate('/trainee/courses/'+id+"/content")
  }
  return (
    <div className='flex flex-col'>
    <TrainerPDFView trainee={true}/>
    <button onClick={mark} className='btn-inner self-end'>Mark as completed</button>
    </div>
  )
}
