import React, { useEffect } from 'react'
import PdfViewer from '../PdfViewer '
import TrainerPDFView from '../../Pages/trainer/TrainerPDFView'
import useFetch from '../AuthComponents/UseFetch'
import { useNavigate, useParams } from 'react-router-dom'
import { useDispatch } from 'react-redux'
import { toggleChat } from '../../features/chatSlice'
import ChatComponent from './chatComponent'

export default function TraineePdf() {
  const {fetchData} = useFetch()
  const lessonId = localStorage.getItem("lessonId")
  const {id} = useParams()
  const navigate = useNavigate()
  const dispatch = useDispatch()
  async function mark(){
    const res = await fetchData({url:`/course/${id}/mark-content/${lessonId}`,method:"POST"})
    if(res.status === "passed"){
      navigate(`/trainee/courses/${id}/content/Congratulations`)
    }else{
      navigate(`/trainee/courses/${id}/content`)
    }
  }
  return (
    <div className='flex flex-col'>
    <TrainerPDFView trainee={true}/>
    <button onClick={mark} className='btn-inner self-end'>Mark as completed</button>
    <div
        onClick={() => dispatch(toggleChat())}
        className='bg-white border-2 border-primary fixed right-10 bottom-4 text-white  size-20 rounded-full flex justify-center items-center hover:bg-background hover:cursor-pointer'>
        <img src="data:image/png;base64,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" />
      </div>
      <ChatComponent />
    </div>
  )
}
