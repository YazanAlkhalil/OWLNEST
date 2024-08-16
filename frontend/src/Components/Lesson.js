import { useSortable } from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { FaPlay } from "react-icons/fa";
import { FaRegFilePdf } from "react-icons/fa6";
import { MdDelete } from "react-icons/md";
import { PiExam } from "react-icons/pi";
import useFetch from "./AuthComponents/UseFetch";
import { useNavigate, useParams } from "react-router-dom";

function getIcon(icon) {
  if (icon == 'video')
    return <FaPlay />
  else if (icon == 'pdf')
    return <FaRegFilePdf />
  else
    return <PiExam />
}

function Lesson({ item, sortable, isDisplayOnly, getInfo }) {
  const navigate = useNavigate()
  const { id } = useParams()
  const { attributes, listeners, setNodeRef, transform, transition } = useSortable({ id: item.id });
  const style = {
    transition,
    transform: CSS.Transform.toString(transform)
  }
  const { fetchData } = useFetch()
  async function handleDelete() {
    const res = await fetchData({ url: "/content/" + item.id.slice(6), method: "DELETE" })
    getInfo()
  }

  async function handleClick(){
    localStorage.setItem("lessonId", item.id)
    if (item.content == 'video')
      navigate("/trainer/courses/" + id + "/video")
    else if (item.content == 'pdf')
      navigate("/trainer/courses/" + id + "/pdf")
    else
      navigate("/trainer/courses/" + id + "/quiz")
  }
  if (!sortable) {
    return <div onClick={handleClick}
      className={`${isDisplayOnly ? "" : "group"} dark:bg-DarkSecondary dark:hover:bg-DarkGrayHover dark:text-white bg-gray-50 hover:cursor-pointer hover:bg-gray-200 text-black border flex justify-between items-center mb-2 p-2 rounded`}>
      <div className="flex items-center">
        {getIcon(item.content)}
        <h4 className='ml-2 text-xl'>{item.title}</h4>
      </div>
      <MdDelete onClick={handleDelete} className='ml-2 hover:cursor-pointer box-content p-2  size-6 text-transparent  group-hover:text-red-500  rounded-full ' />
    </div>
  }
  return <div style={style} ref={setNodeRef} {...attributes} {...listeners}
    className='dark:bg-DarkSecondary dark:hover:bg-DarkGrayHover dark:text-white bg-gray-50 hover:cursor-pointer hover:bg-gray-200 text-black border flex items-center mb-2 p-2 rounded'>
    <div className="flex items-center">
      {getIcon(item.content)}
      <h4 className='ml-2 text-xl'>{item.title}</h4>
    </div>
    <MdDelete className='ml-2 hover:cursor-pointer box-content p-2  size-6 text-transparent  rounded-full ' />

  </div>
}
export default Lesson;