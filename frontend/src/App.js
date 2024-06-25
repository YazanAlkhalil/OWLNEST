import { BrowserRouter,
  //  Routes, Route, Navigate 
  } 
   from 'react-router-dom';
// import RegisterPage from './Pages/Auth/RegisterPage';
import Router from './Router';
// import CreateCoursePage from './Pages/trainer/CreateCoursePage';
import { Toaster } from 'react-hot-toast';
// import TrainerLayout from './Components/TrainerLayout';
// import TraineeLayout from './Components/TraineeLayout'
// import AdminLayout from './Components/AdminLayout';
// import LoginPage from './Pages/Auth/LoginPage';
// import RegisterPage from './Pages/Auth/RegisterPage';
// import TrainerCoursesPage from './Pages/trainer/TrainerCoursesPage';
// import LoginPage from "./Pages/Auth/LoginPage";
// import AdminCoursesPage from './Pages/admin/AdminCoursesPage'
// import AdminCourseDetails from './Pages/admin/AdminCourseDetails';
// import AdminDashboard from './Pages/admin/AdminDashboard';
// import AdminUsers from './Pages/admin/AdminUsers';
// import NotFoundPage from './Pages/NotFoundPage'


function App() {
  return (
    <BrowserRouter>
      <Router />
      <Toaster />
    </BrowserRouter>
  );
}

export default App;
