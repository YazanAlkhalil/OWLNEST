import { useState, useRef, useEffect } from 'react';
import { Document, Page } from 'react-pdf';
import { FaMinus, FaPlus } from "react-icons/fa";
import { BiArrowBack } from 'react-icons/bi';
import { useNavigate, useParams } from 'react-router-dom';


function PdfViewer({ filename }) {
  const [numPages, setNumPages] = useState();
  const [pageNumber, setPageNumber] = useState(1);
  const [scale, setScale] = useState(1);
  const containerRef = useRef(null);
  const navigate = useNavigate()
  const {id}= useParams()


  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
  }

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

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

  return (
    <div className="relative flex flex-col items-center min-h-screen bg-gray-100">
      <div className="sticky top-[-2rem] z-10 w-full bg-white shadow-md p-4 flex justify-between items-center">
        <div className='flex gap-3 items-center'>
        <BiArrowBack className='size-7 hover:cursor-pointer' onClick={()=> navigate(`/trainee/courses/${id}/content`)}/>
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
          file={'http://localhost:5000/uploads/' + filename}
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
  );
}

export default PdfViewer;