import React, { useEffect } from 'react'
import PdfViewer from '../PdfViewer '
import { useLocation } from 'react-router-dom';
import useFetch from '../AuthComponents/UseFetch';

export default function TraineePdf() {
  const { state } = useLocation();
  const { fetchData ,resData } = useFetch();
  useEffect(()=>{
    const getPdf = async () => {
      const res = await fetchData({
        url:
          "http://127.0.0.1:8000/api/trainee/content/"+state,
        method: "get",
      });
      console.log(res);
      
    }
    getPdf()
  },[])
  return (
    <div>
      <PdfViewer pdfUrl={resData?.file} />
    </div>
  )
}
