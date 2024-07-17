import React from 'react'
import Company from '../Components/Company'
import Navbar2 from '../Components/Navbar2'
import Company2 from '../Components/Company2'
import logo from '../images/logo.png'


export default function CompanyPage() {
  
  return (
    <>
    <Navbar2 />
    <div className="container mx-auto">
        <h1 className='font-black text-4xl p-8'>Companies:</h1>
        <div className='grid grid-cols-3 gap-10 px-10'>
        {/* <Company />
        <Company />
        <Company />
        <Company />
        <Company />
        <Company />
        <Company />
        <Company />
        <Company />
        <Company />
        <Company />
        <Company /> */}
        <Company2 image={logo}/>
        <Company2 image={logo}/>
        <Company2 image={logo}/>
        </div>
    </div>
    </>
  )
}
