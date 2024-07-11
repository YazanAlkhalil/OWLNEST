<<<<<<< HEAD

import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";


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
=======
//LoginSlice.jsx
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

export const loginUser = createAsyncThunk(
    "users/login",
    async (data, thunkAPI) => {
        // try {
        //     const params = {
        //         email: email,
        //         password: password
        //     };
        //     let link = "http://localhost:8080/api/v1/auth/authenticate";
        //     const response = await axios.post(link, params, {
        //         headers: { "Content-Type": "application/json" }
        //     });
        //     let data = await response.data;
        //     if (response.status === 200) {
        //         localStorage.setItem("token", data.token);
        //         return data;
        //     } else {
        //         return thunkAPI.rejectWithValue(data);
        //     }
        // } catch (e) {
        //     console.log("Error", e.response.data);
        //     thunkAPI.rejectWithValue(e.response.data);
        // }
        console.log(data);
    }
);

export const LoginSlice = createSlice({
    name: "login",
    initialState: {
        token: "",
        isFetching: false,
        isSuccess: false,
        isError: false,
        errorMessage: ""
    },
    reducers: {
        clearState: (state) => {
            state.isError = false;
            state.isSuccess = false;
            state.isFetching = false;

            return state;
        }
    },
    extraReducers: (builder) => {
        builder
            .addCase(loginUser.fulfilled, (state, { payload }) => {
                // state.token = payload.token;
                state.isFetching = false;
                state.isSuccess = true;
                return state;
            })
            .addCase(loginUser.rejected, (state, { payload }) => {
                state.isFetching = false;
                state.isError = true;
                state.errorMessage = payload.message
            })
            .addCase(loginUser.pending, (state) => {
                state.isFetching = true;
            })
    }
});

export const { clearState } = LoginSlice.actions;

export const loginSelector = (state) => state.login;
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
