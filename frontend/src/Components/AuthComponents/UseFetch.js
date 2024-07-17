import axios from "axios";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

export default function UseFetch() {
  const navigate = useNavigate();
  const [resData, setResData] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = async (
   { 
    url,
    reqData,
    method = "post",
    params = {},
    headers = {}
    }
  ) => {
    try {
      console.log("ssss");
      console.log(reqData);
      if (method === "post") {
        const response = await axios.post(
          url,
          reqData,
          {
            withCredentials: true,
            headers: headers
          }
        );
        let res = response.data;
        setResData(res);
      } else if (method === "get") {
        const response = await axios.get(url, {
            withCredentials: true,
            params
         });
        let res = response.data;
        setResData(res);
      } else if (method === "delete") {
        const response = await axios.delete(url, {
            withCredentials: true,
            params });
        let res = response.data;
        setResData(res);
      } else {
        const response = await axios.patch(url, reqData, {
            withCredentials: true,
            params });
        let res = response.data;
        setResData(res);
      }
    } catch (error) {
      console.log(error.response, "asd");
      if (error.response) {
        if (error.response.status === 401) {
          try {
            const refreshResponse = await axios.post(
              "http://127.0.0.1:8000/api/refresh/",
              {},
              {
                withCredentials: true,
                headers: { "Content-Type": "application/json" },
              }
            );
            if (refreshResponse.status === 200) {
              const retryResponse = await axios.post(
                "http://127.0.0.1:8000/api/create_company/",
                reqData
              );
              let res = retryResponse.data;
              setResData(res);
            } else {
              console.log("Unexpected response from refresh endpoint");
              navigate("/", { replace: true });
            }
          } catch (refreshError) {
            if (refreshError.response && refreshError.response.status === 403) {
              console.log("Refresh token expired");
              navigate("/", { replace: true });
            } else {
              console.log("Error refreshing token:", refreshError);
              navigate("/", { replace: true });
            }
          }
        } else {
          console.log("Error status:", error.response.status);
          setError(error);
        }
      } else if (error.request) {
        console.log("No response received:", error.request);
        setError(error);
      } else {
        console.log("Error", error.message);
        setError(error);
      }
    } finally {
      setLoading(false);
    }
  };
  return { fetchData, resData, loading, error };
}
