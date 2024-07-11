import React, { useEffect, useState } from 'react'
import backGround from '../../images/—Pngtree—e-learning education online illustration_6548963.png';
import { useLocation, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { forgetPass } from '../../features/Auth/ForgetPasswordSlice';

export default function NewPassword() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [password,setPassword] = useState();
    const location = useLocation();
  const { Data } = location.state || {};
  useEffect(()=>{
    console.log(Data);
  }
  ,[]);
  const handleSubmit = (e)=>{
    e.preventDefault(); 
    const data = {
      email : Data,
      password : password
    };
    console.log(data);
    dispatch(forgetPass(data));
    navigate('/');
  }
  return (
    <>
      <div className='login'>
        <div className="flex flex-wrap ">
          <div className="w-1/2 pad text-center">
            <div className='container pt-5 rounded bg-slate-400 w-[80%] min-h-64 mx-auto sm:px-4'>
            <div>
                <h1 className='font-semibold mb-5 text-2xl text-white'>Please Enter Your New Passowrd</h1>
                <form>
                <input
                          type="password"
                          id="password"
                          placeholder="Password"
                          value={password}
                          onChange={(e) => setPassword(e.target.value)}
                          className={`w-full bg-white px-3 py-2  
                            rounded focus:outline-none`}
                            />
                            <button 
                     type="submit"
                    onClick={handleSubmit}
                     className='px-9 rounded mt-8 py-4 bg-primary text-white font-semibold '>Submit</button>
                   
                            {/* ${border
                            errors1.password
                              ? "border-red-500"
                              : "border-gray-300"
                          }  */}
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
