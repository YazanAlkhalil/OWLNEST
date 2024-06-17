import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

const TraineeLayout = () => {
  return (
    <div className="tw-flex tw-flex-1 ">
      <Sidebar  links={[
        { name: "homepage", url: "/trainee/homepage" },
        { name: "courses", url: "/trainee/courses" },
        { name: "favorites", url: "/trainee/favorites" },
        { name: "certifications", url: "/trainee/certifications" },
      ]} />
      <div className="tw-h-screen tw-flex tw-flex-col tw-grow-[24]">
        <Navbar highlight='trainee'/>
        <main className="tw-flex-1 tw-p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
export default TraineeLayout;
