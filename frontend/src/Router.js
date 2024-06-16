import React from 'react';
import { Routes, Route } from "react-router-dom";
import LoginPage from './Pages/Auth/LoginPage';
import RegisterPage from './Pages/Auth/RegisterPage';
import VerifyEmail from './Components/AuthComponents/VerifyEmail';
import TypeRegister from './Components/AuthComponents/TypeRegister';
import CompanyDetails from './Components/AuthComponents/CompanyDetails';

export default function Router() {
  return (
    <Routes>
            <Route path="/" element={<LoginPage />} />
            <Route path='/signUp' element={<RegisterPage />} />
            <Route path='/verify' element={<VerifyEmail />} /> 
            <Route path='/checkCompany' element={<TypeRegister />} /> 
            <Route path='/companyDetails' element={<CompanyDetails />} /> 
    </Routes>
  )
}
