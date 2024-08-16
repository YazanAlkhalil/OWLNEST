import React, { useState } from 'react'
import { Box, FormControl, InputLabel, MenuItem, Select } from '@mui/material'
import { useDispatch, useSelector } from 'react-redux';
import { toggleDarkMode } from '../features/DarkMode/DarkModeSlice';

function SettingGeneral() {
  const dispatch = useDispatch();
  const isDarkMode = useSelector((state) => state.theme.isDarkMode);

  return (
    <div className='pl-10'>
      <h3 className='mb-6 text-xl'>Dark or Light mode?</h3>
      <label class="inline-flex items-center cursor-pointer">
        <span class="mr-3 text-lg font-medium ">Light mode</span>
        <input type="checkbox" checked={isDarkMode} onChange={() => dispatch(toggleDarkMode())} class="sr-only peer" />
        <div class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600"></div>
      </label>
      
    </div>
  )
}

export default SettingGeneral
