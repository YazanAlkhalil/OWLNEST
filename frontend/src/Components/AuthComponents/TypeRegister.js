import React from 'react';
import backGround from "../../images/logo-removebg-preview.png";
import './TypeRegister.css';
import { NavLink } from 'react-router-dom';

export default function TypeRegister() {
  return (
    <>
    <div className='TypeRegister'>
        <div className="row">
          <div className="col-6 text-center">
            <div className='container'>
                <div className='checkCard'>
                    <h4 className='fw-bold mb-4'>Do you have a Company?</h4>
                    <div className='mb-5'>
                        <img src={backGround} alt='error' width={'150px'} height={'150px'} />
                    </div>
                    <div className='buttonGroup'>
                        <NavLink to={'/companyDetails'} className='btn button fw-bold text-light'>Create Your Nest Now</NavLink>
                        <NavLink className='btn button fw-bold text-light'>Maybe Later</NavLink>
                    </div>
                </div>
            </div>
          </div>
          <div className="col-6 loginBackGround text-center">
            <div>
            <h1 className="text-light">
                WELCOME IN OUR OWL NEST WEBSITE 😁
              </h1>
              <img src={backGround} alt="error" width={'350px'} height={'350px'} />
            </div>
          </div>
        </div>
      </div>
    </>
  )
}
