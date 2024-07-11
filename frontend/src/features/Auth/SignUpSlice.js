//SignUpSlice.jsx
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";


export const signupUser = createAsyncThunk(
<<<<<<< HEAD
    "signUp",
    async (data, thunkAPI) => {
        try {
            let link = "http://127.0.0.1:8000/api/register/";
            let otpUrl = "http://127.0.0.1:8000/api/send_otp/";
            const response = await axios.post(link, data, {
                headers: { "Content-Type": "application/json" }
            });
            let res = await response.data;
            if (response.status === 200) {
                console.log(res);
                let email = {
                    email: data.email
                }
                console.log(email);
                const otpResponse = await axios.post(otpUrl, email, {
                    headers: { "Content-Type": "application/json" }
                });
                
                if (otpResponse.status === 200) {
                    console.log(otpResponse.data);
                    return data;
                } else {
                    return thunkAPI.rejectWithValue(otpResponse.data);
                }
            } else {
                return thunkAPI.rejectWithValue(res);
            }
        } catch (e) {
            console.log("Error", e.response.data);
            return thunkAPI.rejectWithValue(e.response.data);
        }
        // console.log(data);
=======
    "users/signupUser",
    async (data, thunkAPI) => {
        // try {
        //     let link = "http://localhost:8080/api/v1/auth/register";
        //     const params = {
        //         email: email,
        //         firstname: firstname,
        //         lastname: lastname,
        //         password: password
        //     };
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
        //     return thunkAPI.rejectWithValue(e.response.data);
        // }
        console.log(data);
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
        
    }
);

export const SignUpSlice = createSlice({
    name: "signup",
    initialState: {
<<<<<<< HEAD
        data: "",
=======
        token: "",
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
        isFetching: false,
        isSuccess: false,
        isError: false,
        errorMessage: ""
    },
    extraReducers: (builder) => {
        builder
<<<<<<< HEAD
            .addCase(signupUser.fulfilled, (state, action) => {
                state.data = action.payload;
=======
            .addCase(signupUser.fulfilled, (state, { payload }) => {
                // console.log(payload);
                // state.token = payload.token;
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
                state.isFetching = false;
                state.isSuccess = true;
                return state;
            })
<<<<<<< HEAD
            .addCase(signupUser.rejected, (state, action) => {
                state.isFetching = false;
                state.isError = true;
                state.errorMessage = action.payload.message
=======
            .addCase(signupUser.rejected, (state, { payload }) => {
                state.isFetching = false;
                state.isError = true;
                state.errorMessage = payload.message
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
            })
            .addCase(signupUser.pending, (state) => {
                state.isFetching = true;
            })
    }
});

<<<<<<< HEAD
export const signupSelector = (state) => state.signup;
export default SignUpSlice.reducer;
=======
// export const { clearState } = SignupSlice.actions;

export const signupSelector = (state) => state.signup;
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
