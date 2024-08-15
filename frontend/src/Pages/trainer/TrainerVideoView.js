import { faArrowLeft } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom';

function TrainerVideoView() {
    const navigate = useNavigate();
    const onGoBackClick = () => {
        navigate("/trainee/courses/:id/content");
    };

    useEffect(() => {
        const socket = new WebSocket("ws://127.0.0.1:8000/ws/course/1/content/1");


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
            <div className="mt-10">
                <video className="h-[70%] mx-auto w-[70%] rounded-lg" controls>
                    <source
                        src="https://docs.material-tailwind.com/demo.mp4"
                        type="video/mp4"
                    />
                    Your browser does not support the video tag.
                </video>
            </div>
            <div className="w-[70%] mt-10 mx-auto">
                <h1 className="text-2xl font-semibold">Description : </h1>
                <p className="text-md px-5 py-10">
                    lorem lorem lorem loremlorem loremlorem loremlorem loremlorem
                    loremlorem loremlorem loremlorem loremlorem loremlorem loremlorem
                    loremlorem loremlorem loremlorem loremlorem loremlorem loremlorem
                    loremlorem loremlorem loremlorem loremlorem loremlorem loremlorem
                    loremlorem loremlorem loremlorem loremlorem loremlorem loremlorem
                    loremlorem loremlorem loremlorem loremlorem loremlorem loremlorem
                    loremlorem loremlorem loremlorem loremlorem loremlorem loremlorem
                    loremlorem loremlorem loremlorem loremlorem loremlorem loremlorem
                    loremlorem loremlorem loremlorem loremlorem loremlorem loremlorem
                    loremlorem loremlorem loremlorem loremlorem lorem{" "}
                </p>
            </div>
        </div>
    )
}

export default TrainerVideoView
