import { useSortable } from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { useEffect, useRef, useState } from "react";
import { FaPlay } from "react-icons/fa";
import { FaRegFilePdf } from "react-icons/fa6";
import { PiExam } from "react-icons/pi";
function Unit({ item,sortable,uploadVideo,uploadPDF,createQuiz }) {
  const [isOverlayVisible, setOverlayVisible] = useState(false);
  const overlayRef = useRef(null);

  const toggleOverlay = () => {
    setOverlayVisible(!isOverlayVisible);
  };
  const handleClickOutside = (event) => {
    if (overlayRef.current && !overlayRef.current.contains(event.target)) {
      setOverlayVisible(false);
    }
  };
  useEffect(() => {
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);
  const { attributes, listeners, setNodeRef, transform, transition } =
    useSortable({ id: item.id  });
  const style = {
    transition,
    transform: CSS.Transform.toString(transform),
  };
  if(!sortable){
    return (
      <div
      className="relative bg-gray-300 mb-2 py-2 px-4 rounded flex justify-between items-center"
    >
      <span className="text-xl">{item.name} </span>
      <button
        onClick={toggleOverlay}
        className="hover:bg-slate-100 bg-white rounded p-2 text-black"
      >
        add lesson
      </button>
      <div
        ref={overlayRef}
        className={`${isOverlayVisible ? "block" : "hidden"} z-10 bg-slate-200  absolute top-12 right-12`}
      >
        <div onClick={uploadVideo} className="flex items-center gap-2 hover:bg-slate-300 hover:cursor-pointer py-2 px-3">
          <FaPlay />
          Video
        </div>
        <div onClick={uploadPDF} className="flex items-center gap-2 hover:bg-slate-300 hover:cursor-pointer py-2 px-3">
          <FaRegFilePdf />
          PDF
        </div>
        <div onClick={createQuiz} className="flex items-center gap-2 hover:bg-slate-300 hover:cursor-pointer py-2 px-3">
          <PiExam />
          Quiz
        </div>
      </div>
    </div>
    )
  }




  return (
    <div
      style={style}
      ref={setNodeRef}
      {...attributes}
      {...listeners}
      className="relative h-14 bg-gray-300 mb-2 py-2 px-4 rounded flex justify-between items-center"
    >
      <span className="text-xl">{item.name} </span>
      
      
    </div>
  );
}

export default Unit;
