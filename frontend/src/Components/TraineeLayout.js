import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

const TraineeLayout = () => {
  return (
    <div className="flex flex-1 ">
      <Sidebar  links={[
        { name: "homepage", url: "/trainee/homepage" },
        { name: "courses", url: "/trainee/courses" },
        { name: "favorites", url: "/trainee/favorites" },
        { name: "certifications", url: "/trainee/certifications" },
      ]} />
      <div className="h-screen flex flex-col grow-[24]">
        <Navbar highlight='trainee'/>
        <main className="flex-1 p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
export default TraineeLayout;
