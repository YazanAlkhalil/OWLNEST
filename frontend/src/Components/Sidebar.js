import { NavLink } from "react-router-dom";
import image from "../images/OIG2 3.png";

function Sidebar({ links }) {

  return (
    <div className="col-span-1 flex flex-col items-center text-background  flex-grow bg-primary flex-shrink-0">
      <img className="box-border w-[90%] max-h-60" src={image} />
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
