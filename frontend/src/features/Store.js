import { configureStore } from "@reduxjs/toolkit";
import { LoginSlice } from "./Auth/LoginSlice";
import { SignUpSlice } from "./Auth/SignUpSlice";



const store = configureStore({
    reducer: {
        login: LoginSlice.reducer,
        signup: SignUpSlice.reducer,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            immutableCheck: false,
            serializableCheck: false
        }),
        devTools : true
});

export default store;
