import React from 'react'
import herpImage from '../images/istockphoto-1992829733-170667a.webp'
import thirdSectionImage from '../images/top_v7.jpg'
import firstSvg from '../images/Background.svg'
import secondSvg from '../images/Background2.svg'
import thirdSvg from '../images/Background3.svg'
import star from '../images/Star.svg'
import airbnb from '../images/airbnb.svg'
import shopify from '../images/shopify.svg'
import girl from '../images/AmandaHouston_smaller1.jpg'
import man from '../images/a2de3954697c636276192afea0a6f661.jpg'
import logo from '../images/logo.png'
import facebook from '../images/facebook.svg'
import twitter from '../images/twitter.svg'
import youtube from '../images/youtube.svg'
import github from '../images/github.svg'
import instagram from '../images/instagram.svg'
import { useNavigate } from 'react-router-dom'




function LandingPage() {
    const navigate = useNavigate()
    return (
        <div>
            {/* nav bar */}
            <div className='bg-primary justify-between px-8 py-10 flex text-white'>
                <div>
                    <h2 className='text-white font-poppins text-2xl font-bold tracking-[0.075px]'>OwlNest</h2>
                </div>
                <div className='flex items-center gap-12'>
                    <ul className='flex gap-10'>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>Home</li>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>Features</li>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>How it Works</li>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>Testimonials</li>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>Blog</li>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>subscribe</li>
                    </ul>
                    <div className='flex gap-6'>
                        <button className='border text-base border-white hover:bg-white hover:cursor-pointer hover:text-black py-2 px-4 rounded' onClick={()=>navigate('/login')}>Login</button>
                        <button className='bg-accent text-base hover:bg-accentHover hover:cursor-pointer py-2 px-4 rounded' onClick={()=>navigate('/signUp')}>Register</button>
                    </div>
                </div>
            </div>
            <div>

                {/* //hero section */}
                <div className='bg-primary px-40 pb-10 flex text-center justify-between'>
                    <img className='rounded  w-[400px]' src={herpImage} />
                    <div className='ml-24 flex flex-col items-center'>
                        <h1 className='text-white text-[64px] leading-tight font-semibold mt-8 '>Learn Everyday & Any New Skills Online with Top Instructors.</h1>
                        <p className='text-xl text-white mt-10 mx-40'>
                            We allow companies to train there employees in the way they want.
                        </p>
                        <button onClick={()=> navigate('/signUp')} className='bg-accent btn hover:bg-accentHover px-6 mt-10 text-white '>
                            Get Started
                        </button>
                    </div>
                </div>

                {/* section two */}
                <div className='flex items-center gap-14 my-20 px-40'>
                    <div className='w-2/5'>
                        <h3 className='text-5xl font-semibold mb-6'>Great
                            Deals For You</h3>
                        <p className='text-2xl text-gray-500 font-normal'>The sky was cloudless and of a deep dark blue the spectacle.</p>
                    </div>
                    <div className='flex gap-6'>
                        <div className='border border-black shadow-lg p-4 flex flex-col items-start'>
                            <div className='rounded-full bg-[]'>
                                <img src={firstSvg} />
                                <h5 className='text-2xl font-semibold my-4'>Easy Payment</h5>
                                <p className='mb-4 text-gray-500 font-normal'>Online, billing invoice & contracts</p>
                            </div>

                        </div>
                        <div className='border border-black shadow-lg p-4 flex flex-col items-start'>
                            <div className='rounded-full bg-[]'>
                                <img src={secondSvg} />
                                <h5 className='text-2xl font-semibold my-4'>Easy Payment</h5>
                                <p className='mb-4 text-gray-400 font-normal'>Online, billing invoice & contracts</p>
                            </div>

                        </div>
                        <div className='border border-black shadow-lg p-4 flex flex-col items-start'>
                            <div className='rounded-full bg-[]'>
                                <img src={thirdSvg} />
                                <h5 className='text-2xl font-semibold my-4'>Easy Payment</h5>
                                <p className='mb-4 text-gray-400 font-normal'>Online, billing invoice & contracts</p>
                            </div>
                        </div>

                    </div>
                </div>

                {/* third section */}
                <div className='flex items-center gap-16 my-20 px-40'>
                    <img src={thirdSectionImage} />
                    <div className='mt-6'>
                        <h3 className='text-5xl font-semibold mb-6'>Quality Education Suporior human resources</h3>
                        <p className='text-gray-700 mb-6 text-2xl font-normal'>By connecting patients all over the world to the best instructors, resort like home helping individuals</p>
                        <button className='bg-accent text-base hover:bg-accentHover hover:cursor-pointer py-2 px-4 rounded text-white'>Explore More</button>
                    </div>
                </div>

                {/* forth section */}
                <div className='my-10 px-40 bg-secondary text-white py-10'>
                    <h3 className='mb-6 text-5xl font-semibold'>What our student say?</h3>
                    <p className='text-xl font-normal'>Follow this steps below to start use of Projećt Software.</p>
                    <div className='flex items-center gap-4 my-6'>
                        <div className='bg-white text-black w-1/2 h-72 rounded shadow-lg p-8 flex flex-col'>
                            <div className='flex justify-between'>
                                <img src={star} />
                                <img src={airbnb} />
                            </div>
                            <p className='my-6'>
                                OwlNest is a really great site with really great people and the quality of content is excellent. Some of the best education in the world use this
                            </p>
                            <div className='flex items-center mt-auto'>
                                <img className='w-12 h-12 rounded-full mr-4' src={man} />
                                <div >
                                    <h6 className='text-xl font-semibold'>
                                        Himura Adreas
                                    </h6>
                                    <p className='text-gray-500'>
                                        CEO at Manika
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div className='bg-white text-black w-1/2 h-72 rounded shadow-lg p-8 flex flex-col'>
                            <div className='flex justify-between'>
                                <img src={star} />
                                <img src={shopify} />
                            </div>
                            <p className='my-6'>
                                Education has consistently delivered above and beyond my expectations! Brilliant tutor work, incredible response time and a really friendly team.
                            </p>
                            <div className='flex items-center mt-auto'>
                                <img className='w-12 h-12 rounded-full mr-4' src={girl} />
                                <div >
                                    <h7 className='text-xl font-semibold'>
                                        Angela Karamoy
                                    </h7>
                                    <p className='text-gray-500'>
                                        CEO at Eduka
                                    </p>
                                </div>
                            </div>
                        </div>


                    </div>

                </div>

                {/* fifth section */}
                <div className='px-40 my-10 py-10'>
                    <div className='bg-primary rounded items-center flex justify-evenly text-white p-8'>
                        <div className='w-1/2'>
                            <h4 className='text-5xl font-semibold'>Get More Info About us</h4>
                            <p className='text-gray-300 mt-4 mb-6'>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum.</p>
                            <div >
                                <button className='btn mr-3 bg-accent hover:bg-accent px-12 py-3'>Book Now</button>
                                <button className='btn border border-white px-12 py-3'>Contact Us</button>
                            </div>

                        </div>
                        <img className='w-1/5' src={logo} />
                    </div>
                </div>

                {/* footer */}
                <div className='py-10 px-40 bg-background flex gap-12'>
                    <div className='w-2/6'>
                        <h6 className='mb-4 text-2xl font-semibold'>OwlNest</h6>
                        <p className='text-gray-500'>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum.</p>
                        <div className='mt-6 flex gap-6'>
                            <img src={facebook} />
                            <img src={twitter} />
                            <img src={instagram} />
                            <img src={youtube} />
                            <img src={github} />
                        </div>
                    </div>
                    <div className='w-1/6'>
                        <h6 className='mb-4 text-2xl font-semibold'>Products</h6>
                        <ul>
                            <li className='my-2 text-gray-500'>Features</li>
                            <li className='my-2 text-gray-500'>Enterprise</li>
                            <li className='my-2 text-gray-500'>Security</li>
                            <li className='my-2 text-gray-500'>Customer Stories</li>
                            <li className='my-2 text-gray-500'>Pricing</li>
                            <li className='my-2 text-gray-500'>Demo</li>
                        </ul>
                    </div>
                    <div className='w-1/6'>
                        <h6 className='mb-4 text-2xl font-semibold'>Teams</h6>
                        <ul>
                            <li className='my-2 text-gray-500'>Engineering</li>
                            <li className='my-2 text-gray-500'>Financial Services</li>
                            <li className='my-2 text-gray-500'>Sales</li>
                            <li className='my-2 text-gray-500'>IT</li>
                            <li className='my-2 text-gray-500'>Customer Support</li>
                            <li className='my-2 text-gray-500'>Human Resources</li>
                            <li className='my-2 text-gray-500'>Media</li>
                        </ul>
                    </div>
                    <div className='w-1/6'>
                        <h6 className='mb-4 text-2xl font-semibold'>Company</h6>
                        <ul>
                            <li className='my-2 text-gray-500'>About us</li>
                            <li className='my-2 text-gray-500'>Leadership</li>
                            <li className='my-2 text-gray-500'>News</li>
                            <li className='my-2 text-gray-500'>Media Kit</li>
                            <li className='my-2 text-gray-500'>Career</li>
                            <li className='my-2 text-gray-500'>Documentation</li>
                        </ul>
                    </div>
                    <div>
                        <h6 className='mb-4 text-2xl font-semibold'>Subscribe Us</h6>
                        <div className='bg-[#ccd4e1] text-gray-500 p-2 rounded mb-4'>
                            Your email here...
                        </div>
                        <button className='btn bg-accent hover:bg-accentHover px-16 text-white'>
                            Subscribe
                        </button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default LandingPage
