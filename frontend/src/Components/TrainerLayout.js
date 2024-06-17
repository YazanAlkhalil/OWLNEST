import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

const TrainerLayout = () => {
  return (
    <div className="tw-flex tw-flex-1 ">
      <Sidebar  links={[
        { name: "courses", url: "/trainee/courses" },
        { name: "inprogress", url: "/trainee/inprogress" },
      ]} />
      <div className="tw-h-screen tw-overflow-auto tw-flex tw-flex-col tw-grow-[24]">
        <Navbar highlight='trainer' />
        <main className="tw-flex-1 tw-p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
export default TrainerLayout;
