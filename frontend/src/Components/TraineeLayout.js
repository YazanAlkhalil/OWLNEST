import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import { useState } from "react";
import { useSelector } from "react-redux";

const TraineeLayout = () => {
  // const [sid,setSid] = useState(false);
  const value = useSelector(state => state.clickCourse.value); 
  return (
    <div className="grid grid-cols-6 ">
      {!value ? <Sidebar  links={[
        { name: "Homepage", url: "/trainee/homepage" },
        { name: "Courses", url: "/trainee/courses" },
        { name: "Favorites", url: "/trainee/favorites" },
        { name: "Certifications", url: "/trainee/certifications" },
      ]} /> :
      <Sidebar  links={[
        { name: "Content", url: "/trainee/courses/content" },
        { name: "Progress", url: "/trainee/courses/progress" },
        { name: "Discussin", url: "/trainee/courses/discussion" },
        { name: "Info", url: "/trainee/courses/Info" },
      ]} />}
      <div className="h-screen col-span-5 flex flex-col grow-[24]">
        <Navbar highlight='trainee'/>
        <main className="flex-1 p-8 overflow-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
export default TraineeLayout;
