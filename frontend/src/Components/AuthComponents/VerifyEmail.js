import React, { useEffect, useState } from "react";
import "./VerifyEmail.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { NavLink, useNavigate } from "react-router-dom";
import backGround from "../../images/—Pngtree—e-learning education online illustration_6548963.png";
import OtpInput from "react-otp-input";
import { useSelector } from "react-redux";
import { signupSelector } from "../../features/Auth/SignUpSlice";

export default function VerifyEmail() {
  const navigate = useNavigate();
  const [otp, setOtp] = useState("");
  const { data } = useSelector(signupSelector);

  function onGoBackClick() {
    navigate("/signUP", { replace: true });
  }
  useEffect(()=>{
    console.log(data);
  }
  ,[data]);

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
                    to={"/checkCompany"}
                    className="inline-block align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline pt-3 text-gray-100 fw-bold button">
                    CONFIRM
                  </NavLink>
                </form>
                <div className="resendDiv pt-5 mt-5 flex ">
                  <p className="font-semibold">00:56</p>
                  <button className="inline-block ml-3 mt-3 align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline text-gray-100 font-semibold">
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
