import React from "react";
import certificate from './../../images/certificate-text-samples.jpg';

const certificateArray = [
  {
    id: 1,
    title: "HTML/CSS",
    image: certificate,
    description: "HTML/CSS certification from W3C",
    date: "2020-01-01",
  },
  {
    id: 2,
    title: "JavaScript",
    image: certificate,
    description: "JavaScript certification from W3C",
    date: "2020-02-01",
  },
  {
    id: 3,
    title: "React",
    image: certificate,
    description: "React certification from Pluralsight",
    date: "2020-03-01",
  },
  {
    id: 4,
    title: "Angular",
    image: certificate,
    description: "Angular certification from Pluralsight",
    date: "2020-04-01",
  },
  {
    id: 5,
    title: "Vue",
    image: certificate,
    description: "Vue certification from Pluralsight",
    date: "2020-05-01",
  },
];

export default function TraineeCertificate() {
  return (
    <>
      <div className="flex flex-wrap gap-4">
        {certificateArray.map((cer)=>{
          return(
            <div key={cer.id} className="bg-white shadow-md rounded p-4">
              <img src={cer.image} alt={cer.title} className="w-[270px] h-40 object-cover rounded-t"/>
              <h5 className="text-lg font-semibold m-2">{cer.title}</h5>
              <p className="text-sm font-semibold m-2">{cer.description}</p>
              <p className="text-sm m-2">{cer.date}</p> 

            </div>
          );
        })}
      </div>
    </>
  );
}
