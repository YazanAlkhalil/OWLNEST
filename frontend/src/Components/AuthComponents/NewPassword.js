import React, { useEffect, useState } from 'react'
import backGround from '../../images/—Pngtree—e-learning education online illustration_6548963.png';
import { useLocation, useNavigate, useParams } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { forgetPass } from '../../features/Auth/ForgetPasswordSlice';

export default function NewPassword() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [password,setPassword] = useState();
    const { uuid, token } = useParams();
    const [confirmPassword, setConfirmPassword] = useState('');
    const [errors, setErrors] = useState({});

    const validate = () => {
        const newErrors = {};
        if (!password) {
            newErrors.password = 'Password is required';
        }
        if (password !== confirmPassword) {
            newErrors.confirmPassword = 'Passwords do not match';
        }
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

  const handleSubmit = (e)=>{
    e.preventDefault();
     
    const data = {
      password : password,
      uidb64 : uuid,
      token : token
    };
    console.log(data);
    if(validate()){
      dispatch(forgetPass(data));
      navigate('/login');
    }
  }
  return (
    <>
      <div className='login'>
        <div className="flex flex-wrap ">
          <div className="w-1/2 pad text-center">
            <div className='container pt-5 rounded bg-slate-300 w-[80%] min-h-64 mx-auto sm:px-4'>
            <div>
                <h1 className='font-semibold mb-5 text-2xl text-white'>Please Enter Your New Passowrd</h1>
                <form onSubmit={handleSubmit}>
            <div className="mb-4">
                <input
                    type="password"
                    id="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className={`w-full bg-white px-3 py-2 rounded focus:outline-none ${errors.password ? 'border-red-500' : 'border-gray-300'}`}
                />
                {errors.password && <p className="text-red-500 font-semibold text-sm">{errors.password}</p>}
            </div>
            <div className="">
                <input
                    type="password"
                    id="confirmPassword"
                    placeholder="Confirm Password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    className={`w-full bg-white px-3 py-2 rounded focus:outline-none ${errors.confirmPassword ? 'border-red-500' : 'border-gray-300'}`}
                />
                {errors.confirmPassword && <p className="text-red-500 font-semibold text-sm">{errors.confirmPassword}</p>}
            </div>
            <button 
                type="submit"
                className='px-9 rounded mb-4 mt-8 py-4 dark:bg-DarkGray bg-primary text-white font-semibold'
            >
                Submit
            </button>
        </form>
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
