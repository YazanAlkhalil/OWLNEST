
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import Cookies from 'js-cookie';

export const loginUser = createAsyncThunk(
    "login",
    async (data, thunkAPI) => {
        try {
            let loginUrl = "http://127.0.0.1:8000/api/login/";
            const response = await axios.post(loginUrl, data, {
                withCredentials: true,
                headers: { "Content-Type": "application/json" }
            });
            let res = await response.data;
            if (response.status === 200) {
                console.log(res);
            } else {
                return thunkAPI.rejectWithValue(res);
            }
        } catch (e) {
            console.log("Error", e.response.data);
            return thunkAPI.rejectWithValue(e.response.data);
        }
        
    }
);
export const logout = createAsyncThunk(
    "logout",
    async (_, thunkAPI) => {
        try {
            let logoutUrl = "http://127.0.0.1:8000/api/logout/";
            const response = await axios.post(logoutUrl,{},{
                withCredentials: true,
                headers: { "Content-Type": "application/json" }
            });
            let res = await response.data;
            if (response.status === 200) {
                Cookies.remove('accessToken');
                Cookies.remove('refreshToken');
                console.log(res);
            } else {
                return thunkAPI.rejectWithValue(res);
            }
        } catch (e) {
            console.log("Error", e.response.data);
            return thunkAPI.rejectWithValue(e.response.data);
        }
        
    }
);

export const LoginSlice = createSlice({
    name: "login",
    initialState: {
        isFetching: false,
        isSuccess: false,
        error: null,
    },
    extraReducers: (builder) => {
        builder
            .addCase(loginUser.fulfilled, (state, action) => {
                state.isSuccess = true;
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
            .addCase(logout.fulfilled, (state) => {
                state.isSuccess = false;
                state.isFetching = false;
                state.error = null;
            })
            .addCase(logout.pending, (state) => {
                state.isFetching = true;
                state.error = null;
            })
            .addCase(logout.rejected, (state, action) => {
                state.isFetching = false;
                state.isSuccess = false;
                state.error = action.payload;
            })
            // .addCase(refreshAccessToken.fulfilled, (state, action) => {
            //     state.accessToken = action.payload;
            // })
            .addMatcher(
                (action) => action.type.endsWith('/rejected'),
                (state, action) => {
                    state.error = action.payload;
                }
            );
    }
});


export const loginSelector = (state) => state.login;
export default LoginSlice.reducer;
