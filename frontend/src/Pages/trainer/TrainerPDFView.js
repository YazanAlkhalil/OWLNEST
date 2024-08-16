import React from 'react'
import { pdfjs } from 'react-pdf';
import { useState, useRef, useEffect } from 'react';
import { Document, Page } from 'react-pdf';
import { FaMinus, FaPlus } from "react-icons/fa";
import { BiArrowBack } from 'react-icons/bi';
import { useLocation, useNavigate, useParams } from 'react-router-dom';
import useFetch from '../../Components/AuthComponents/UseFetch';

pdfjs.GlobalWorkerOptions.workerSrc = new URL(
  'pdfjs-dist/build/pdf.worker.min.mjs',
  import.meta.url,
).toString();

function TrainerPDFView({trainee}) {
  const [numPages, setNumPages] = useState();
  const [url,setUrl]= useState("")
  const {fetchData} = useFetch()
  const lessonId = localStorage.getItem("lessonId")
  const location = useLocation();
  const [pageNumber, setPageNumber] = useState(1);
  const [scale, setScale] = useState(1);
  const containerRef = useRef(null);
  const navigate = useNavigate()
  const { id } = useParams()

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
  }

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;
    const getUrl = async ()=>{
      let res
      if(trainee){
        res= await fetchData({
          url: "/trainee/content/"+ lessonId
        })
      }
      else{

        res= await fetchData({
          url: "/content/"+ lessonId
        })
      }
      setUrl(res.file)
      console.log(res);
    }
    getUrl()
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setPageNumber(parseInt(entry.target.dataset.pageNumber));
          }
          else {
            setPageNumber(1)
          }
        });
      },
      { threshold: 0.5 }
    );

    const pages = container.querySelectorAll('.pdf-page');
    pages.forEach((page) => observer.observe(page));

    return () =>
      observer.disconnect()
      ;
  }, [numPages]);

  const zoomIn = () => setScale(prevScale => Math.min(prevScale + 0.1, 1.4));
  const zoomOut = () => setScale(prevScale => Math.max(prevScale - 0.1, 0.6));
  const goToCourseBasePath = () => {
    const currentPath = location.pathname;
    const basePath = currentPath.replace(/\/pdf$/, ''); // Removes '/pdf' at the end of the path
    navigate(basePath);
};

  return (
    <div className="relative flex flex-col items-center min-h-screen ">
      <div className="sticky top-[-2rem] z-10 w-full shadow-md p-4 flex justify-between items-center">
        <div className='flex gap-3 items-center'>
          <BiArrowBack className='size-7 hover:cursor-pointer' onClick={goToCourseBasePath} />
          <button
            onClick={zoomIn}
            className="bg-secondary hover:bg-[#3f6188d0] text-white font-bold py-2 px-4 rounded"
          >
            <FaPlus />
          </button>
          <button
            onClick={zoomOut}
            className="bg-secondary hover:bg-[#3f6188d0] text-white font-bold py-2 px-4 rounded"
          >
            <FaMinus />
          </button>
        </div>
        <p className="text-center text-lg font-semibold">
          Page {pageNumber} of {numPages}
        </p>
      </div>
      <div
        ref={containerRef}
        className="container mx-auto px-4 py-8 max-w-4xl"
      >
        <Document
          file={url}
          onLoadSuccess={onDocumentLoadSuccess}
          className="flex flex-col items-center"
        >
          {Array.from(new Array(numPages), (el, index) => (
            <div
              key={`page_${index + 1}`}
              className="pdf-page mb-8 shadow-lg"
              data-page-number={index + 1}
            >
              <Page
                pageNumber={index + 1}
                renderTextLayer={false}
                renderAnnotationLayer={false}
                className="border border-gray-300 rounded"
                width={Math.min(600 * scale, window.innerWidth - 32)}
                scale={scale}
              />
            </div>
          ))}
        </Document>
      </div>
    </div>
  )
}

export default TrainerPDFView
