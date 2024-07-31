import React, { useState } from 'react'
import NavButton from '../../Components/NavButton'
import AdminCourseUsers from '../../Components/AdminCourseUsers'
import CourseReports from '../../Components/CourseReports'

function AdminCourseDetails(props) {
    const name = localStorage.getItem('courseName')
    const [content, setContent] = useState(props.content ? props.content : 'reports')
    return (
        <>
            <div className='flex items-center justify-between mb-6'>
                <p className='text-3xl'>{name}</p>
                <div className='flex gap-3'>
                    <NavButton name={'Reports'} highlight={content == 'reports'} handleClick={() => setContent('reports')} />
                    <NavButton name={"Users"} highlight={content == 'users'} handleClick={() => setContent('users')} />
                </div>
            </div>
            <div>
                {content == 'users' && <AdminCourseUsers />}
                {content == 'reports' && <CourseReports admin={false} />}
            </div>
        </>

    )
}

export default AdminCourseDetails
