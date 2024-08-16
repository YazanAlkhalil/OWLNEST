import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import React, { useEffect, useState } from 'react'
import { useNavigate,useParams } from 'react-router-dom';
import useFetch from '../../Components/AuthComponents/UseFetch'
function TrainerVideoView() {
    const navigate = useNavigate();
    const {fetchData} = useFetch()
    const [loading,setLoading] = useState(true)
    const lessonId = localStorage.getItem("lessonId").slice(6)
    const [videoDetails,setVideoDetails] = useState({
        title:"",
        url:"",
        description:""
    })
    const {id} = useParams()
    const onGoBackClick = () => {
        navigate("/trainer/courses/"+id);
    };

    useEffect(() => {
        const socket = new WebSocket("ws://127.0.0.1:8000/ws/course/1/content/1");
        const getVideoDetails = async ()=>{

            const res = await fetchData({url:"/content/"+lessonId})
            console.log(res);
            setVideoDetails({
                title:res.title,
                url:res.file,
                description:res.description
            })
            setLoading(false)
        }
        getVideoDetails()
        socket.onclose = function (e) {
            console.error("WebSocket closed unexpectedly");
        };

        return () => {
            socket.close();
        };
    }, []);

    return (
        <div>
            <FontAwesomeIcon
                className="cursor-pointer text-2xl"
                icon={faArrowLeft}
                onClick={onGoBackClick}
            />
            <h1 className='mx-auto text-xl'>{videoDetails.title}</h1>
            <div className="mt-10">
                {!loading && <video className="h-[70%] mx-auto w-[70%] rounded-lg" controls>
                    <source
                        src={videoDetails.url}
                        type="video/mp4"
                    />
                    Your browser does not support the video tag.
                </video>}
            </div>
            <div className="w-[70%] mt-10 mx-auto">
                <h1 className="text-2xl font-semibold">Description : </h1>
                <p className="text-md px-5 py-10">
                    {videoDetails.description}
                </p>
            </div>
        </div>
    )
}

export default TrainerVideoView
