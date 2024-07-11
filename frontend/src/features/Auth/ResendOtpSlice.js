//SignUpSlice.jsx
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";


export const resendOtp = createAsyncThunk(
    "resend",
    async (data, thunkAPI) => {
        try {
            let otpUrl = "http://127.0.0.1:8000/api/send_otp/";
            const response = await axios.post(otpUrl, data, {
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
        // console.log(data);
        
    }
);

export const ResendOtpSlice = createSlice({
    name: "resend",
    initialState: {
        data: "",
        isFetching: false,
        isSuccess: false,
        isError: false,
        errorMessage: ""
    },
    extraReducers: (builder) => {
        builder
            .addCase(resendOtp.fulfilled, (state, action) => {
                state.data = action.payload;
                state.isFetching = false;
                state.isSuccess = true;
                return state;
            })
            .addCase(resendOtp.rejected, (state, action) => {
                state.isFetching = false;
                state.isError = true;
                state.errorMessage = action.payload.message
            })
            .addCase(resendOtp.pending, (state) => {
                state.isFetching = true;
            })
    }
});

export const resendSelector = (state) => state.resend;
export default ResendOtpSlice.reducer;
