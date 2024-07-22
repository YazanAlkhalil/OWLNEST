import { Outlet } from "react-router-dom";
import Sidebar from "../Sidebar";
import NavBar from "../Navbar";



const CourseLayout = () => {
 
  return (
    <div className="grid grid-cols-6 ">
      <Sidebar  links={[
        { name: "Content", url: "/trainee/courses/:id/content" },
        { name: "Progress", url: "/trainee/courses/:id/progress" },
        { name: "Discussin", url: "/trainee/courses/:id/discussion" },
        { name: "Info", url: "/trainee/courses/:id/Info" },
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
