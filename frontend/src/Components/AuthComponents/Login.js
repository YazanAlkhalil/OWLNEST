import React, { useState } from 'react';
import './Login.css';
import { NavLink } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { loginUser } from '../../features/Auth/LoginSlice';

export default function Login() {

  const [email , setEmail] = useState('');
  const [password , setPassword] = useState('');
  const dispatch = useDispatch();

  function handleSubmitClick(e){
    e.preventDefault();
    const data = {
      email : email,
      password : password
    }
    // console.log(data);
    dispatch(loginUser(data));
  }

  return (
   <>
      <div className='login'>
        <div className="row">
          <div className="col-6">
            <div className='container'>
            <div className="login-form text-center">
              <h2 className='fw-bold fs-2'>Login</h2>
              <p>How to i get started lorem ipsum dolor at?</p>
              <form onSubmit={handleSubmitClick}>
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
                <div className="form-group">
                  <input
                    type="password"
                    id="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
                <div className='forgetPass mt-3 mb-2'>
                    <a href='#'>Forget Password</a>
                </div>
                <button type="submit" className='btn btn-light fw-bold text-light'>Login Now</button>
              </form>
              <div className="sign-up mt-3">
                <p className='fw-bold'>- Get Started Now -</p>
                <NavLink to={'signUp'} className='btn pt-3 btn-light button fw-bold text-light'>Register</NavLink>
              </div>
            </div>
            </div>
          </div>
          <div className="col-6 loginBackGround text-center">
            <div>
            <h1 className="text-light fs-1">
                WELCOME IN OUR OWL NEST WEBSITE 😁
              </h1>
              <img  alt="error" width={'350px'} height={'350px'} />
            </div>
          </div>
        </div>
      </div>
      
   
   </>
  )
}
