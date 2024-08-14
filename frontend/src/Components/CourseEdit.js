import { useEffect, useState } from 'react'
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
import { MdEdit } from 'react-icons/md';
import useFetch from '../Components/AuthComponents/UseFetch'
import { useParams } from 'react-router-dom';
import def from '../images/default-course-thumbnail.png'
import toast from 'react-hot-toast';

function CourseEdit({ inprogress }) {
  const [isInfo, setIsInfo] = useState(false)
  const [unitCount, setUnitCount] = useState(0)
  const [course, setCourse] = useState({
    image,
    name: 'www',
    description: "sdfa"
  })
  const [isUploadingVideo, setIsUploadingVideo] = useState(false)
  const [isUploadingPDF, setIsUploadingPDF] = useState(false)
  const [createQuiz, setCreateQuiz] = useState(false)
  const [sortable, setSortable] = useState(false)
  const [backendContent, setBackendContent] = useState(false)
  const { fetchData } = useFetch()
  const companyId = localStorage.getItem('companyId')
  const { id } = useParams()
  const [content, setContent] = useState([])
  const getInfo = async () => {
    let res
    if (inprogress)
      res = await fetchData({ url: "http://127.0.0.1:8000/api/trainer/company/" + companyId + "/progress_courses/" + id })
    else
      res = await fetchData({ url: "http://127.0.0.1:8000/api/trainer/company/" + companyId + "/courses/" + id })

    if (res.id) {
      setCourse({
        name: res.name,
        image: res.image,
        description: res.pref_description
      })
      // get the content in a different format for reordering
      const tempContent = []
      setUnitCount(res.units.length)
      setBackendContent(res.units)
      res.units.forEach(unit => {

        tempContent.push({
          type: "unit",
          title: unit.title,
          id: "unit" + unit.id,
        })

        unit.contents.forEach(lesson => {
          let content;
        content = lesson.type
          tempContent.push({
            type: "lesson",
            content,
            title: lesson.title,
            id: "lesson" + lesson.id,
          })
        })
      })
      setContent(tempContent)
    }
  }
  useEffect((
  ) => {
    getInfo()
  }, [])
  if (isInfo)
    return <AdditionalInfo close={() => { setIsInfo(false); getInfo() }} />
  console.log(backendContent);
  if (isUploadingVideo)
    return <UploadVideo backendContent={backendContent} submit={() => { setIsUploadingVideo(false); getInfo() }} />
  if (isUploadingPDF)
    return <UploadPDF backendContent={backendContent} submit={() => { setIsUploadingPDF(false); getInfo() }} />
  if (createQuiz)
    return <CreateQuiz backendContent={backendContent} submit={() => { setCreateQuiz(false); getInfo() }} />

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
  async function addUnit(name) {
    await fetchData({ url: "http://127.0.0.1:8000/api/trainer/company/" + companyId + "/courses/" + id + "/unit/create", method: "POST", data: { title: name ,order:unitCount } })
    getInfo()
  }

  async function publish() {
    const res = fetchData({ url: "http://127.0.0.1:8000/api/trainer/company/" + companyId + "/courses/" + id + "/publish", method: "POST" })
    toast.success('course published successfully wait for admins approval')
  }

  async function handleReorder(){
    console.log(content);
    let units = []
    let counterLesson = 0
    content.forEach((item) =>{
      if(item.type == "unit"){
        units.push({
          id:item.id.slice(4),
          order:units.length,
          contents:[]
        })
        counterLesson = 0
      }
      else{
        units[units.length-1].contents.push({
          id:item.id.slice(6),
          order:counterLesson,
        })
        counterLesson++;
      }
    })
    setSortable(!sortable)
    if(sortable){
      const res = fetchData({ url: "http://127.0.0.1:8000/api/trainer/company/" + companyId + "/course/" + id + "/reorder", method: "POST",data:{units} })

    }
  }

  async function changeImage(e){
    const formData = new FormData();
    formData.append("image",e.target.files[0])
    const res = await fetchData({url:"course/"+id,method:"PATCH",data:formData})
    getInfo()
  }


  return (
    <>
      <div className='flex justify-between '>
        <div className='flex w-full'>
          <div className='group relative mr-4 rounded w-2/6'>
            <img className='w-full' src={course.image ? course.image : def} />
            <input onChange={changeImage} id='courseImage' type='file' className='hidden' />
            <label htmlFor='courseImage'>
              <MdEdit className='hidden group-hover:block absolute -right-5 -bottom-5 p-3 box-content rounded-full bg-secondary dark:bg-DarkSecondary size-6 hover:cursor-pointer dark:hover:bg-DarkGrayHover' />
            </label>
          </div>
          <div className='flex-grow'>
            <h1 className='text-xl font-bold'>{course.name}</h1>
            <p className='mt-4 text-md font-light'>{course.description} </p>
          </div>
        </div>
        <div>
          <button className='text-xl border border-solid border-secondary px-3 py-2 hover:bg-secondary dark:text-white hover:text-white rounded  text-secondary' onClick={() => setIsInfo(true)}>
            info
          </button>
        </div>
      </div>
      <div className='flex justify-end mb-4'>
        <button onClick={handleReorder} className='mr-2 btn-inner text-xl border border-solid border-secondary px-3 py-2 hover:bg-secondary hover:text-white rounded  text-secondary' >
          {sortable ? 'save' : 'reorder'}
        </button>
        <FormDialog addUnit={addUnit} />
      </div>
      <DndContext collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
        <div >

          <div >
            <SortableContext items={content} strategy={verticalListSortingStrategy}>
              {
                content.map((item) => {
                  if (item.type == 'unit')
                    return <Unit key={item.id} getInfo={getInfo} createQuiz={() => setCreateQuiz(true)} uploadVideo={() => setIsUploadingVideo(true)} uploadPDF={() => setIsUploadingPDF(true)} sortable={sortable} item={item} />
                  else
                    return <Lesson sortable={sortable} getInfo={getInfo} key={item.id} item={item} />
                })}
            </SortableContext>
          </div>
        </div>
      </DndContext>
      <div className='flex justify-end mt-10'>

        <button onClick={publish} className='p-2 bg-accent rounded text-xl ml-auto'>Submit</button>
      </div>
    </>
  )
}

export default CourseEdit
