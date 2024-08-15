import React, { useEffect, useState } from 'react'
import ChartExample from './Chart'
import Card from './Card'
import { useSelector } from 'react-redux';
import useFetch from './AuthComponents/UseFetch';
import { useParams } from 'react-router-dom';

function CourseReports({ admin }) {
  const isDarkMode = useSelector((state) => state.theme.isDarkMode);
  const [cardsData, setCardsData] = useState({
    avg_grade: "",
    number_of_trainees_in_progress: "",
    trainees_complete: "",
    trainers_number: ""
  })
  const [xp, setXP] = useState([])
  const [name, setName] = useState("")
  const { fetchData } = useFetch()
  const { id } = useParams()
  useEffect(() => {
    async function getInfo() {
      const res = await fetchData({ url: "/course/" + id + "/report" })
      setName(res.admin_username)
      setXP(res.graph)
      setCardsData({
        avg_grade: res.avg_grade,
        number_of_trainees_in_progress: res.number_of_trainees_in_progress,
        trainees_complete: res.trainees_complete,
        trainers_number: res.trainers_number
      })
      console.log(res);
    }
    getInfo()
  }, [])

  return (
    <div className='flex flex-col'>

      {admin && <h1 className='text-xl '>Admin : {name}</h1>}
      <div className='flex justify-between'>
        <Card title={'learner in progress'} value={cardsData.number_of_trainees_in_progress} />
        <Card title={'completed learners'} value={cardsData.trainees_complete} />
        <Card title={'Average grades'} value={cardsData.avg_grade} />
        <Card title={'Instructors'} value={cardsData.trainers_number} />

      </div>
      <div className='mt-auto'>

        <ChartExample options={{
          height: 380,
          title: {
            text: "XP gains for trainees",
          },
          theme: !isDarkMode ? 'ag-default-dark' : 'ag-default',

          data: xp,
          series: [
            {
              type: "area",
              xKey: "month",
              yKey: "xp",
              yName: "xp",
            },

          ],
        }} />
      </div>
    </div>
  )
}

export default CourseReports
