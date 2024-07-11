<<<<<<< HEAD
import React, { useEffect, useState } from "react";
import "./VerifyEmail.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { NavLink, useLocation, useNavigate } from "react-router-dom";
import backGround from "../../images/—Pngtree—e-learning education online illustration_6548963.png";
import OtpInput from "react-otp-input";
import { useDispatch, useSelector } from "react-redux";
import { signupSelector } from "../../features/Auth/SignUpSlice";
import { verifyOTP } from "../../features/Auth/VerifySlice";
import { resendOtp } from "../../features/Auth/ResendOtpSlice";
=======
import React, { useState } from "react";
import "./VerifyEmail.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { NavLink, useNavigate } from "react-router-dom";
import backGround from "../../images/—Pngtree—e-learning education online illustration_6548963.png";
import OtpInput from "react-otp-input";
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73

export default function VerifyEmail() {
  const navigate = useNavigate();
  const [otp, setOtp] = useState("");
<<<<<<< HEAD
  const { data } = useSelector(signupSelector);
  const dispatch = useDispatch();
  const [email,setEmail] = useState();
  const location = useLocation();
  const { myData,from } = location.state || {};
=======
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73

  function onGoBackClick() {
    navigate("/signUP", { replace: true });
  }
<<<<<<< HEAD
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
  useEffect(()=>{
    console.log(myData,from);
  }
  ,[]);
  const handleConfirmClick = () => {
    const data1 = {
      email: data.email || myData,
      otp: otp,
    };
    dispatch(verifyOTP(data1)).then(() => {
      if (from === 'signup') {
        navigate('/login');
      } else if (from === 'forgetPass') {
        navigate('/newPassword',{ state: { Data: myData } });
      }
    });
  }
  const handleResendClick = () => {
    const data = {
      email : email || myData
    };
    console.log(data);
    dispatch(resendOtp(data))
  }

=======
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73

  return (
    <>
      <div className="verifyEmail">
        <div className="flex flex-wrap ">
          <div className="w-1/2">
            <div className="container mx-auto sm:px-4 p-6">
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
                  <NavLink
<<<<<<< HEAD
                    onClick={handleConfirmClick}
                    to={"/"}
=======
                    to={"/checkCompany"}
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
                    className="inline-block align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline pt-3 text-gray-100 fw-bold button">
                    CONFIRM
                  </NavLink>
                </form>
                <div className="resendDiv pt-5 mt-5 flex ">
<<<<<<< HEAD
                  <p className="font-semibold">{formatTime(time)}</p>
                  <button onClick={handleResendClick} disabled={!enable} className="inline-block ml-3 mt-3 align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline text-gray-100 font-semibold">
=======
                  <p className="font-semibold">00:56</p>
                  <button className="inline-block ml-3 mt-3 align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline text-gray-100 font-semibold">
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
                    RESEND
                  </button>
                </div>
              </div>
            </div>
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
