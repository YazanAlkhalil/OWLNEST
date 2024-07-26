import React, { useEffect, useState } from 'react'
import { FaReply } from "react-icons/fa6";
import { BiLike } from "react-icons/bi";
import { BiDislike } from "react-icons/bi";
import { useParams } from 'react-router-dom';
import useFetch from './AuthComponents/UseFetch';
import { BiSolidDislike } from "react-icons/bi";
import { BiSolidLike } from "react-icons/bi";

export default function Reply({data}) {
  const [replyData, setReplyData] = useState(data);
  const { fetchData } = useFetch();
  const { id } = useParams();

  useEffect(() => {
    setReplyData(data);
  }, [data]);

  const handleReactionClick = async (reaction) => {
    const newReaction = replyData.reaction === reaction ? 0 : reaction;
    const dataToSend = {
      reply: replyData.id,
      reaction: newReaction,
    };
    console.log(dataToSend);
    const res = await fetchData({
      url: `http://127.0.0.1:8000/api/course/${id}/comments/reply/react`,
      method: "post",
      data: dataToSend,
    });
    if (res) {
      setReplyData((prevData) => ({
        ...prevData,
        reaction: newReaction,
        likes:
          newReaction === 1
            ? prevData.likes + 1
            : prevData.reaction === 1
            ? prevData.likes - 1
            : prevData.likes,
        dislikes:
          newReaction === -1
            ? prevData.dislikes + 1
            : prevData.reaction === -1
            ? prevData.dislikes - 1
            : prevData.dislikes,
      }));
    }
  };

  return (
    <div>
     <div className='flex justify-between w-3/4 mx-auto px-6 py-5 '>
        <div className='flex'>
            <img src={`http://127.0.0.1:8000/api${replyData?.image}`} alt='error' className='w-[90px] h-[90px] ' />
            <div className='ml-3 my-4'>
              <h4 className='text-xl font-black'>{replyData?.username} </h4>
              <p className='text-xl font-semibold'>{replyData?.content} </p>
            </div>
        </div>
        <div>
            <div className='flex p-4'>
            <div
              onClick={() => handleReactionClick(1)}
              className={`${
                replyData?.reaction === 1 ? "bg-slate-200" : ""
              } border-r-2 flex border-r-stone-950 px-10 py-1 cursor-pointer`}>
              {replyData?.reaction === 1 ? <BiSolidLike style={{color: "#3F6188"}} size={"30"} /> : <BiLike size={"30"} />}
              <p className="ml-2 text-xl font-semibold">{replyData?.likes}</p>
            </div>
            <div
              onClick={() => handleReactionClick(-1)}
              className={`${
                replyData?.reaction === -1 ? "bg-slate-200" : ""
              } px-10 py-1 flex cursor-pointer`}>
              {replyData?.reaction === -1 ? <BiSolidDislike style={{color: "blue"}} size={"30"} /> : <BiDislike size={"30"} />}
              <p className="ml-2 text-xl font-semibold">
                {replyData?.dislikes}
              </p>
            </div>
            </div>
        </div>
      </div>
    </div>
  )
}
