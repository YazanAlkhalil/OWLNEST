import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    value : false
}

export const ClickCourseSlice = createSlice({
    name: "clickCourse",
    initialState,
    reducers:{
        clickCourse: (state) => {  
            state.value = true
            },
        clickPreviousButton: (state) => {  
            state.value = false
            },
    }
})

export const { clickCourse,clickPreviousButton } = ClickCourseSlice.actions

export default ClickCourseSlice.reducer