//SignUpSlice.jsx
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";


export const forgetPass = createAsyncThunk(
    "forgetPassword",
    async (data, thunkAPI) => {
        try {
            let otpUrl = "http://127.0.0.1:8000/api/forget_password/";
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

export const ForgetPasswordSlice = createSlice({
    name: "forgetPassword",
    initialState: {
        data: "",
        isFetching: false,
        isSuccess: false,
        isError: false,
        errorMessage: ""
    },
    extraReducers: (builder) => {
        builder
            .addCase(forgetPass.fulfilled, (state, action) => {
                state.data = action.payload;
                state.isFetching = false;
                state.isSuccess = true;
                return state;
            })
            .addCase(forgetPass.rejected, (state, action) => {
                state.isFetching = false;
                state.isError = true;
                state.errorMessage = action.payload.message
            })
            .addCase(forgetPass.pending, (state) => {
                state.isFetching = true;
            })
    }
});

export const forgtePassSelector = (state) => state.resend;
export default ForgetPasswordSlice.reducer;
