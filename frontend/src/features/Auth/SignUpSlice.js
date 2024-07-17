import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";


export const signupUser = createAsyncThunk(
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
        
    }
);

export const SignUpSlice = createSlice({
    name: "signup",
    initialState: {
        data: "",
        isFetching: false,
        isSuccess: false,
        isError: false,
        errorMessage: ""
    },
    extraReducers: (builder) => {
        builder
            .addCase(signupUser.fulfilled, (state, action) => {
                state.data = action.payload;
                state.isFetching = false;
                state.isSuccess = true;
                return state;
            })
            .addCase(signupUser.rejected, (state, action) => {
                state.isFetching = false;
                state.isError = true;
                state.errorMessage = action.payload.message
            })
            .addCase(signupUser.pending, (state) => {
                state.isFetching = true;
            })
    }
});

export const signupSelector = (state) => state.signup;
export default SignUpSlice.reducer;
