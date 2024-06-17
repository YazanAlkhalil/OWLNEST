import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

const TrainerLayout = () => {
  return (
    <div className="flex flex-1 ">
      <Sidebar  links={[
        { name: "courses", url: "/trainee/courses" },
        { name: "inprogress", url: "/trainee/inprogress" },
      ]} />
      <div className="h-screen overflow-auto flex flex-col grow-[24]">
        <Navbar highlight='trainer' />
        <main className="flex-1 p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
export default TrainerLayout;
