import React from 'react';
import './TypeRegister.css';
import { NavLink } from 'react-router-dom';
import logo from './../../images/logo.png';
import backGround from './../../images/—Pngtree—e-learning education online illustration_6548963.png'

export default function TypeRegister() {
  return (
    <>
    <div className='TypeRegister'>
        <div className="flex flex-wrap ">
          <div className="w-1/2 text-center">
            <div className='container mx-auto sm:px-4'>
                <div className='checkCard mx-auto'>
                    <h4 className='font-semibold text-xl mb-4'>Do you have a Company?</h4>
                    <div className='mb-9'>
                        <img src={logo} className='mx-auto'  alt='error' width={'150px'} height={'150px'} />
                    </div>
                    <div className='buttonGroup flex justify-center gap-9'>
                        <NavLink to={'/companyDetails'} className='inline-block font-semibold p-5 align-middle  select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline button  text-gray-100'>Create Your Nest Now</NavLink>
                        <NavLink to={'/company'} className='inline-block font-semibold p-5 align-middle  select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline button  text-gray-100'>Maybe Later</NavLink>
                    </div>
                </div>
            </div>
          </div>
          <div className="w-1/2 loginBackGround">
            <div>
              <img src={backGround} className='mx-auto'  alt="error" width={'500px'} height={'500px'} />
            </div>
          </div>
        </div>
      </div>
    </>
  )
}
