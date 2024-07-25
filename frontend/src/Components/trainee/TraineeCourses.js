import React from 'react'
import image from '../../images/multimedia-courses-scope-and-career 1.png'
import image2 from '../../images/BA-Courses 1.png'
import TraineeCourse from '../TraineeCourse'

export default function TraineeCourses() {
  return (
    <>
      <div className='flex flex-wrap gap-3 '>
      <TraineeCourse id={1} image={image} name={'Multimedia'} />
      <TraineeCourse id={'2'} image={image2} name={'Soft skills'} />
      <TraineeCourse id={'3'} image={image2} name={'Soft skills'} />
      <TraineeCourse id={'4'} image={image2} name={'Soft skills'} />
      <TraineeCourse id={'5'} image={image2} name={'Soft skills'} />
      <TraineeCourse id={'6'} image={image2} name={'Soft skills'} />
      </div>
    </>
  )
}
