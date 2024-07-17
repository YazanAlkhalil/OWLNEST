import { useState } from 'react'
import { DndContext, closestCenter } from '@dnd-kit/core';
import { arrayMove, SortableContext, verticalListSortingStrategy } from '@dnd-kit/sortable';
import Unit from './Unit';
import Lesson from './Lesson';
import image from '../images/course__cs101_courses_datastructuresfromctopython__course-promo-image-1653540139 1.png'
import FormDialog from './CreateUnitDialog'
import AdditionalInfo from './AdditionalInfo';
import UploadVideo from './UploadVideo';
import UploadPDF from './UploadPDF';
import CreateQuiz from './CreateQuiz';
import { BiArrowBack } from "react-icons/bi";

function CourseEdit() {
  const [isInfo, setIsInfo] = useState(false)
  const [course,setCourse]=useState({
    image,
    name:'www',
    description:"sdfa"
  })
  const [isUploadingVideo, setIsUploadingVideo] = useState(false)
  const [isUploadingPDF, setIsUploadingPDF] = useState(false)
  const [createQuiz, setCreateQuiz] = useState(false)
  const [sortable, setSortable] = useState(false)
  const [content, setContent] = useState([
    {
      type: "unit",
      title: "unit 1",
      id: "12",
    },
    {
      type: "lesson",
      content: "video",
      title: "video 1",
      id: "1",
    },
    {
      type: "lesson",
      content: "pdf",
      title: "pdf 1",
      id: "2",
    },
    {
      type: "lesson",
      content: "quiz",
      title: "quiz 1",
      id: "3",
    },
    {
      type: "unit",
      title: "unit 2",
      id: "23",
    },
    {
      type: "lesson",
      content: "quiz",
      title: "quiz 2",
      id: "4",
    },


  ])

  if (isInfo)
    return <AdditionalInfo close={() => setIsInfo(false)} />

  if (isUploadingVideo)
    return <UploadVideo submit={() => setIsUploadingVideo(false)} />
  if (isUploadingPDF)
    return <UploadPDF submit={() => setIsUploadingPDF(false)} />
  if (createQuiz)
    return <CreateQuiz submit={() => setCreateQuiz(false)} />

  function handleDragEnd(e) {
    const { active, over } = e
    if (active.id !== over.id) {
      setContent((items) => {
        const activeIndex = items.findIndex(item => item.id === active.id);
        const overIndex = items.findIndex(item => item.id === over.id);
        return arrayMove(items, activeIndex, overIndex);
      });
    }
  }
  function addUnit(name) {

  }
  return (
    <>
      <div className='flex justify-between '>
        <div className='flex w-full'>
          <img className='mr-4 rounded w-2/6' src={course.image} />
          <div className='flex-grow'>
            <h1 className='text-xl font-bold'>{course.name}</h1>
            <p className='mt-4 text-md font-light'>{course.description} </p>
          </div>
        </div>
        <div>
          <button className='text-xl border border-solid border-secondary px-3 py-2 hover:bg-secondary hover:text-white rounded  text-secondary' onClick={() => setIsInfo(true)}>
            info
          </button>
        </div>
      </div>
      <div className='flex justify-end mb-4'>
        <button className='mr-2 text-xl border border-solid border-secondary px-3 py-2 hover:bg-secondary hover:text-white rounded  text-secondary' >
          {sortable ? 'save' : 'reorder'}
        </button>
        <FormDialog addUnit={addUnit}/>
      </div>
      <DndContext collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
        <div >

          <div >
            <SortableContext items={content} strategy={verticalListSortingStrategy}>
              {
              content.map((item) => {
                if (item.type == 'unit')
                  return <Unit key={item.id} createQuiz={() => setCreateQuiz(true)} uploadVideo={() => setIsUploadingVideo(true)} uploadPDF={() => setIsUploadingPDF(true)} sortable={sortable} item={item} />
                else
                  return <Lesson sortable={sortable} key={item.id} item={item} />
              })}
            </SortableContext>
          </div>
        </div>
      </DndContext>
    </>
  )
}

export default CourseEdit
