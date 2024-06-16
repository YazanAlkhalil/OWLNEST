import { useState } from 'react'
import { DndContext,closestCenter } from '@dnd-kit/core';
import { arrayMove,SortableContext,verticalListSortingStrategy } from '@dnd-kit/sortable';
import Unit from './Unit';
import Lesson from './Lesson';
import image from '../images/course__cs101_courses_datastructuresfromctopython__course-promo-image-1653540139 1.png'
import FormDialog from './CreateUnitDialog'
import AdditionalInfo from './AdditionalInfo';
import UploadVideo from './UploadVideo';
import UploadPDF from './UploadPDF';
import CreateQuiz from './CreateQuiz';
function CourseEdit() {
  const [isInfo,setIsInfo] = useState(false)
  const [isUploadingVideo,setIsUploadingVideo] = useState(false)
  const [isUploadingPDF,setIsUploadingPDF] = useState(false)
  const [createQuiz,setCreateQuiz] = useState(false)
  const [sortable,setSortable] = useState(false)
  const [content, setContent] = useState([
    {
      type: "unit",
      name: "unit 1",
      id: "12",
    },
    {
      type: "lesson",
      content: "video",
      name: "video 1",
      id: "1",
    },
    {
      type: "lesson",
      content: "pdf",
      name: "pdf 1",
      id: "2",
    },
    {
      type: "lesson",
      content: "quiz",
      name: "quiz 1",
      id: "3",
    },
    {
      type: "unit",
      name: "unit 2",
      id: "23",
    },
    {
      type: "lesson",
      content: "quiz",
      name: "quiz 2",
      id: "4",
    },
    
    
  ])

  if(isInfo) 
  return <AdditionalInfo close={()=>setIsInfo(false)}/>

if(isUploadingVideo)
  return <UploadVideo submit={()=>setIsUploadingVideo(false)}/>
if(isUploadingPDF)
  return <UploadPDF submit={()=>setIsUploadingPDF(false)}/>
if(createQuiz)
  return <CreateQuiz submit={()=>setCreateQuiz(false)}/>
  
  function handleDragEnd(e){
    const {active,over} = e
    if(active.id !== over.id) {
      setContent((items) => {
        const activeIndex = items.findIndex(item => item.id === active.id);
        const overIndex = items.findIndex(item => item.id === over.id);
        return arrayMove(items, activeIndex, overIndex);
      });
  }}
  function addUnit(name) {

  }
  return (
      <>
      <div className='flex pb-10 justify-between '>
        <div className='flex'>
          <img className='mr-2 rounded w-44' src={image}/>
          <h1 >Course name</h1>
        </div>
        <div>
          <button className='text-xl border border-solid border-secondary px-3 py-2 hover:bg-secondary hover:text-white rounded  text-secondary' onClick={()=> setIsInfo(true)}>
            info
          </button>
        </div>
      </div>
      <div className='flex justify-end mb-4'>
        <button className='mr-2 text-xl border border-solid border-secondary px-3 py-2 hover:bg-secondary hover:text-white rounded  text-secondary' onClick={()=>setSortable(!sortable)}>
          reorder
        </button>
      <FormDialog />
      </div>
      <DndContext collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
    <div >
    
      <div >
        <SortableContext items={content} strategy={verticalListSortingStrategy}>
          {content.map((item) => {
            if(item.type == 'unit')
              return <Unit key={JSON.stringify(item)} createQuiz={()=> setCreateQuiz(true)} uploadVideo={()=> setIsUploadingVideo(true)} uploadPDF={()=>setIsUploadingPDF(true)}  sortable={sortable} item={item} />
            if(item.type == 'lesson')
              return <Lesson sortable={sortable} key={JSON.stringify(item)} item={item}/>
          })}
        </SortableContext>
      </div>
    </div>
      </DndContext>
      </>
  )
}

export default CourseEdit
