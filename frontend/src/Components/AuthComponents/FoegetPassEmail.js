import React, { useState } from 'react'
import backGround from '../../images/—Pngtree—e-learning education online illustration_6548963.png';
import './ForgetPassEmail.css';
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { resendOtp } from '../../features/Auth/ResendOtpSlice';

export default function FoegetPassEmail() {
    const [email,setEmail] = useState();
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault(); 

        const data = {
            email: email
        };

        console.log(data);
        dispatch(resendOtp(data));

        navigate('/verify', { state: { myData: email ,from: 'forgetPass' } });
    };
  return (
    <>
      <div className='login'>
        <div className="flex flex-wrap ">
          <div className="w-1/2 pad text-center">
            <div className='container pt-5 rounded bg-slate-400 w-[80%] min-h-52 mx-auto sm:px-4'>
                <div>
                    <h1 className='font-semibold mb-2 text-2xl text-white'>Enter your Email</h1>
                    <form>
                    <input
                    type="email"
                    id="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className={`w-full bg-white px-3 py-2 
                        rounded focus:outline-none`}
                        // required
                        />
                    <button 
                     type="submit"
                    onClick={handleSubmit}
                     className='px-9 rounded mt-5 py-4 bg-primary text-white font-semibold '>Submit</button>
                    </form>
                        {/* ${errors.password ? 'border border-red-500' : 'border-gray-300'}  */}
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
