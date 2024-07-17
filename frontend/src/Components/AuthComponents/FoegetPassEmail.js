import React, { useState } from 'react'
import backGround from '../../images/—Pngtree—e-learning education online illustration_6548963.png';
import './ForgetPassEmail.css';
import { useDispatch, useSelector } from 'react-redux';
import { requestEmail, requestEmailSelector } from '../../features/Auth/RequestEmail';
import toast from 'react-hot-toast';
import Loader from '../Loader';

export default function FoegetPassEmail() {
    const [email,setEmail] = useState();
    const dispatch = useDispatch();
    const [errors, setErrors] = useState({});
    const {isFetching} = useSelector(requestEmailSelector);

    const validate = () => {
      const errors = {};
  
      // Email validation
      if (!email) {
        errors.email = 'Email is required';
      } else if (!/\S+@\S+\.\S+/.test(email)) {
        errors.email = 'Email address is invalid';
      }
      setErrors(errors);
      return Object.keys(errors).length === 0;
    };

    const handleSubmit = async (e) => {
        e.preventDefault(); 

        const data = {
            email: email
        };
        console.log(data);
       if (validate()) {
        const resultAction = await dispatch(requestEmail(data));
        if (requestEmail.fulfilled.match(resultAction)) {
            toast.success('we have sent a link to reset your password.',{
              duration: 3000,
              icon: '👏'
            });
        } else if (requestEmail.rejected.match(resultAction)) {
            const errorMessage = resultAction.payload?.detail || 'Email not Found';
            toast.error(errorMessage);
            console.log('Email Not Found:', errorMessage);
        } 
       }
    };
  return (
    <>
      <div className='login'>
        <div className="flex flex-wrap ">
          <div className="w-1/2 pad text-center">
            {
              isFetching ? <div className='container w-[100%] h-[100%] flex justify-center items-center sm:px-4'>
              <Loader />
            </div> : <div className='container pt-5 rounded bg-slate-300 w-[80%] min-h-60 mx-auto sm:px-4'>
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
                      ${errors.password ? 'border border-red-500' : 'border-gray-300'} 
                        rounded focus:outline-none`}
                        />
                         {errors.email && <div className="font-semibold mt-2 text-sm text-red-500">{errors.email}</div>}
                    <button 
                     type="submit"
                    onClick={handleSubmit}
                     className='px-9 rounded mt-5 py-4 bg-primary text-white font-semibold '>Submit</button>
                    </form>
                        {/* ${errors.password ? 'border border-red-500' : 'border-gray-300'}  */}
                </div>
            </div>
            }
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
