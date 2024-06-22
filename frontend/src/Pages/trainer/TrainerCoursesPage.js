import TrainerCourse from "../../Components/TrainerCourse"
import image from '../../images/multimedia-courses-scope-and-career 1.png'
import image2 from '../../images/BA-Courses 1.png'
import image3 from '../../images/c_7_free_google_courses_become_machine_learning_engineer_1 1.png'
import image4 from '../../images/course__cs101_courses_datastructuresfromctopython__course-promo-image-1653540139 1.png'

function TrainerCoursesPage() {
  return (
    <div className="grid grid-cols-3 gap-y-12 ">
      <TrainerCourse image={image} name={'Multimedia'}/>
      <TrainerCourse image={image2} name={'Soft skills'}/>
      <TrainerCourse image={image3} name={'ML Google'}/>
      <TrainerCourse image={image4} name={'CS101'}/>
    </div>
    
  )
}

export default TrainerCoursesPage
