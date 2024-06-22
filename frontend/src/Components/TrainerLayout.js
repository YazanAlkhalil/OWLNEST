import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

const TrainerLayout = () => {
  return (
    <div className="grid grid-cols-6 h-screen">
      <Sidebar   links={[
        { name: "courses", url: "/trainer/courses" },
        { name: "inprogress", url: "/trainer/inprogress" },
      ]} />
      <div className="h-screen col-span-5 overflow-auto flex flex-col grow-[24]">
        <Navbar highlight='trainer' />
        <main className="flex-1 p-8 overflow-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
export default TrainerLayout;
