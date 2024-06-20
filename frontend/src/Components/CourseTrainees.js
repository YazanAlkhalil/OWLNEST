import React from 'react'
import BasicTable from './Table'
import image from '../images/user-profile-icon-flat-style-member-avatar-vector-illustration-isolated-background-human-permission-sign-business-concept_157943-15752.avif'
function CourseTrainees() {
  return (
    <div className='text-2xl'>
      <BasicTable heading={['Name','Progress','XP','Grades','Completed']} 
      data={[
        {
          progress: '100%',
          xp:"234",
          grades:"75%",
          completed: "2024/2/2",
          name:"يعقوب قمر الدين ديبيازة",

        },
        {
          progress: '50%',
          xp:"234",
          grades:"75%",
          completed: null,
          name:"خالد كشميري",

        },
        {
          progress: '50%',
          xp:"234",
          grades:"75%",
          completed: null,
          name:"خضر كرويتا"

        },
        {
          progress: '100%',
          xp:"234",
          grades:"75%",
          completed: "2024/2/2",
          name:"اسماعيل احمد كنباوي"

        },
        {
          progress: '100%',
          xp:"234",
          grades:"75%",
          completed: "2024/2/2",
          name:"عثمان عبد الجليل ششة"

        },
        {
          progress: '100%',
          xp:"234",
          grades:"75%",
          completed: "2024/2/2",
          name:"محمد سنبل"
        },
      ]}
      />
    </div>
  )
}

export default CourseTrainees
