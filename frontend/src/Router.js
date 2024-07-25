import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "./Pages/Auth/LoginPage";
import RegisterPage from "./Pages/Auth/RegisterPage";
import VerifyEmail from "./Components/AuthComponents/VerifyEmail";
import TypeRegister from "./Components/AuthComponents/TypeRegister";
import CompanyDetails from "./Components/AuthComponents/CompanyDetails";
import TrainerLayout from "./Components/TrainerLayout";
import TraineeLayout from "./Components/TraineeLayout";
import AdminLayout from "./Components/AdminLayout";
import CreateCoursePage from "./Pages/trainer/CreateCoursePage";
import TrainerCoursesPage from "./Pages/trainer/TrainerCoursesPage";
import AdminDashboard from "./Pages/admin/AdminDashboard";
import AdminCourseDetails from "./Pages/admin/AdminCourseDetails";
import AdminCoursesPage from "./Pages/admin/AdminCoursesPage";
import AdminUsers from "./Pages/admin/AdminUsers";
import NotFoundPage from "./Pages/NotFoundPage";
import CompanyPage from "./Pages/CompanyPage";
import TranieeDashboard from "./Components/trainee/TranieeDashboard";
import TraineeCourses from "./Components/trainee/TraineeCourses";
import TraineeFavorites from "./Components/trainee/TraineeFavorites";
import TraineeCertificate from "./Components/trainee/TraineeCertificate";
import TraineeCourseDisplay from "./Components/trainee/TraineeCourseDisplay";
import TraineeProgress from "./Components/trainee/TraineeProgress";
import TraineeDiscussion from "./Components/trainee/TraineeDiscussion";
import TraineeInfor from "./Components/trainee/TraineeInfor";
import CourseLayout from "./Components/trainee/CourseLayout";
import Plane from "./Components/admin/Plane";
import TraineeVideoLesson from "./Components/trainee/TraineeLesson";
import TraineeQuiz from "./Components/TraineeQuiz";
import TraineePdf from "./Components/trainee/TraineePdf";
import LandingPage from "./Pages/LandingPage";
import FoegetPassEmail from "./Components/AuthComponents/FoegetPassEmail";
import NewPassword from "./Components/AuthComponents/NewPassword";

export default function Router() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/signUp" element={<RegisterPage />} />
      <Route path="/verify" element={<VerifyEmail />} />
      <Route path="/checkCompany" element={<TypeRegister />} />
      <Route path="/companyDetails" element={<CompanyDetails />} />
      <Route path="/company" element={<CompanyPage />} />
      <Route path="/forgetPassEmail" element={<FoegetPassEmail />} />
      <Route path="/newPassword/api/password_reset/:uuid/:token" element={<NewPassword />} />

      <Route path="/trainee" element={<TraineeLayout />}>
        <Route path="/trainee/homePage" element={<TranieeDashboard />} />

        <Route path="/trainee/courses" element={<TraineeCourses />}>
        </Route>
        <Route path="/trainee/favorites" element={<TraineeFavorites />} />
        <Route path="/trainee/certifications" element={<TraineeCertificate />} />
        <Route
          path="/trainee"
          element={<Navigate to="/trainee/homePage" replace />}
        />
      </Route>

      <Route path="/trainee/courses/:id" element={<CourseLayout />}>
        <Route path="content" element={<TraineeCourseDisplay />} />
        <Route path="content/lesson" element={<TraineeVideoLesson />} />
        <Route path="progress" element={<TraineeProgress />} />
        <Route path="discussion" element={<TraineeDiscussion />} />
        <Route path="Info" element={<TraineeInfor />} />
      </Route>

        <Route path="/trainee/courses/:id/content/quiz" element={<TraineeQuiz />} />
        <Route path="/trainee/courses/:id/content/Text" element={<TraineePdf />} />




      <Route path="/trainer" element={<TrainerLayout />}>
        <Route path="/trainer/courses/:id" element={<CreateCoursePage />} />
        <Route path="/trainer/courses" element={<TrainerCoursesPage />} />
        <Route
          path="/trainer"
          element={<Navigate to="/trainer/courses" replace />}
        />
      </Route>

      <Route path="/admin" element={<AdminLayout />}>
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
        <Route path="/admin/buyCourse" element={<Plane />} />
        <Route path="/admin/courses/:id" element={<AdminCourseDetails />} />
        <Route path="/admin/courses" element={<AdminCoursesPage />} />
        <Route path="/admin/users" element={<AdminUsers />} />
        {/* <Route path='/admin/users/:id' element={<AdminCoursesPage />} /> */}
        <Route
          path="/admin"
          element={<Navigate to="/admin/dashboard" replace />}
        />
      </Route>
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}
