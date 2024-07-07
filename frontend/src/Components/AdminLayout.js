import { Outlet } from "react-router-dom";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

const AdminLayout = () => {
  return (
    <div className="grid grid-cols-6">
      <Sidebar  links={[
        { name: "home", url: "/admin/dashboard" },
        { name: "courses", url: "/admin/courses" },
        { name: "users", url: "/admin/users" },
      ]} />
      <div className="h-screen col-span-5 flex flex-col grow-[24]">
        <Navbar highlight='admin'/>
        <main className="flex-1 p-8 overflow-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
export default AdminLayout;
