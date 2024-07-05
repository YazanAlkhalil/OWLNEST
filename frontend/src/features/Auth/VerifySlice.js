// VerifySlice.jsx
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

export const verifyOTP = createAsyncThunk(
    "verifyOTP",
    async (data, thunkAPI) => {
        try {
            const link = "http://127.0.0.1:8000/api/verify_otp/";
            const response = await axios.post(link, data, {
                headers: { "Content-Type": "application/json" }
            });
            const res = response.data;
            if (response.status === 200) {
                console.log("OTP Verification Successful:", res);
                return res;
            } else {
                console.log("OTP Verification Failed:", res);
                return thunkAPI.rejectWithValue(res);
            }
        } catch (e) {
            console.log("Error:", e.response.data);
            return thunkAPI.rejectWithValue(e.response.data);
        }
    }
);

export const VerifyOTPSlice = createSlice({
    name: "verifyOTP",
    initialState: {
        isFetching: false,
        isSuccess: false,
        isError: false,
        errorMessage: ""
    },
    extraReducers: (builder) => {
        builder
            .addCase(verifyOTP.fulfilled, (state, action) => {
                state.isFetching = false;
                state.isSuccess = true;
                return state;
            })
            .addCase(verifyOTP.rejected, (state, action) => {
                state.isFetching = false;
                state.isError = true;
                state.errorMessage = action.payload.message;
            })
            .addCase(verifyOTP.pending, (state) => {
                state.isFetching = true;
            });
    }
});

export const verifyOTPSelector = (state) => state.verifyOTP;
export default VerifyOTPSlice.reducer;
