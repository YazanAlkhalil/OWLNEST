//SignUpSlice.jsx
import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";


export const newCompany = createAsyncThunk(
    "newCompany",
    async (data, thunkAPI) => {
        try {
            let CreateCompnyUrl = "http://127.0.0.1:8000/api/create_company/";
            const response = await axios.post(CreateCompnyUrl, data, {
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

export const CompanySlice = createSlice({
    name: "newCompany",
    initialState: {
        data: "",
        isFetching: false,
        isSuccess: false,
        isError: false,
        errorMessage: ""
    },
    extraReducers: (builder) => {
        builder
            .addCase(newCompany.fulfilled, (state, action) => {
                state.data = action.payload;
                state.isFetching = false;
                state.isSuccess = true;
                return state;
            })
            .addCase(newCompany.rejected, (state, action) => {
                state.isFetching = false;
                state.isError = true;
                state.errorMessage = action.payload.message
            })
            .addCase(newCompany.pending, (state) => {
                state.isFetching = true;
            })
    }
});

export const newCompanySelector = (state) => state.newCompany;
export default CompanySlice.reducer;
