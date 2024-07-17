import axios from "axios";
import { useState } from "react";
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
    setLoading(true);
    setError(null);
    try {
      let response;
      if (method === "post") {
        response = await axios.post(url, reqData, { withCredentials: true, headers ,params });
      } else if (method === "get") {
        response = await axios.get(url, { withCredentials: true, params,headers });
      } else if (method === "delete") {
        response = await axios.delete(url, { withCredentials: true, params ,headers});
      } else {
        response = await axios.patch(url, reqData, { withCredentials: true, params ,headers});
      }
      let res = response.data;
      setResData(res);
    } catch (error) {
      if (error.response && error.response.status === 401) {
        try {
          const refreshResponse = await axios.post("http://127.0.0.1:8000/api/refresh/", {}, { withCredentials: true });
          if (refreshResponse.status === 200) {
            const retryResponse = await axios.post(url, reqData);
            let res = retryResponse.data;
            setResData(res);
          } else {
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
        setError(error);
      }
    } finally {
      setLoading(false);
    }
  };

  return { fetchData, resData, loading, error };
}
