//SignUpSlice.jsx
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";


export const requestEmail = createAsyncThunk(
    "requestEmail",
    async (data, thunkAPI) => {
        try {
            let requestEmail = "http://127.0.0.1:8000/api/request_reset_email/";
            const response = await axios.post(requestEmail, data, {
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

export const RequestEmailSlice = createSlice({
    name: "requestEmail",
    initialState: {
        isFetching: false,
        isSuccess: false,
        isError: false,
        errorMessage: ""
    },
    extraReducers: (builder) => {
        builder
            .addCase(requestEmail.fulfilled, (state, action) => {
                state.isFetching = false;
                state.isSuccess = true;
                return state;
            })
            .addCase(requestEmail.rejected, (state, action) => {
                state.isFetching = false;
                state.isError = true;
                state.errorMessage = action.payload.message
            })
            .addCase(requestEmail.pending, (state) => {
                state.isFetching = true;
            })
    }
});

export const requestEmailSelector = (state) => state.requestEmail;
export default RequestEmailSlice.reducer;
