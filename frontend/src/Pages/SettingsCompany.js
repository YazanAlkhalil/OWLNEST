import React, { useEffect, useState } from "react";
import logo from "../images/simple-user-default-icon-free-png.webp";
import useFetch from "../Components/AuthComponents/UseFetch";
import {
  Box,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  TextField,
  Typography,
  IconButton,
  Button,
} from "@mui/material";

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

const BASE_URL = "http://127.0.0.1:8000";

export default function SettingsCompany() {
  const [photo, setPhoto] = useState({
    send: null, 
    current: logo,
  });
  const { fetchData } = useFetch();
  const [userData, setUserData] = useState({
    name: "",
    email: "",
    phone: "",
    location: "",
    country: "",
    size: "",
    description : ""
  });
  const [disable, setDisable] = useState(false);

  const handlePhotoChange = (e) => {
    setDisable(true);
    const file = e.target.files[0];
    setPhoto({
      send: file,
      current: URL.createObjectURL(file) || logo,
    });
  };

  useEffect(() => {
    async function getUserData() {
      const res = await fetchData({
        url: "http://127.0.0.1:8000/api/company/",
        method: "get",
      });
      console.log(res);

      if (res) {
        setUserData({
          name: res.name || "",
          email: res.email || "",
          phone: res.phone || "",
          location: res.location || "",
          country: res.country || "",
          size: res.size || "",
          description : res.description
        });
        if (res.logo) {
          setPhoto({
            send: null, // no file selected yet
            current: `${BASE_URL}${res.logo}`,
          });
        }
      }
    }
    getUserData();
  }, [fetchData]);

  const handleButtonClick = () => {
    document.getElementById("photo-input").click();
  };

  const handleChange = (e) => {
    setDisable(true);
    const { name, value } = e.target;
    setUserData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };


  const handleOnClick = async () => {
    const formData = new FormData();

    formData.append("name", userData.name);
    formData.append("email", userData.email);
    formData.append("phone", userData.phone);
    formData.append("location", userData.location);
    formData.append("country", userData.country);
    formData.append("size", userData.size);
    formData.append("description", userData.description);

    if (photo.send) {
      formData.append("logo", photo.send);
    }


    const res = await fetchData({
      url: "http://127.0.0.1:8000/api/edit_company/",
      method: "patch",
      data: formData,
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    console.log(res);
  };

  return (
    <Box p={2} >
      <Typography variant="h4" gutterBottom>
        Edit Your Company Details
      </Typography>
      <div className="w-[75%] p-8 rounded mx-auto bg-slate-700">
      <div className="text-center">
      <Box position="relative" display="inline-block">
        <img
          src={photo.current}
          alt="ProfilePhoto"
          style={{ width: 96, height: 96, borderRadius: "50%", border: "1px solid white" }}
        />
        <input
          id="photo-input"
          type="file"
          accept="image/*"
          style={{ display: "none" }}
          onChange={handlePhotoChange}
        />
        <IconButton
          onClick={handleButtonClick}
          style={{
            position: "absolute",
            bottom: 0,
            right: 0,
            backgroundColor: "white",
            padding: 4,
            borderRadius: "50%",
            border: "1px solid gray",
          }}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            width="16"
            height="16"
            fill="currentColor"
            style={{ color: "gray" }}
          >
            <path d="M0 0h24v24H0z" fill="none" />
            <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zm2.92 1.92l.85-.85 2.67 2.67-.85.85H5.92zm3.3-3.3l2.67 2.67 8.5-8.5-2.67-2.67-8.5 8.5z" />
          </svg>
        </IconButton>
      </Box>
      </div>
      <Box mt={2}>
        <TextField
          label="name"
          name="name"
          value={userData.name}
          onChange={handleChange}
          fullWidth
          variant="outlined"
          margin="normal"
        />
        <TextField
          label="Location"
          name="location"
          value={userData.location}
          onChange={handleChange}
          fullWidth
          variant="outlined"
          margin="normal"
        />
        <TextField
          label="Email"
          name="email"
          value={userData.email}
          onChange={handleChange}
          fullWidth
          variant="outlined"
          margin="normal"
        />
        <TextField
          label="Phone"
          name="phone"
          value={userData.phone}
          onChange={handleChange}
          fullWidth
          variant="outlined"
          margin="normal"
        />
        <TextField
          label="Description"
          name="description"
          value={userData.description}
          onChange={handleChange}
          fullWidth
          variant="outlined"
          InputLabelProps={{ shrink: true }}
          margin="normal"
        />
        <FormControl fullWidth variant="outlined" margin="normal">
          <InputLabel>Country</InputLabel>
          <Select
            name="country"
            value={userData.country}
            onChange={handleChange}
            label="Country"
          >
            {countries.map(([code, name]) => (
              <MenuItem key={code} value={code}>
                {name}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
        <FormControl fullWidth variant="outlined" margin="normal">
          <InputLabel>Size</InputLabel>
          <Select
            name="size"
            value={userData.size}
            onChange={handleChange}
            label="Size"
          >
            <MenuItem value="L">Large</MenuItem>
            <MenuItem value="M">Medium</MenuItem>
            <MenuItem value="S">Small</MenuItem>
          </Select>
        </FormControl>
       <div className="flex justify-end mt-5">
       <Button disabled={!disable} onClick={handleOnClick} size="large" variant="contained">Save</Button>
       </div>
      </Box>
      </div>
    </Box>
  );
} 
