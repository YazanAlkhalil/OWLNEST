import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

const AdminLayout = () => {
  return (
    <div className="flex flex-1 ">
      <Sidebar  links={[
        { name: "home", url: "/trainee/home" },
        { name: "courses", url: "/trainee/courses" },
        { name: "users", url: "/trainee/inprogress" },
      ]} />
      <div className="h-screen flex flex-col grow-[24]">
        <Navbar highlight='admin'/>
        <main className="flex-1 p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
export default AdminLayout;
