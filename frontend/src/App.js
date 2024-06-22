import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
// import RegisterPage from './Pages/Auth/RegisterPage';
import Router from './Router';
import CreateCoursePage from './Pages/trainer/CreateCoursePage';
import { Toaster } from 'react-hot-toast';
import TrainerLayout from './Components/TrainerLayout';
import TraineeLayout from './Components/TraineeLayout'
import AdminLayout from './Components/AdminLayout';
import LoginPage from './Pages/Auth/LoginPage';
import RegisterPage from './Pages/Auth/RegisterPage';
import TrainerCoursesPage from './Pages/trainer/TrainerCoursesPage';
// import LoginPage from "./Pages/Auth/LoginPage";
import AdminCoursesPage from './Pages/admin/AdminCoursesPage'
import AdminCourseDetails from './Pages/admin/AdminCourseDetails';
import AdminDashboard from './Pages/admin/AdminDashboard';
import AdminUsers from './Pages/admin/AdminUsers';
import NotFoundPage from './Pages/NotFoundPage'


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/trainee" element={<TraineeLayout />}>

        </Route>

        <Route path="/trainer" element={<TrainerLayout />}>
          <Route path='/trainer/courses/:id' element={<CreateCoursePage />} />
          <Route path='/trainer/courses' element={<TrainerCoursesPage />} />
          <Route path="/trainer" element={<Navigate to="/trainer/courses" replace />} />

        </Route>

        <Route path="/admin" element={<AdminLayout />}>
          <Route path='/admin/dashboard' element={<AdminDashboard />} />
          <Route path='/admin/courses/:id' element={<AdminCourseDetails />} />
          <Route path='/admin/courses' element={<AdminCoursesPage />} />
          <Route path='/admin/users' element={<AdminUsers />} />
          {/* <Route path='/admin/users/:id' element={<AdminCoursesPage />} /> */}
          <Route path="/admin" element={<Navigate to="/admin/dashboard" replace />} />
        </Route>
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
      <Toaster />
    </BrowserRouter>
  );
}

export default App;
