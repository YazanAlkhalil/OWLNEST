import React, { useState } from "react";
import "./Register.css";
import { NavLink, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { signupSelector, signupUser } from "../../features/Auth/SignUpSlice";
import backGround from "../../images/—Pngtree—e-learning education online illustration_6548963.png";
import toast from "react-hot-toast";
import Loader from "../Loader";
import { IoArrowBack } from "react-icons/io5";
import { TextField } from "@mui/material";

const countries = [
  ["DZ", "Algeria"],
  ["BH", "Bahrain"],
  ["EG", "Egypt"],
  ["IQ", "Iraq"],
  ["JO", "Jordan"],
  ["KW", "Kuwait"],
  ["LB", "Lebanon"],
  ["LY", "Libya"],
  ["MR", "Mauritania"],
  ["MA", "Morocco"],
  ["OM", "Oman"],
  ["PS", "Palestine"],
  ["QA", "Qatar"],
  ["SA", "Saudi Arabia"],
  ["SD", "Sudan"],
  ["SY", "Syria"],
  ["TN", "Tunisia"],
  ["AE", "United Arab Emirates"],
  ["YE", "Yemen"],
];

export default function Register() {
  const navigate = useNavigate();
  const { isFetching } = useSelector(signupSelector);
  // states
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [confPass, setConfPass] = useState("");
  const [phone, setPhoneNumber] = useState("");
  const [date, setDate] = useState("");
  const [gender, setGender] = useState("M");
  const [country, setCountry] = useState("SY");
  const [errors1, setErrors1] = useState({});
  const [errors2, setErrors2] = useState({});

  const validate1 = () => {
    const errors = {};

    if (!username) {
      errors.username = "Username is required";
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email) {
      errors.email = "Email is required";
    } else if (!emailRegex.test(email)) {
      errors.email = "Invalid email format";
    }

    if (!password) {
      errors.password = "Password is required";
    } else if (password.length < 6) {
      errors.password = "Password must be at least 6 characters";
    }

    if (!confPass) {
      errors.confPass = "Confirm Password is required";
    } else if (confPass !== password) {
      errors.confPass = "Passwords do not match";
    }

    setErrors1(errors);

    return Object.keys(errors).length === 0;
  };

  const validate2 = () => {
    const errors = {};
    if (!phone) {
      errors.phoneNumber = "Phone Number is required";
    }

    if (!date) {
      errors.date = "Date is required";
    }
    if (!gender) {
      errors.gender = "Gender is required";
    }
    if (!country) {
      errors.country = "Country is required";
    }
    setErrors2(errors);

    return Object.keys(errors).length === 0;
  };

  // configure another form
  const [firstPart, setFirstPart] = useState(false);
  function onNextClick() {
    if (validate1()) {
      setFirstPart(true);
    }
  }

  // redux logic
  const dispatch = useDispatch();

  const handleSubmittedClick = async (e) => {
    e.preventDefault();
    const data = {
      username: username,
      password: password,
      email: email,
      phone: phone,
      birthday: date,
      gender: gender,
      country: country,
    };
    if (validate2()) {
      try {
        const resultAction = await dispatch(signupUser(data));
        if (signupUser.fulfilled.match(resultAction)) {
          navigate('/verify', { replace: true });
        } else {
          const errorMessage = resultAction.payload?.message || 'Register failed';
          toast.error(errorMessage);
          console.log('Register failed:', errorMessage);
        }
      } catch (error) {
        const errorMessage = error.response?.data?.message || 'An unknown error occurred';
        toast.error(errorMessage);
        console.log('Register failed:', errorMessage);
      }
    }
  };

  return (
    <>
      <div className="signUp">
        <div className="flex flex-wrap ">
          <div className="w-1/2">
            {
              isFetching ? <div className='container w-[100%] h-[100%] flex justify-center items-center sm:px-4'>
                <Loader />
              </div> : <div className="container mx-auto sm:px-4">
                <div className="login-form flex flex-col justify-evenly h-screen text-center">
                  <h2 className="font-semibold text-3xl mb-10">Register</h2>
                  <form onSubmit={handleSubmittedClick}>
                    {!firstPart && (
                      <>
                        <div className="mb-4 mb-3">
                          <div class="my-6 relative w-full min-w-[200px] h-12">
                            <input
                              class={"peer w-full h-full bg-transparent text-blue-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-gray-900"}
                              type="text"
                              id="username"
                              placeholder=""
                              value={username}
                              onChange={(e) => setUsername(e.target.value)} />
                            <label
                              class="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal !overflow-visible truncate peer-placeholder-shown:text-blue-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-gray-500 peer-focus:text-gray-900 before:border-blue-gray-200 peer-focus:before:!border-gray-900 after:border-blue-gray-200 peer-focus:after:!border-gray-900">Username
                            </label>
                            
                          </div>
                          {errors1.username && (
                            <div className="text-red-500 text-sm   font-semibold">
                              {errors1.username}
                            </div>
                          )}
                        </div>
                        <div className="mb-4 mb-3">
                          
                          <div class="my-6 relative w-full min-w-[200px] h-12">
                            <input
                              class="peer w-full h-full bg-transparent text-blue-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-gray-900"
                              type="email"
                            id="email"
                            placeholder=""
                            value={email}
                            onChange={(e) => setEmail(e.target.value)} />
                            <label
                              class="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal !overflow-visible truncate peer-placeholder-shown:text-blue-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-gray-500 peer-focus:text-gray-900 before:border-blue-gray-200 peer-focus:before:!border-gray-900 after:border-blue-gray-200 peer-focus:after:!border-gray-900">
                                Email
                            </label>
                          </div>
                          {errors1.email && (
                            <div className="text-red-500 text-sm  font-semibold">
                              {errors1.email}
                            </div>
                          )}
                        </div>
                        <div className="mb-4 mb-3">
                          
                          <div class="my-6 relative w-full min-w-[200px] h-12">
                            <input
                              class="peer w-full h-full bg-transparent text-blue-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-gray-900"
                              type="password"
                              id="password"
                            placeholder=""
                            value={password}
                            onChange={(e) => setPassword(e.target.value)} />
                            <label
                              class="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal !overflow-visible truncate peer-placeholder-shown:text-blue-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-gray-500 peer-focus:text-gray-900 before:border-blue-gray-200 peer-focus:before:!border-gray-900 after:border-blue-gray-200 peer-focus:after:!border-gray-900">
                                Password
                            </label>
                          </div>
                          {errors1.password && (
                            <div className="text-red-500 text-sm  font-semibold">
                              {errors1.password}
                            </div>
                          )}
                        </div>
                        <div className="mb-4 mb-3">
                          
                          <div class="my-6 relative w-full min-w-[200px] h-12">
                            <input
                              class="peer w-full h-full bg-transparent text-blue-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-gray-900"
                              type="password"
                            id="confirmPassword"
                            placeholder=""
                            value={confPass}
                            onChange={(e) => setConfPass(e.target.value)} />
                            <label
                              class="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal !overflow-visible truncate peer-placeholder-shown:text-blue-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-gray-500 peer-focus:text-gray-900 before:border-blue-gray-200 peer-focus:before:!border-gray-900 after:border-blue-gray-200 peer-focus:after:!border-gray-900">
                                Confirm Password
                            </label>
                          </div>
                          {errors1.confPass && (
                            <div className="text-red-500 text-sm  font-semibold">
                              {errors1.confPass}
                            </div>
                          )}
                        </div>
                        <button
                          type="button"
                          onClick={onNextClick}
                          className="inline-block text-white font-semibold align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline bg-gray-100 text-gray-800 hover:bg-gray-200 fw-bold text-gray-100">
                          NEXT
                        </button>
                      </>
                    )}
                    {firstPart && (
                      <>
                        <div classNamy-6 me="mb-4 mb-3">
                          <div class="relative mb-4  w-full min-w-[200px] h-10">
                            <input
                              class="peer w-full h-full bg-transparent text-blue-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-gray-900"
                              type="number"
                            id="phone"
                            placeholder=""
                            value={phone}
                            onChange={(e) => setPhoneNumber(e.target.value)} />
                            <label
                              class="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal !overflow-visible truncate peer-placeholder-shown:text-blue-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-gray-500 peer-focus:text-gray-900 before:border-blue-gray-200 peer-focus:before:!border-gray-900 after:border-blue-gray-200 peer-focus:after:!border-gray-900">
                                Phone number
                            </label>
                          </div>
                          {errors2.phoneNumber && (
                            <div className="text-red-500 text-sm  font-semibold">
                              {errors2.phoneNumber}
                            </div>
                          )}
                        </div>
                        <div classNamy-6 me="mb-4 mb-3">
                          <input
                            type="date"
                            id="date"
                            value={date}
                            onChange={(e) => setDate(e.target.value)}
                            className={`w-full mb-4  bg-white px-3 py-2 border ${errors2.date ? "border-red-500" : "border-gray-300"
                              } rounded focus:outline-none`}
                          />
                          {errors2.date && (
                            <div className="text-red-500 text-sm  font-semibold">
                              {errors2.date}
                            </div>
                          )}
                        </div>
                        <div className="mb-4">
                          <select
                            name="gender"
                            value={gender}
                            onChange={(e) => setGender(e.target.value)}
                            className={`w-full px-3 py-2 border ${errors2.gender
                              ? "border-red-500"
                              : "border-gray-300"
                              } rounded focus:outline-none`}>
                            <option value="M">Male</option>
                            <option value="F">Female</option>
                          </select>
                          {errors2.gender && (
                            <div className="text-red-500 text-sm  font-semibold">
                              {errors2.gender}
                            </div>
                          )}
                        </div>
                        <div className="mb-4 mb-3">
                          <div className="wrapper">
                            <select
                              name="country"
                              id="select-box"
                              value={country}
                              onChange={(e) => setCountry(e.target.value)}
                              className={`w-full px-3 py-2 border ${errors2.country
                                ? "border-red-500"
                                : "border-gray-300"
                                } rounded focus:outline-none`}
                            >
                              {countries.map(([code, name]) => (
                                <option key={code} value={code}>
                                  {name}
                                </option>
                              ))}
                            </select>
                            {errors2.country && (
                              <div className="text-red-500 text-sm  font-semibold">
                                {errors2.country}
                              </div>
                            )}
                          </div>
                        </div>
                        <button
                          // to="/verify"
                          type="submit"
                          className="inline-block text-white button  font-semibold align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline bg-gray-100 text-gray-800 hover:bg-gray-200 fw-bold text-gray-100">
                          Register
                        </button>
                      </>
                    )}
                  </form>
                  <div className="sign-up mt-3">
                    <p className="font-semibold mb-3">
                      - Already have an account? -
                    </p>
                    <NavLink
                      to={"/login"}
                      className="inline-block pt-5 font-semibold text-white align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline pt-3 bg-gray-100 text-gray-800 hover:bg-gray-200 button fw-bold text-gray-100">
                      LOGIN
                    </NavLink>
                    {
                      firstPart &&
                      <div className="flex items-center justify-start gap-2 mt-10">
                        <IoArrowBack className="hover:cursor-pointer" onClick={() => { setFirstPart(!firstPart) }} />
                        <h1 className="hover:cursor-pointer" onClick={() => { setFirstPart(!firstPart) }}>Go Back</h1>
                      </div>
                    }
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
