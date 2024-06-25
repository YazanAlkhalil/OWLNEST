import React from 'react'
import AddComment from '../AddComment'
import Comment from '../Comment'

export default function TraineeDiscussion() {
  return (
    <>
        <div className='flex justify-end px-10 py-5'>
            <AddComment />
        </div>
        <div>
            <Comment />
        </div>

    </>
  )
}
