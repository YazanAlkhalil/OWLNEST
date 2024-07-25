import image from "../images/logo.png";
import { NavLink } from "react-router-dom";

function Sidebar({ links }) {

  return (
    <div className="col-span-1 flex flex-col items-center text-background flex-grow dark:bg-DarkGray bg-primary flex-shrink-0">
      <img className="box-border pt-4 w-[50%] mb-5 max-h-60" src={image} />
      <ul className='px-4 flex flex-col'>
        {links.map((link) => (
          <NavLink
            to={link.url}
            relative="path"
            className={`text-3xl relative mb-10 flex items-center`}
            key={link.name}

          >
            {({ isActive }) => (
              <>
                {isActive && (
                  <svg className="absolute -left-10" width="54" height="53" viewBox="0 0 54 53" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g filter="url(#filter0_d_403_266)">
                      <path d="M21.2007 21.0526C31.6686 23.4737 34.1111 30.9426 36.5304 37.2011L34.3321 38L33.2272 35.2158C32.6689 35.4216 32.0873 35.5789 31.6686 35.5789C18.8745 35.5789 15.3851 15 15.3851 15C16.5482 17.4211 24.69 17.7237 30.5055 18.9342C36.321 20.1447 38.6472 25.2895 38.6472 27.7105C38.6472 30.1316 36.6118 32.25 36.6118 32.25C32.8317 21.0526 21.2007 21.0526 21.2007 21.0526Z" fill="#DEA01E" />
                    </g>
                    <defs>
                      <filter id="filter0_d_403_266" x="0.385254" y="0" width="53.262" height="53" filterUnits="userSpaceOnUse" colorInterpolationFilters="sRGB">
                        <feFlood floodOpacity="0" result="BackgroundImageFix" />
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha" />
                        <feOffset />
                        <feGaussianBlur stdDeviation="7.5" />
                        <feComposite in2="hardAlpha" operator="out" />
                        <feColorMatrix type="matrix" values="0 0 0 0 0.870588 0 0 0 0 0.627451 0 0 0 0 0.117647 0 0 0 1 0" />
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_403_266" />
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_403_266" result="shape" />
                      </filter>
                    </defs>
                  </svg>
                )}
            <span>{link.name}</span>
              </>
            )}

          </NavLink>
        ))}
      </ul>
    </div>
  );
}

export default Sidebar;
