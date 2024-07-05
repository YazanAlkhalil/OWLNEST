import axios from 'axios';
import Cookies from 'js-cookie';
import { jwtDecode } from 'jwt-decode';
import { logout, refreshAccessToken } from '../features/Auth/LoginSlice';
import store from '../features/Store';


const API_URL = 'http://127.0.0.1:8000/api';

const isTokenExpired = (token) => {
    const decoded = jwtDecode(token);
    return decoded.exp * 1000 < Date.now();
};

const axiosInstance = axios.create({
    baseURL: API_URL,
});

axiosInstance.interceptors.request.use(
    async (config) => {
        let accessToken = Cookies.get('accessToken');
        if (accessToken && isTokenExpired(accessToken)) {
            try {
                const actionResult = await store.dispatch(refreshAccessToken());
                const newAccessToken = actionResult.payload;
                accessToken = newAccessToken;
            } catch (error) {
                store.dispatch(logout());
                throw new Error('Session expired. Please log in again.');
            }
        }
        if (accessToken) {
            config.headers['Authorization'] = `Bearer ${accessToken}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export default axiosInstance;
