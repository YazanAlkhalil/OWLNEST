import { configureStore } from "@reduxjs/toolkit";
import { SignUpSlice } from "./Auth/SignUpSlice";
import { VerifyOTPSlice } from "./Auth/VerifySlice";
import LoginReducer from "./Auth/LoginSlice";
import ResendReducer from "./Auth/ResendOtpSlice";
import ForgetPasswordReducer from "./Auth/ForgetPasswordSlice";



const store = configureStore({
    reducer: {
        login: LoginReducer,
        signup: SignUpSlice.reducer,
        verifyOTP: VerifyOTPSlice.reducer,
        resend: ResendReducer,
        forgetPassword:  ForgetPasswordReducer
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            immutableCheck: false,
            serializableCheck: false
        }),
        devTools : true
});

export default store;
