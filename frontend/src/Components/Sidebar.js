import image from "../images/OIG2 3.png";

function Sidebar({ links }) {
  return (
    <div className="tw-flex tw-flex-col tw-items-center tw-text-background  tw-flex-grow tw-bg-primary">
      <img className="tw-box-border tw-w-[90%] tw-max-h-60" src={image} />
      <ul className='tw-px-4'>
        {links.map((link) => (
          <li className="tw-text-3xl tw-mb-10" key={link.name}>
            <a href={link.url}>{link.name}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Sidebar;
