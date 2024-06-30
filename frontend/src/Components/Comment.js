import React, { useState } from "react";
import logo from "./../images/user-profile-icon-flat-style-member-avatar-vector-illustration-isolated-background-human-permission-sign-business-concept_157943-15752.avif";
import { FaReply } from "react-icons/fa6";
import { BiLike } from "react-icons/bi";
import { BiDislike } from "react-icons/bi";
import AddReply from "./AddReply";
import Reply from "./Reply";

const replies = [
  {
    id: 1,
    name: "John Doe",
    reply:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut",
  },
  {
    id: 2,
    name: "John Doe",
    reply:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut",
  },
  {
    id: 3,
    name: "John Doe",
    reply:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut",
  },
];

export default function Comment({ name, text }) {
  const [value,setValue] = useState(false);
  const handleClickRepliesButton = () => {
    setValue(!value);
  };
  return (
    <>
      <div className="border border-b-stone-950 border-4 mb-6">
        <div className="flex justify-between px-6 py-5 ">
          <div className="flex">
            <img src={logo} alt="error" className="w-[90px] h-[90px] " />
            <div className="ml-3">
              <h4 className="text-xl font-black">{name}</h4>
              <p className="text-xl font-semibold">{text}</p>
              <div
                className="flex w-[120px] mt-2 cursor-pointer text-white px-2 py-2 bg-gray-400"
                onClick={handleClickRepliesButton}>
                <p className="text-md font-bold mx-2">Replies</p>
                <FaReply className=" mt-1" />
              </div>
            </div>
          </div>
          <div>
            <div className="flex ">
              <div className="border-r-2 flex border-r-stone-950 px-10 py-1 cursor-pointer">
                <BiLike size={"30"} />
                <p className="ml-2 text-xl font-semibold">4</p>
              </div>
              <div className="px-10 py-1 flex cursor-pointer">
                <BiDislike size={"30"} />
                <p className="ml-2 text-xl font-semibold">1</p>
              </div>
            </div>
            <div className="text-center mt-3">
              <AddReply />
            </div>
          </div>
        </div>
          {value && <div>
            {replies.map((rep)=>{
            return <Reply key={rep.id} name={rep.name} text={rep.reply} />
          })}
          </div>
          }
          
      </div>
    </>
  );
}
