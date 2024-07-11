import { configureStore } from "@reduxjs/toolkit";
<<<<<<< HEAD
import { SignUpSlice } from "./Auth/SignUpSlice";
import { VerifyOTPSlice } from "./Auth/VerifySlice";
import LoginReducer from "./Auth/LoginSlice";
import ResendReducer from "./Auth/ResendOtpSlice";
import ForgetPasswordReducer from "./Auth/ForgetPasswordSlice";
import CompanyReducer from "./Auth/CompanySlice";
=======
import { LoginSlice } from "./Auth/LoginSlice";
import { SignUpSlice } from "./Auth/SignUpSlice";
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73



const store = configureStore({
    reducer: {
<<<<<<< HEAD
        login: LoginReducer,
        signup: SignUpSlice.reducer,
        verifyOTP: VerifyOTPSlice.reducer,
        resend: ResendReducer,
        forgetPassword:  ForgetPasswordReducer,
        newCompany:  CompanyReducer,
=======
        login: LoginSlice.reducer,
        signup: SignUpSlice.reducer,
>>>>>>> 8dea41e2c9a71d9687848d0401f6b25010f1af73
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            immutableCheck: false,
            serializableCheck: false
        }),
        devTools : true
});

export default store;
