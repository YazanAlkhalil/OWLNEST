import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

const TraineeLayout = () => {
  return (
    <div className="grid grid-cols-6 ">
      <Sidebar  links={[
        { name: "homepage", url: "/trainee/homepage" },
        { name: "courses", url: "/trainee/courses" },
        { name: "favorites", url: "/trainee/favorites" },
        { name: "certifications", url: "/trainee/certifications" },
      ]} />
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
