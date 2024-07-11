import React, { useState } from "react";
import "./CompanyDetails.css";
import uploadImg from "../../images/add_photo_alternate_outlined.png";
import backGround from "../../images/—Pngtree—e-learning education online illustration_6548963.png";
import { useNavigate } from "react-router-dom";
<<<<<<< HEAD
import { useDispatch } from "react-redux";
import { newCompany } from "../../features/Auth/CompanySlice";
import UseFetch from "./UseFetch";


const countries = [
  ["DZ", "Algeria"],
  ["BH", "Bahrain"],
  ["EG", "Egypt"],
  ["IQ", "Iraq"],
  ["JO", "Jordan"],
  ["KW", "Kuwait"],
  ["LB", "Lebanon"],
  ["LY", "Libya"],
  ["MR", "Mauritania"],
  ["MA", "Morocco"],
  ["OM", "Oman"],
  ["PS", "Palestine"],
  ["QA", "Qatar"],
  ["SA", "Saudi Arabia"],
  ["SD", "Sudan"],
  ["SY", "Syria"],
  ["TN", "Tunisia"],
  ["AE", "United Arab Emirates"],
  ["YE", "Yemen"],
];



export default function CompanyDetails() {
  // const navigate = useNavigate();
  // const dispatch = useDispatch();
  const { fetchData, resData, loading, error } = UseFetch();
  const [compName, setCompName] = useState("");
  const [compEmail, setCompEmail] = useState("");
  const [logo,setLogo] = useState('');
=======

export default function CompanyDetails() {
  const navigate = useNavigate();
  const [compName, setCompName] = useState("");
  const [compEmail, setCompEmail] = useState("");
  // const [logo,setLogo] = useState('');
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
  const [country, setCountry] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [location, setLocation] = useState("");
  const [size, setSize] = useState(0);
  const [desc, setDesc] = useState("");
  const [errors, setErrors] = useState({});

<<<<<<< HEAD
  function handleLogo(e) {
    console.log(e.target.files);
    setLogo(URL.createObjectURL(e.target.files[0]));
}
=======
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
  const validateEmail = (email) => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  };

  const validateForm = () => {
    const newErrors = {};

    if (!compName) newErrors.compName = true;
    if (!compEmail) {
      newErrors.compEmail = true;
    } else if (!validateEmail(compEmail)) {
      newErrors.compEmail = true;
    }
    if (!country) newErrors.country = true;
    if (!location) newErrors.location = true;
    if (!desc) newErrors.desc = true;
    if (!size) newErrors.size = true;
    if (!phoneNumber) newErrors.phoneNumber = true;

    setErrors(newErrors);

    return Object.keys(newErrors).length === 0;
  };

  const handleCreateNestClick = (e) => {
    e.preventDefault();
<<<<<<< HEAD
    

    const data = {
      name : compName,
      email: compEmail,
      logo : logo,
      country: country,
      location: location,
      size: size,
      description: desc,
      phone : phoneNumber
    }
    console.log(data);
    if (validateForm()) {
      // console.log(fetchData);
      // dispatch(newCompany(data));
     fetchData({url: "http://127.0.0.1:8000/api/create_company/",reqData: data,params: {}})
    //  fetchData({url: "http://127.0.0.1:8000/api/user/",reqData: {},params: {}})

=======
    if (validateForm()) {
      navigate('/trainee',{replace: true});
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
    }
  };

  const getInputClass = (field) =>
    errors[field] ? "border border-red-500" : "";

  return (
    <>
      <div className="companyDetails">
        <div className="flex flex-wrap ">
          <div className="w-1/2">
            <div className="container mx-auto sm:px-4">
              <div className="login-form text-center">
                <h4 className="font-semibold text-xl mb-4">
                  Please Enter Company Details
                </h4>
                <form onSubmit={handleCreateNestClick}>
                  <div className="mb-4">
                    <input
                      type="text"
                      id="companyName"
                      placeholder="Company Name"
                      value={compName}
                      onChange={(e) => setCompName(e.target.value)}
                      className={` ${getInputClass("compName")}`}
                
                    />
                  </div>
                  <div className="mb-4">
                    <input
                      type="email"
                      id="companyemail"
                      placeholder="Company Email"
                      value={compEmail}
                      onChange={(e) => setCompEmail(e.target.value)}
                      className={` ${getInputClass("compEmail")}`}
                
                    />
                  </div>
                  <div className="mb-4">
                    <div className="file-upload">
                      <img src={uploadImg} alt="upload" className="mx-auto" />
                      <h6 className="fw-bold">Click box to upload LOGO</h6>
<<<<<<< HEAD
                      <input type="file" multiple accept="image/*" onChange={handleLogo} />
=======
                      <input type="file" multiple accept="image/*" />
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
                    </div>
                  </div>
                  <div className="mb-4 size flex justify-center">
                    <select
                      name="country"
                      id="select-box"
                      value={country}
                      onChange={(e) => setCountry(e.target.value)}
                      className={` ${getInputClass("country")}`}
<<<<<<< HEAD
                      >
                      {countries.map(([code, name]) => (
                              <option key={code} value={code}>
                                {name}
                              </option>
                      ))}
=======
                >
                      <option value="USA">USA</option>
                      <option value="Three">Three</option>
                      <option value="Four">Four</option>
                      <option value="Five">Five</option>
                      <option value="Six">Six</option>
                      <option value="Seven">Seven</option>
                      <option value="Eight">Eight</option>
                      <option value="Nine">Nine</option>
                      <option value="Ten">Ten</option>
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
                    </select>
                    <input
                      type="text"
                      id="location"
                      placeholder="Location"
                      value={location}
                      onChange={(e) => setLocation(e.target.value)}
                      className={` ${getInputClass("location")}`}
                
                    />
                  </div>
                  <div className="mb-4">
                    <input
                      type="text"
                      id="description"
                      placeholder="Description"
                      value={desc}
                      onChange={(e) => setDesc(e.target.value)}
                      className={` ${getInputClass("desc")}`}
                
                    />
                  </div>
                  <div className="mb-4 size flex justify-center">
                    <select
                      name="size"
                      id="select-box"
                      value={size}
                      onChange={(e) => setSize(e.target.value)}
                      className={` ${getInputClass("size")}`}
<<<<<<< HEAD
                    >
                      <option value="L">Large</option>
                      <option value="M">Medium</option>
                      <option value="S">Small</option>
=======
                >
                      <option value="100">100</option>
                      <option value="200">200</option>
                      <option value="300">300</option>
                      <option value="400">400</option>
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
                    </select>
                    <input
                      type="number"
                      id="number"
                      placeholder="Phone Number"
                      value={phoneNumber}
                      onChange={(e) => setPhoneNumber(e.target.value)}
                      className={` ${getInputClass("phoneNumber")}`}
                
                    />
                  </div>
                  <button
                    type="submit"
                    className="inline-block text-white font-bold align-middle  select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline bg-gray-100 text-gray-800 hover:bg-gray-200 fw-bold text-gray-100">
                    Create NEST
                  </button>
                </form>
              </div>
            </div>
          </div>
          <div className="w-1/2 loginBackGround">
            <div>
              <img
                src={backGround}
                className="mx-auto"
                alt="error"
                width={"500px"}
                height={"500px"}
              />
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
