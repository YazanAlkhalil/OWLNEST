import React, { useState } from "react";
import "./CompanyDetails.css";
import uploadImg from "../../images/add_photo_alternate_outlined.png";

export default function CompanyDetails() {

  const [compName,setCompName] = useState('');
  const [compEmail,setCompEmail] = useState('');
  // const [logo,setLogo] = useState('');
  const [country,setCountry] = useState('USA');
  const [phoneNumber,setPhoneNumber] = useState('');
  const [location,setLocation] = useState('');
  const [size,setSize] = useState(0);
  const [desc,setDesc] = useState('');

  function handleCreateNestClick(e){
    e.preventDefault();
    console.log("Company Details: ",compName,compEmail,country,phoneNumber,location,size,desc);
  }
  
  return (
    <>
      <div className="companyDetails">
        <div className="row">
          <div className="col-6">
            <div className="container">
              <div className="login-form text-center">
                <h4 className="fw-bold mb-4">
                  Please Enter Company Details 😉
                </h4>
                <form onSubmit={handleCreateNestClick}>
                  <div className="form-group mb-3">
                    <input
                      type="text"
                      id="companyName"
                      placeholder="Company Name"
                      value={compName}
                      onChange={(e) => setCompName(e.target.value)}
                      required
                    />
                  </div>
                  <div className="form-group mb-3">
                    <input
                      type="email"
                      id="companyemail"
                      placeholder="Company Email"
                      value={compEmail}
                      onChange={(e) => setCompEmail(e.target.value)}
                      required
                    />
                  </div>
                  <div className="form-group mb-3">
                    <div className="file-upload">
                      <img src={uploadImg} alt="upload" />
                      <h6 className="fw-bold">Click box to upload LOGO</h6>
                      <input type="file" multiple accept="image/*" />
                    </div>
                  </div>
                  <div className="form-group size  d-flex justify-content-center mb-3">
                  <select
                            name="country"
                            id="select-box"
                            value={country} 
                            onChange={(e)=> setCountry(e.target.value)} 
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
                          </select>
                      <input
                        type="text"
                        id="location"
                        placeholder="Location"
                        value={location}
                        onChange={(e) => setLocation(e.target.value)}
                        required
                      />
                    </div>
                  <div className="form-group mb-3">
                    <input
                      type="number"
                      id="number"
                      placeholder="Phone Number"
                      value={phoneNumber}
                      onChange={(e) => setPhoneNumber(e.target.value)}
                      required
                    />
                  </div>
                  <div className="form-group size d-flex justify-content-center mb-3">
                  <select
                            name="size"
                            id="select-box"
                            value={size} 
                            onChange={(e)=> setSize(e.target.value)} 
                            >
                            <option value="100">100</option>
                            <option value="200">200</option>
                            <option value="300">300</option>
                            <option value="400">400</option>
                          </select>
                    <input
                      type="text"
                      id="description"
                      placeholder="Description"
                      value={desc}
                      onChange={(e) => setDesc(e.target.value)}
                      required
                    />
                  </div>
                  <button
                    type="submit"
                    className="btn btn-light fw-bold text-light">
                    Create NEST
                  </button>
                </form>
              </div>
            </div>
          </div>
          <div className="col-6 loginBackGround text-center">
            <div>
              <h1 className="text-light">
                WELCOME IN OUR OWL NEST WEBSITE 😁
              </h1>
              <img  alt="error" width={'350px'} height={'350px'} />
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
