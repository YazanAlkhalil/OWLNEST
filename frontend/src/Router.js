import React from "react";
import { Routes, Route } from "react-router-dom";
import LoginPage from "./Pages/Auth/LoginPage";
import RegisterPage from "./Pages/Auth/RegisterPage";
import VerifyEmail from "./Components/AuthComponents/VerifyEmail";
import TypeRegister from "./Components/AuthComponents/TypeRegister";
import CompanyDetails from "./Components/AuthComponents/CompanyDetails";
import TrainerLayout from './Components/TrainerLayout';
import TraineeLayout from './Components/TraineeLayout'
import AdminLayout from './Components/AdminLayout';
import CreateCoursePage from './Pages/trainer/CreateCoursePage';

export default function Router() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="/signUp" element={<RegisterPage />} />
      <Route path="/verify" element={<VerifyEmail />} />
      <Route path="/checkCompany" element={<TypeRegister />} />
      <Route path="/companyDetails" element={<CompanyDetails />} />
      <Route path="/trainee" element={<TraineeLayout />}></Route>

      <Route path="/trainer" element={<TrainerLayout />}>
        <Route index path="/trainer/" element={<CreateCoursePage />} />
      </Route>

      <Route path="/admin" element={<AdminLayout />}></Route>
    </Routes>
  );
}
