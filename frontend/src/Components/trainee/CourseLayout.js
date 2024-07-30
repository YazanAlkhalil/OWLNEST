import { Outlet, useLocation, useNavigate, useParams } from "react-router-dom";
import Sidebar from "../Sidebar";
import NavBar from "../Navbar";
import { useEffect } from "react";



const CourseLayout = () => {
  const navigate = useNavigate();
  const { id } = useParams();
  const location = useLocation();

  useEffect(() => {
    if (location.pathname === `/trainee/courses/${id}`) {
      navigate(`/trainee/courses/${id}/content`, { replace: true });
    }
  }, [id, location.pathname, navigate]);

 
  return (
    <div className="grid grid-cols-6 ">
      <Sidebar  links={[
        { name: "Content", url: `/trainee/courses/${id}/content` },
        { name: "Progress", url: `/trainee/courses/${id}/progress` },
        { name: "Discussin", url: `/trainee/courses/${id}/discussion` },
        { name: "Info", url: `/trainee/courses/${id}/Info` },
      ]} />
      <div className="h-screen dark:bg-Gray dark:text-white col-span-5 flex flex-col grow-[24]">
        <NavBar highlight='trainee'/>
        <main className="flex-1 p-8 overflow-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
export default CourseLayout;
