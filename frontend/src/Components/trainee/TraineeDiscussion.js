import React from 'react'
import AddComment from '../AddComment'
import Comment from '../Comment'

const commets = [
  {
  id: 1,
  name: 'John',
  text: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque, quod',
  },
  {
    id: 2,
    name: 'Jane',
    text: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque, quod'
  },
  {
    id: 3,
    name: 'John',
    text: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloremque, quod'
    }
]

export default function TraineeDiscussion() {
  return (
    <>
        <div className='flex justify-end py-5'>
            <AddComment />
        </div>
        <div>
           {commets.map((com)=>{
            return <Comment key={com.id} name={com.name} text={com.text} />
           })}
        </div>

    </>
  )
}
