import React, { useState, useEffect } from "react";
import { FaReply } from "react-icons/fa6";
import { BiLike } from "react-icons/bi";
import { BiDislike } from "react-icons/bi";
import AddReply from "./AddReply";
import Reply from "./Reply";
import useFetch from "./AuthComponents/UseFetch";
import { useParams } from "react-router-dom";
import { BiSolidDislike } from "react-icons/bi";
import { BiSolidLike } from "react-icons/bi";
import toast from "react-hot-toast";
 
 

export default function Comment({ data }) {
  const [commentData, setCommentData] = useState(data);
  const [value, setValue] = useState(false);
  const { fetchData } = useFetch();
  const { id } = useParams();

  useEffect(() => {
    setCommentData(data);
  }, [data]);

  const handleClickRepliesButton = () => {
    setValue(!value);
    if (commentData?.replies.length === 0) {
      toast.error("No replies to display");
    }
  };

  const addNewReply = (reply) => {
    setCommentData((prevData) => ({
      ...prevData,
      replies: [reply,...prevData.replies ],
    }));
  }

  const handleReactionClick = async (reaction) => {
    const newReaction = commentData.reaction === reaction ? 0 : reaction;
    const dataToSend = {
      comment: commentData.id,
      reaction: newReaction,
    };
    const res = await fetchData({
      url: `http://127.0.0.1:8000/api/course/${id}/comments/react`,
      method: "post",
      data: dataToSend,
    });
    if (res) {
      setCommentData((prevData) => ({
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
    <div className="border border-b-stone-950 border-4 mb-6">
      <div className="flex justify-between px-6 py-5">
        <div className="flex">
          <img
            src={`http://127.0.0.1:8000/api${commentData?.image}`}
            alt="error"
            className="w-[90px] h-[90px]"
          />
          <div className="ml-3">
            <h4 className="text-xl font-black">{commentData?.username}</h4>
            <p className="text-xl font-semibold">{commentData?.content}</p>
            <div
              className="flex w-[120px] mt-2 cursor-pointer text-white px-2 py-2 bg-gray-400"
              onClick={handleClickRepliesButton}>
              <p className="text-md font-bold mx-2">Replies</p>
              <FaReply className="mt-1" />
            </div>
          </div>
        </div>
        <div>
          <div className="flex">
            <div
              onClick={() => handleReactionClick(1)}
              className={`${
                commentData?.reaction === 1 ? "bg-slate-200" : ""
              } border-r-2 flex border-r-stone-950 px-10 py-1 cursor-pointer`}>
              {commentData?.reaction === 1 ? <BiSolidLike style={{color: "#3F6188"}} size={"30"} /> : <BiLike size={"30"} />}
              <p className="ml-2 text-xl font-semibold">{commentData?.likes}</p>
            </div>
            <div
              onClick={() => handleReactionClick(-1)}
              className={`${
                commentData?.reaction === -1 ? "bg-slate-200" : ""
              } px-10 py-1 flex cursor-pointer`}>
              {commentData?.reaction === -1 ? <BiSolidDislike style={{color: "#3F6188"}} size={"30"} /> : <BiDislike size={"30"} />}
              <p className="ml-2 text-xl font-semibold">
                {commentData?.dislikes}
              </p>
            </div>
          </div>
          <div className="text-center mt-3">
            <AddReply commentId={commentData?.id} addNewReply={addNewReply}/>
          </div>
        </div>
      </div>
      {value && (
        <div>
          {commentData?.replies.map((rep) => {
            return <Reply key={rep.id} data={rep} />;
          })}
        </div>
      )}
    </div>
  );
}
