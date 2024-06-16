import React, { useState } from "react";
import "./Register.css";
import { NavLink } from "react-router-dom";
import { useDispatch } from "react-redux";
import { signupUser } from "../../features/Auth/SignUpSlice";

export default function Register() {

  // states
  const [username,setUsername] = useState('');
  const [password,setPassword] = useState('');
  const [email,setEmail] = useState('');
  const [confPass,setConfPass] = useState('');
  const [phoneNumber,setPhoneNumber] = useState('');
  const [date,setDate] = useState('');
  const [gender,setGender] = useState('Male');
  const [country,setCountry] = useState('USA');

  // configure another form 
  const [firstPart, setFirstPart] = useState(false);
  function onNextClick() {
    setFirstPart(true);
  }

  // redux logic
  const dispatch = useDispatch();
  

  function handleSubmittedClick(e){
    e.preventDefault();
    const data = {
      username:username,  
      password:password,
      email:email,
      confPass:confPass,
      phoneNumber:phoneNumber,
      date:date,
      gender:gender,
      country:country
    }
    // console.log(data);
    dispatch(signupUser(data));
  }

  return (
    <>
      <div className="signUp">
        <div className="row">
          <div className="col-6">
            <div className="container">
              <div className="login-form text-center">
                <h2 className="fw-bold mb-4">Register</h2>
                <form onSubmit={handleSubmittedClick}>
                  {!firstPart && (
                    <>
                      <div className="form-group mb-3">
                        <input
                          type="text"
                          id="username"
                          placeholder="Username"
                          value={username}
                          onChange={(e) => setUsername(e.target.value)}
                          required
                        />
                      </div>
                      <div className="form-group mb-3">
                        <input
                          type="email"
                          id="email"
                          placeholder="Email"
                          value={email}
                          onChange={(e) => setEmail(e.target.value)}
                          required
                        />
                      </div>
                      <div className="form-group mb-3">
                        <input
                          type="password"
                          id="password"
                          placeholder="Password"
                          value={password}
                          onChange={(e) => setPassword(e.target.value)}
                          required
                        />
                      </div>
                      <div className="form-group mb-3">
                        <input
                          type="password"
                          id="password"
                          placeholder="Confirm Password"
                          value={confPass}
                          onChange={(e) => setConfPass(e.target.value)}
                          required
                        />
                      </div>
                      <button
                        onClick={onNextClick}
                        className="btn btn-light fw-bold text-light">
                        NEXT
                      </button>
                    </>
                  )}
                  {firstPart && (
                    <>
                      <div className="form-group mb-3">
                        <input
                          type="number"
                          id="phone"
                          placeholder="Phone Number"
                          value={phoneNumber}
                          onChange={(e) => setPhoneNumber(e.target.value)}
                          required
                        />
                      </div>
                      <div className="form-group mb-3">
                        <input
                          type="date"
                          id="date"
                          value={date}
                          onChange={(e) => setDate(e.target.value)}
                          required
                        />
                      </div>
                      <div className="form-group mb-3">
                        <select name="gender" value={gender} onChange={(e)=> setGender(e.target.value)} >
                          <option value="Male">Male</option>
                          <option value="FeMale">FeMale</option>
                        </select>
                      </div>
                      <div className="form-group mb-3">
                        <div className="wrapper">
                          <select
                            name="country"
                            id="select-box"
                            value={country} 
                            onChange={(e)=> setCountry(e.target.value)} 
                            >
                            <option value="USA">USA</option>
                            <option value="Three">Three</option>
                            <option value="Four">Four</option>
                            <option value="Five">Five</option>
                            <option value="Six">Six</option>
                            <option value="Seven">Seven</option>
                            <option value="Eight">Eight</option>
                            <option value="Nine">Nine</option>
                            <option value="Ten">Ten</option>
                          </select>
                        </div>
                      </div>
                      <button
                        to="/verify"
                        type="submit"
                        className="btn btn-light fw-bold text-light">
                        Register
                      </button>
                    </>
                  )}
                </form>
                <div className="sign-up mt-3">
                  <p className="fw-bold">- Already have an account? -</p>
                  <NavLink to={'/'} className='btn pt-3 btn-light button fw-bold text-light'>LOGIN</NavLink>
                </div>
              </div>
            </div>
          </div>
          <div className="col-6 loginBackGround text-center">
            <div>
              <h1 className="text-light">WELCOME IN OUR OWL NEST WEBSITE 😁</h1>
              <img
                alt="error"
                width={"350px"}
                height={"350px"}
              />
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
