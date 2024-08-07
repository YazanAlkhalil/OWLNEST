import React, { useEffect, useState } from 'react'
import Unit from '../Unit';
import Lesson from '../Lesson';
import image from '../../images/course__cs101_courses_datastructuresfromctopython__course-promo-image-1653540139 1.png'
import FormDialog from '../CreateUnitDialog'
import AdditionalInfo from '../AdditionalInfo';
import useFetch from '../AuthComponents/UseFetch'
import { useParams } from 'react-router-dom';
import def from '../../images/default-course-thumbnail.png'

function PendingCourseDetails() {
    const [course, setCourse] = useState({
        image,
        name: 'www',
        description: "sdfa"
    })

    const { fetchData } = useFetch()
    const companyId = localStorage.getItem('companyId')
    const { id } = useParams()
    const [content, setContent] = useState([])

    const getInfo = async () => {
        const res = await fetchData({ url: "http://127.0.0.1:8000/api/trainer/company/" + companyId + "/progress_courses/" + id })
        console.log(res);
        if (res.id) {

            setCourse({
                name: res.name,
                image: res.image,
                description: res.pref_description
            })


            // get the content in a different format for reordering
            const tempContent = []
            res.units.forEach(unit => {

                tempContent.push({
                    type: "unit",
                    title: unit.title,
                    id: "unit" + unit.id,
                })

                unit.temp_contents.forEach(lesson => {
                    let content;
                    if (lesson.is_pdf)
                        content = 'pdf'
                    else if (lesson.is_video)
                        content = "video"
                    else
                        content = 'quiz'
                    console.log(content);
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

    async function approve(){
        
    }
    async function disapprove(){

    }
    return (
        <>
            <div className='flex justify-between '>
                <div className='flex w-full'>
                    <div className='group relative mr-4 rounded w-2/6'>
                        <img className='w-full' src={course.image ? course.image : def} />

                    </div>
                    <div className='flex-grow'>
                        <h1 className='text-xl font-bold'>{course.name}</h1>
                        <p className='mt-4 text-md font-light'>{course.description} </p>
                    </div>
                </div>

            </div>
            
            <div >

                <div >
                    {
                        content.map((item) => {
                            if (item.type == 'unit')
                                return <Unit isDisplayOnly={true} key={item.id}item={item} />
                            else
                                return <Lesson isDisplayOnly={true} key={item.id} item={item} />
                        })}
                </div>
            </div>
            <div className='flex justify-end mt-10'>
                <button onClick={disapprove} className='p-2  rounded hover:cursor-pointer text-xl mr-6'>Disapprove</button>
                <button onClick={approve} className='p-2 bg-accent rounded hover:cursor-pointer text-xl'>Approve</button>
            </div>
        </>
    )
}

export default PendingCourseDetails
