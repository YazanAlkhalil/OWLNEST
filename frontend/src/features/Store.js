import { configureStore } from "@reduxjs/toolkit";
import { LoginSlice } from "./Auth/LoginSlice";
import { SignUpSlice } from "./Auth/SignUpSlice";
import { ClickCompanySlice } from "./ClickCompany";
import { ClickCourseSlice } from "./ClickCourse";


const store = configureStore({
    reducer: {
        login: LoginSlice.reducer,
        signup: SignUpSlice.reducer,
        clickCompany: ClickCompanySlice.reducer,
        clickChangeCompany: ClickCompanySlice.reducer,
        clickCourse : ClickCourseSlice.reducer,
        clickPreviousButton : ClickCourseSlice.reducer
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            immutableCheck: false,
            serializableCheck: false
        }),
        devTools : true
});

export default store;
