import { useSortable } from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { FaPlay } from "react-icons/fa";
import { FaRegFilePdf } from "react-icons/fa6";
import { PiExam } from "react-icons/pi";

function getIcon(icon) {
    if (icon == 'video')
      return <FaPlay />
    else if (icon == 'pdf')
      return <FaRegFilePdf />
    else
      return <PiExam />
  }
  
function Lesson({item,sortable}) {
    const {attributes,listeners,setNodeRef,transform,transition}=useSortable({id:item.id });
    const style = {
      transition,
      transform: CSS.Transform.toString(transform)
    }
    if(!sortable){
      return <div 
      className='bg-white text-black border flex items-center mb-2 p-2 rounded'>
      {getIcon(item.content)}
      <h4 className='ml-2'>{item.name}</h4>
    </div>
    }
    return <div style={style} ref={setNodeRef} {...attributes} {...listeners}
      className='bg-white text-black border flex items-center mb-2 p-2 rounded'>
      {getIcon(item.content)}
      <h4 className='ml-2'>{item.name}</h4>
    </div>
  }
  export default Lesson;