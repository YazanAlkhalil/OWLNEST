import { useSortable } from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { useEffect, useRef, useState } from "react";
import { FaPlay } from "react-icons/fa";
import { FaRegFilePdf } from "react-icons/fa6";
import { MdDelete } from "react-icons/md";
import { PiExam } from "react-icons/pi";
import useFetch from "./AuthComponents/UseFetch";
function Unit({ item, sortable, uploadVideo, uploadPDF, createQuiz,isDisplayOnly }) {
  const [isOverlayVisible, setOverlayVisible] = useState(false);
  const {fetchData} = useFetch()
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
    useSortable({ id: item.id });
  const style = {
    transition,
    transform: CSS.Transform.toString(transform),
  };

  const deleteUnit = async () => {
    const res = await fetchData({url:""})
  }


  if (!sortable) {
    return (
      <div className="relative mb-2 py-2 px-2 h-12 pl-1 rounded flex justify-between items-center">
        <div>

          <span className="text-2xl">{item.title} </span>
        </div>
        {!isDisplayOnly && <div className="flex items-center">
          <button
            onClick={toggleOverlay}
            className="btn-inner h-18 p-2 "
          >
            add lesson
          </button>
          <MdDelete onClick={deleteUnit} className='ml-2 hover:cursor-pointer box-content p-2  size-6 text-red-500 rounded-full  ' />
        </div>}
        {!isDisplayOnly && <div
          ref={overlayRef}
          className={`${isOverlayVisible ? "block" : "hidden"
            } rounded z-10 bg-white dark:bg-DarkGray shadow-xl border border-slate-50  absolute top-12 right-28`}
        >
          <div
            onClick={() => {
              localStorage.setItem('unitId', item.id)
              uploadVideo()
            }
            }
            className="flex items-center gap-3 hover:bg-slate-200 dark:hover:bg-Gray hover:cursor-pointer text-xl py-3 px-5"
          >
            <FaPlay />
            Video
          </div>
          <div
            onClick={() => {
              localStorage.setItem('unitId', item.id)
              uploadPDF()
            }
            }
            className="flex items-center gap-3 hover:bg-slate-200 dark:hover:bg-Gray hover:cursor-pointer text-xl py-3 px-5"
          >
            <FaRegFilePdf />
            PDF
          </div>
          <div
            onClick={() => {
              localStorage.setItem('unitId', item.id)
              createQuiz()
            }
            }
            className="flex items-center gap-3 hover:bg-slate-200 dark:hover:bg-Gray hover:cursor-pointer text-xl py-3 px-5"
          >
            <PiExam />
            Quiz
          </div>
        </div>}
      </div>
    );
  }



  return (
    <div
      style={style}
      ref={setNodeRef}
      {...attributes}
      {...listeners}
      className="relative mb-2 py-2 px-2 h-12 pl-1 rounded flex justify-between items-center"
    >
      <span className="text-2xl">{item.title} </span>
    </div>
  );
}

export default Unit;
