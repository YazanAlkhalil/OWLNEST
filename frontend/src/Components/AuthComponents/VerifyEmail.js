import React, { useEffect, useState } from "react";
import "./VerifyEmail.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { NavLink, useLocation, useNavigate } from "react-router-dom";
import backGround from "../../images/—Pngtree—e-learning education online illustration_6548963.png";
import OtpInput from "react-otp-input";
import { useDispatch, useSelector } from "react-redux";
import { signupSelector } from "../../features/Auth/SignUpSlice";
import { verifyOTP, verifyOTPSelector } from "../../features/Auth/VerifySlice";
import { resendOtp } from "../../features/Auth/ResendOtpSlice";
import toast from "react-hot-toast";
import Loader from "../Loader";

export default function VerifyEmail() {
  const navigate = useNavigate();
  const [otp, setOtp] = useState("");
  const { data } = useSelector(signupSelector);
  const dispatch = useDispatch();
  const [email,setEmail] = useState();
  const { isFetching } = useSelector(verifyOTPSelector);

  function onGoBackClick() {
    navigate("/signUP", { replace: true });
  }
  const [time, setTime] = useState(300); // 5 minutes = 300 seconds
  const [enable, setEnable] = useState(false);

  useEffect(() => {
    if (time > 0) {
      const timerId = setInterval(() => {
        setTime(prevTime => prevTime - 1);
      }, 1000);

      return () => clearInterval(timerId);
    } else {
      setEnable(true);
    }
  }, [time]);

  const formatTime = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
  };

  useEffect(()=>{
    console.log(data);
    setEmail(data.email)
  }
  ,[data]);
  const handleConfirmClick = async () => {
    const data1 = {
      email: data.email,
      otp: otp,
    };
   
    try {
      const resultAction = await dispatch(verifyOTP(data1));
      if (verifyOTP.fulfilled.match(resultAction)) {
        navigate('/login',{replace: true});
      } else {
          const errorMessage = resultAction.payload?.message || 'OTP incorrect';
          toast.error(errorMessage);
          console.log('OTP incorrect:', errorMessage);
      }
  } catch (error) {
      const errorMessage = error.response?.data?.message || 'An unknown error occurred';
      toast.error(errorMessage);
      console.log('OTP incorrect:', errorMessage);
  }
  }
  const handleResendClick = () => {
    const data = {
      email : email
    };
    console.log(data);
    dispatch(resendOtp(data))
  }


  return (
    <>
      <div className="verifyEmail">
        <div className="flex flex-wrap ">
          <div className="w-1/2">
            {
              isFetching ?  <div className='container w-[100%] h-[100%] flex justify-center items-center sm:px-4'>
              <Loader />
            </div> : <div className="container mx-auto sm:px-4 p-6">
              <FontAwesomeIcon className="cursor-pointer text-2xl" icon={faArrowLeft} onClick={onGoBackClick} />
              <div className="verify mt-4 p-12">
                <h3 className="font-semibold text-2xl">
                  We have sent you a verification code on your email
                </h3>
                <p className="font-semibold">Verification Code</p>
                <form className="text-center">
                  <div className="formGroup flex justify-center">
                    <OtpInput
                      value={otp}
                      onChange={setOtp}
                      numInputs={6}
                      renderSeparator={<span>-</span>}
                      renderInput={(props) => <input {...props} style={{ width: '50px' }} />}
                    />
                  </div>
                  <div
                    onClick={handleConfirmClick}
                    className="inline-block cursor-pointer align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline pt-3 text-gray-100 fw-bold button">
                    CONFIRM
                  </div>
                </form>
                <div className="resendDiv pt-5 mt-5 flex ">
                  <p className="font-semibold">{formatTime(time)}</p>
                  <button onClick={handleResendClick} disabled={!enable} className="inline-block ml-3 mt-3 align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline text-gray-100 font-semibold">
                    RESEND
                  </button>
                </div>
              </div>
            </div>
            }
          </div>
          <div className="w-1/2 loginBackGround">
            <div>
              <img
                src={backGround}
                className="mx-auto"
                alt="error"
                width={"500px"}
                height={"500px"}
              />
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
