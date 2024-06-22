import image from "../images/logo.png";
import { NavLink } from "react-router-dom";

function Sidebar({ links }) {

  return (
    <div className="col-span-1 flex flex-col items-center text-background  flex-grow bg-primary flex-shrink-0">
      <img className="box-border pt-4 w-[70%] mb-5 max-h-60" src={image} />
      <ul className='px-4 flex flex-col'>
        {links.map((link) => (
          <NavLink to={link.url} relative="path" className="text-3xl mb-10" key={link.name}>
            {link.name}
          </NavLink>
        ))}
      </ul>
    </div>
  );
}

export default Sidebar;
