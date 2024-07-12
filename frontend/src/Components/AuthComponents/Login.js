import React, { useState } from 'react';
import './Login.css';
import { NavLink, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import backGround from '../../images/—Pngtree—e-learning education online illustration_6548963.png';
import { loginUser } from '../../features/Auth/LoginSlice';


export default function Login() {

  const [email , setEmail] = useState('');
  const [password , setPassword] = useState('');
  const dispatch = useDispatch();
  const [errors, setErrors] = useState({});
  const navigate = useNavigate();

  const validate = () => {
    const errors = {};

    // Email validation
    if (!email) {
      errors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      errors.email = 'Email address is invalid';
    }

    // Password validation
    if (!password) {
      errors.password = 'Password is required';
    } else if (password.length < 6) {
      errors.password = 'Password must be at least 6 characters';
    }

    setErrors(errors);

    // Return true if there are no errors
    return Object.keys(errors).length === 0;
  };


  const handleSubmitClick = async (e) => {
    e.preventDefault();
    if (validate()) {
        const data = { email, password };
        const resultAction = await dispatch(loginUser(data));
        if (loginUser.fulfilled.match(resultAction)) {
            navigate('/checkCompany');
        } else {
            console.log('Login failed:', resultAction.payload);
        }
    }
};

  return (
   <>
     <div className='login'>
        <div className="flex flex-wrap ">
          <div className="w-1/2">
            <div className='container mx-auto sm:px-4'>
            <div className="login-form text-center">
              <h1 className='font-semibold mb-4 text-2xl font-medium'>Login</h1>
              <p className='mb-3'>How to i get started lorem ipsum dolor at?</p>
              <form onSubmit={handleSubmitClick}>
                <div className="mb-4 mb-3">
                  <input
                    type="email"
                    id="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className={`w-full px-3 py-2  ${errors.password ? 'border border-red-500' : 'border-gray-300'} rounded focus:outline-none`}
                    // required
                  />
                  {errors.email && <div className="font-semibold text-sm text-red-500">{errors.email}</div>}
                </div>
                <div className="mb-4">
                  <input
                    type="password"
                    id="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className={`w-full px-3 py-2  ${errors.password ? 'border border-red-500' : 'border-gray-300'} rounded focus:outline-none`}
                    // required
                  />
                  {errors.password && <div className="font-semibold text-sm text-red-500">{errors.password}</div>}
                </div>
                <div className='forgetPass mt-3 mb-2'>
                    <NavLink to={'/forgetPassEmail'} className='underline'>Forget Password</NavLink>
                </div>
                <button type="submit" className='inline-block align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline bg-gray-100 text-gray-800 hover:bg-gray-600 fw-bold '>Login Now</button>
              </form>
              <div className="sign-up mt-3">
                <p className='fw-bold'>- Get Started Now -</p>
                <NavLink to={'signUp'} className='inline-block align-middle pt-5 text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline pt-3 bg-gray-100 text-gray-800 hover:bg-gray-200 button fw-bold '>Register</NavLink>
              </div>
            </div>
            </div>
          </div>
          <div className="w-1/2 loginBackGround ">
            <div>
              <img src={backGround} className='mx-auto' alt="error" width={'500px'} height={'500px'} />
            </div>
          </div>
        </div>
      </div>
      
   
   </>
  )
}
