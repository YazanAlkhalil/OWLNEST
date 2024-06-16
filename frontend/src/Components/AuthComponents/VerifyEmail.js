import React from 'react';
import './VerifyEmail.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import { NavLink, useNavigate } from 'react-router-dom';

export default function VerifyEmail() {
  const navigate = useNavigate()

  function onGoBackClick(){
    navigate('/signUP',{replace: true});
  }

  return (
    <>
    <div className='verifyEmail'>
        <div className="row">
          <div className="col-6">
            <div className='container p-3'>
            <FontAwesomeIcon icon={faArrowLeft} onClick={onGoBackClick}/>
            <div className='verify mt-4 p-5'>
              <h3 className='fw-bold'>We have sent you a verification code on your email</h3>
              <p className='fw-bold'>Verification Code</p>
              <form className='text-center'>
                <div className='formGroup d-flex justify-content-center'>
                  <input type='text' />
                  <input type='text' />
                  <input type='text' />
                  <input type='text' />
                  <input type='text' />
                  <input type='text' />
                </div>
                <NavLink to={'/checkCompany'} className='btn pt-3 text-light fw-bold button'>CONFIRM</NavLink>
              </form>
              <div className='resendDiv pt-5 mt-5 d-flex'>
                <p className='fw-bold p-3'>00:56</p>
                <button className='btn text-light fw-bold'>RESEND</button>
              </div>
            </div>
            </div>
          </div>
          <div className="col-6 loginBackGround text-center">
            <div>
            <h1 className="text-light">
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
