import React from 'react'
import image from '../../images/multimedia-courses-scope-and-career 1.png'
import image2 from '../../images/BA-Courses 1.png'
import TraineeCourse from '../TraineeCourse'

export default function TraineeCourses() {
  return (
    <>
      <div className='grid grid-cols-3 gap-y-12 '>
      <TraineeCourse image={image} name={'Multimedia'} />
      <TraineeCourse image={image2} name={'Soft skills'} />
      <TraineeCourse image={image2} name={'Soft skills'} />
      <TraineeCourse image={image2} name={'Soft skills'} />
      <TraineeCourse image={image2} name={'Soft skills'} />
      <TraineeCourse image={image2} name={'Soft skills'} />
      </div>
    </>
  )
}
