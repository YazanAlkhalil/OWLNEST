import axios from 'axios'
import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

export default function UseFetch() {
    const navigate = useNavigate();
    const [resData,setResData] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

        const fetchData = async ({url,reqData,params}) => {
        try {
            console.log("h");
            const response = await axios.post(url, reqData, {
                withCredentials: true,
                params:params
            });
            if(response.status === 401){
               try{
                console.log("h");
                const response = await axios.post("http://127.0.0.1:8000/api/refresh/",{
                    withCredentials: true,
                    headers: { "Content-Type": "application/json" }
                });
                if(response.status === 403){
                    console.log("h");
                    navigate("/",{replace : true})
                }else if(response.status === 201){
                    console.log("h");
                    const response = await axios.post(url, reqData, {
                        withCredentials: true,
                        headers: { "Content-Type": "application/json" },
                        params:params
                    });
                    let res = response.data;
                    setResData(res);
                }
               }catch(e){
                console.log(e);
                navigate('/',{replace: true})
               }
            }else if(response.status === 201){
                console.log("h");
                let res = await response.data;
                setResData(res);
            }else if(response.status === 200){
                console.log("h");
                let res = await response.data;
                setResData(res);
            }
        }catch(e){
            console.log(e);
            setError(e);
        }finally{
            setLoading(false)
        }
    }
    return { fetchData, resData, loading, error };
}