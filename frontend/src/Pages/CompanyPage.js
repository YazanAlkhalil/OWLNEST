import React from 'react'
import Company from '../Components/Company'
import Navbar2 from '../Components/Navbar2'

export default function CompanyPage() {
  
  return (
    <>
    <Navbar2 />
    <div className="container mx-auto">
        <h1 className='font-black text-2xl p-8'>Companies</h1>
        <div className='flex justify-evenly flex-wrap gap-7 flex-3'>
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
        <Company />
        <Company />
        </div>
    </div>
    </>
  )
}
