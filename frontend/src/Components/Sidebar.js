import image from "../images/logo.png";

function Sidebar({ links }) {
  return (
    <div className="flex flex-col items-center text-background  flex-grow bg-primary">
      <img className="box-border pt-4 w-[70%] mb-5 max-h-60" src={image} />
      <ul className='px-4'>
        {links.map((link) => (
          <li className="text-3xl mb-10" key={link.name}>
            <a href={link.url}>{link.name}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Sidebar;
