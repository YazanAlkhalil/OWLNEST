import React from 'react';
import { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

export default function PdfViewer ({pdfUrl}) {
    const containerRef = useRef(null);
    const navigate = useNavigate();

    useEffect(() => {
        const container = containerRef.current;
        let PSPDFKIT;
    
        const loadPdf = async () => {
          try {
            PSPDFKIT = await import('pspdfkit');
            await PSPDFKIT.load({
              container,
              document: pdfUrl,
              baseUrl: `${window.location.protocol}//${window.location.host}/${process.env.PUBLIC_URL}`,
            });
          } catch (error) {
            console.error("Error loading PSPDFKit", error);
          }
        };
    
        const unloadPdf = () => {
          if (PSPDFKIT && PSPDFKIT.unload) {
            PSPDFKIT.unload(container);
          }
        };
    
        unloadPdf();
        loadPdf();
    
        return () => {
          unloadPdf();
        };
      }, [pdfUrl]);
  
    return (
      <div className="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center z-50">
          <button
            onClick={()=> navigate('/trainee/courses/:id/content')}
            className="absolute top-2 right-2 px-8 py-2 font-semibold bg-primary text-white rounded-full p-2 hover:bg-secondary"
          >
            Go to next item
          </button>
        <div className="bg-white p-4 rounded-lg relative w-4/5 h-4/5">
          <div ref={containerRef} className="w-full h-full"></div>
        </div>
      </div>
    );
}
