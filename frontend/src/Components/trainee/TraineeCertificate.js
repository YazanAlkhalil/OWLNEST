import React, { useEffect, useState } from "react";
import certificate from './../../images/certificate-text-samples.jpg';
import useFetch from "../AuthComponents/UseFetch";

export default function TraineeCertificate() {
  const { fetchData, resData } = useFetch();
  const [certifecates, setCertifecations] = useState([]);
  const companyID = localStorage.getItem('companyId');

  useEffect(() => {
    const getCertifecations = async () => {
      const res = await fetchData({ url: 'http://127.0.0.1:8000/api/company/' + companyID + '/certifications', method: 'get' })
      console.log(res);
      setCertifecations(res);
    }
    getCertifecations();
  }, [])

  return (
    <>
      <div className="flex flex-wrap gap-4">
        {certifecates.map((cer) => {
          return (
            <div key={cer.id} className="bg-white dark:bg-DarkSecondary shadow-md rounded p-4">
              <img
                src={`http://127.0.0.1:8000/api/${cer.certificate}`}
                alt={cer.title}
                className="w-[270px] h-40 object-cover rounded-t"
              />
            </div>
          );
        })}
      </div>
    </>
  );
}
