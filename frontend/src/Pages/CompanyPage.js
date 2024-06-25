import React from 'react'
import NavBar from '../Components/Navbar'
import Company from '../Components/Company'

export default function CompanyPage() {
  return (
    <>
    <NavBar />
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
