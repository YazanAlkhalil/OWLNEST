import { BrowserRouter,Routes,Route } from 'react-router-dom';
// import RegisterPage from './Pages/Auth/RegisterPage';
import Router from './Router';
import CreateCoursePage from './Pages/trainer/CreateCoursePage';
import { Toaster } from 'react-hot-toast';
import TrainerLayout from './Components/TrainerLayout';
import TraineeLayout from './Components/TraineeLayout'
import AdminLayout from './Components/AdminLayout';
// import LoginPage from "./Pages/Auth/LoginPage";


function App() {
  return (
      <BrowserRouter>
        <Routes>
          <Route path="/trainee" element={<TraineeLayout />}>

          </Route>

          <Route path="/trainer" element={<TrainerLayout />}>
            <Route index path='/trainer/' element={<CreateCoursePage />} />
          </Route>

          <Route path="/admin" element={<AdminLayout />}>

          </Route>
        </Routes>
        <Toaster />
      </BrowserRouter>
    // <LoginPage />
  );
}

export default App;
