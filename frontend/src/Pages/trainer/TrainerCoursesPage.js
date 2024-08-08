import TrainerCourse from "../../Components/TrainerCourse"
import image from '../../images/multimedia-courses-scope-and-career 1.png'
import image2 from '../../images/BA-Courses 1.png'
import image3 from '../../images/c_7_free_google_courses_become_machine_learning_engineer_1 1.png'
import image4 from '../../images/course__cs101_courses_datastructuresfromctopython__course-promo-image-1653540139 1.png'
import useFetch from "../../Components/AuthComponents/UseFetch"
import { useEffect, useState } from "react"
import NoCourses from "../../Components/NoCourses"

function TrainerCoursesPage({ inprogress }) {
  const [courses, setCourses] = useState([])
  const companyId = localStorage.getItem('companyId')
  const { fetchData } = useFetch()

  useEffect(() => {
    const getInprogressCourses = async () => {
      const res = await fetchData({ url: "http://127.0.0.1:8000/api/trainer/company/" + companyId + "/progress_courses" })
      if (Array.isArray(res)) {
        setCourses(res)
      }
    }
    if (inprogress)
      getInprogressCourses()
    else
      setCourses([])
  }, [inprogress])

  return (
    <>
      {
        courses.length > 0 ?

          (<div className="grid grid-cols-3 gap-y-12 ">
            {
              courses.map(course => (
                <TrainerCourse inprogress={inprogress} id={course.id} key={course.id} image={course.image} name={course.name} />
              ))
            }
          </div>)
          :
          <NoCourses/>
      }
    </>
  )
}

export default TrainerCoursesPage
