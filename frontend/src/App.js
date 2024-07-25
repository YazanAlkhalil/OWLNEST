import {
  BrowserRouter,
}
  from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Router from './Router';
// import CreateCoursePage from './Pages/trainer/CreateCoursePage';
import { Toaster } from 'react-hot-toast';
import { useSelector } from 'react-redux';



function App() {
  const isDarkMode = useSelector((state) => state.theme.isDarkMode);
  const darkTheme = createTheme({
    palette: {
      mode: isDarkMode ? 'light' : "dark",
    },
  });
  return (
    <ThemeProvider theme={darkTheme}>
      <BrowserRouter>
        <div className={isDarkMode ? "" : "dark"}>
          <Router />
          <Toaster />
        </div>

      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;
