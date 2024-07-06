import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import Cookies from 'js-cookie';
import { jwtDecode } from 'jwt-decode';
// import axiosInstance from "../../Components/AxiosSetup";

const decodeToken = (token) => jwtDecode(token);

const isTokenExpired = (token) => {
    const decoded = decodeToken(token);
    return decoded.exp * 1000 < Date.now();
};

export const loginUser = createAsyncThunk(
    'loginUser',
    async (data, { rejectWithValue }) => {
        try {
            const link = "http://127.0.0.1:8000/api/login/";
            const response = await axios.post(link, data, {
                headers: { "Content-Type": "application/json" }
            });
            const res = response.data;
            if (response.status === 200) {
                console.log("login successfully", res);
                const { accessToken, refreshToken } = response.data;
                Cookies.set('accessToken', accessToken);
                Cookies.set('refreshToken', refreshToken);
                return res;
            } else {
                console.log("login Failed:", res);
                return rejectWithValue(res);
            }
        } catch (error) {
            return rejectWithValue(error.response.data);
        }
    }
);

export const refreshAccessToken = createAsyncThunk(
    'refreshAccessToken',
    async (_, { rejectWithValue }) => {
        try {
            const link = "http://127.0.0.1:8000/api/refresh/";
            const refreshToken = Cookies.get('refreshToken');
            if (!refreshToken || isTokenExpired(refreshToken)) {
                Cookies.remove('accessToken');
                Cookies.remove('refreshToken');
                throw new Error('Refresh token expired');
            }
            const response = await axios.post(link, { refreshToken: refreshToken });
            const { accessToken } = response.data;
            Cookies.set('accessToken', accessToken);
            return accessToken;
        } catch (error) {
            Cookies.remove('accessToken');
            Cookies.remove('refreshToken');
            return rejectWithValue(error.response.data);
        }
    }
);

export const LoginSlice = createSlice({
    name: "login",
    initialState: {
        accessToken: Cookies.get('accessToken') || null,
        refreshToken: Cookies.get('refreshToken') || null,
        isFetching: false,
        isSuccess: false,
        error: null,
    },
    reducers : {
        logout: (state) => {
            Cookies.remove('accessToken');
            Cookies.remove('refreshToken');
            state.accessToken = null;
            state.refreshToken = null;
        }
    },
    extraReducers: (builder) => {
        builder
            .addCase(loginUser.fulfilled, (state, action) => {
                state.isSuccess = true;
                state.accessToken = action.payload.accessToken;
                state.refreshToken = action.payload.refreshToken;
                state.isFetching = false;
                state.error = null;
            })
            .addCase(loginUser.pending, (state) => {
                state.isFetching = true;
                state.error = null;
            })
            .addCase(loginUser.rejected, (state, action) => {
                state.isFetching = false;
                state.isSuccess = false;
                state.error = action.payload;
            })
            .addCase(refreshAccessToken.fulfilled, (state, action) => {
                state.accessToken = action.payload;
            })
            .addMatcher(
                (action) => action.type.endsWith('/rejected'),
                (state, action) => {
                    state.error = action.payload;
                }
            );
    }
});

export const { logout } = LoginSlice.actions;

export const loginSelector = (state) => state.login;
export default LoginSlice.reducer;
