import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    value : false
}

export const ClickCompanySlice = createSlice({
    name: "clickCompany",
    initialState,
    reducers:{
        clickCompany: (state) => {  
            state.value = true
            },
        clickChnageCompany: (state) => {  
            state.value = false
            },
    }
})

export const { clickCompany,clickChnageCompany } = ClickCompanySlice.actions

export default ClickCompanySlice.reducer