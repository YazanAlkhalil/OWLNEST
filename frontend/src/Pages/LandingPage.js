import React from 'react';
import herpImage from '../images/istockphoto-1992829733-170667a.webp';
import thirdSectionImage from '../images/top_v7.jpg';
import firstSvg from '../images/Background.svg';
import secondSvg from '../images/Background2.svg';
import thirdSvg from '../images/Background3.svg';
import star from '../images/Star.svg';
import airbnb from '../images/airbnb.svg';
import shopify from '../images/shopify.svg';
import girl from '../images/AmandaHouston_smaller1.jpg';
import man from '../images/a2de3954697c636276192afea0a6f661.jpg';
import logo from '../images/logo.png';
import facebook from '../images/facebook.svg';
import twitter from '../images/twitter.svg';
import youtube from '../images/youtube.svg';
import github from '../images/github.svg';
import instagram from '../images/instagram.svg';
import { useNavigate } from 'react-router-dom';
import { useEffect, useMemo, useState } from "react";
import Particles, { initParticlesEngine } from "@tsparticles/react";
import { loadSlim } from "@tsparticles/slim"; // if you are going to use `loadSlim`, install the "@tsparticles/slim" package too.

function LandingPage() {
    const navigate = useNavigate();
    const [init, setInit] = useState(false);

    useEffect(() => {
      initParticlesEngine(async (engine) => {
              await loadSlim(engine);
      }).then(() => {
        setInit(true);
      });
    }, []);
  
    const particlesLoaded = (container) => {
      console.log(container);
    };
  
    const options = useMemo(
      () => ({
        "autoPlay": true,
        "background": {
          "color": {
            "value": "#001F34"
          },
          "image": "",
          "position": "",
          "repeat": "",
          "size": "",
          "opacity": 1
        },
        "backgroundMask": {
          "composite": "destination-out",
          "cover": {
            "color": {
              "value": "#fff"
            },
            "opacity": 1
          },
          "enable": false
        },
        "clear": true,
        "defaultThemes": {},
        "delay": 0,
        "fullScreen": {
          "enable": true,
          "zIndex": 0
        },
        "detectRetina": true,
        "duration": 0,
        "fpsLimit": 120,
        "interactivity": {
          "detectsOn": "window",
          "events": {
            "onClick": {
              "enable": false,
              "mode": {}
            },
            "onDiv": {
              "selectors": {},
              "enable": false,
              "mode": {},
              "type": "circle"
            },
            "onHover": {
              "enable": false,
        "mode": "connect",
        "parallax": {
          "enable": false,
          "force": 2,
          "smooth": 10
        }
            },
            "resize": {
              "delay": 0.5,
              "enable": true
            }
          },
          "modes": {
            "trail": {
              "delay": 1,
              "pauseOnStop": false,
              "quantity": 1
            },
            "attract": {
              "distance": 200,
              "duration": 0.4,
              "easing": "ease-out-quad",
              "factor": 1,
              "maxSpeed": 50,
              "speed": 1
            },
            "bounce": {
              "distance": 200
            },
            "bubble": {
              "distance": 200,
              "duration": 0.4,
              "mix": false
            },
            "connect": {
              "distance": 80,
              "links": {
                "opacity": 0.5
              },
              "radius": 60
            },
            "grab": {
              "distance": 100,
              "links": {
                "blink": false,
                "consent": false,
                "opacity": 1
              }
            },
            "push": {
              "default": true,
              "groups": [],
              "quantity": 4
            },
            "remove": {
              "quantity": 10
            },
            "repulse": {
              "distance": 200,
              "duration": 0.4,
              "factor": 100,
              "speed": 1,
              "maxSpeed": 50,
              "easing": "ease-out-quad"
            },
            "slow": {
              "factor": 3,
              "radius": 200
            },
            "light": {
              "area": {
                "gradient": {
                  "start": {
                    "value": "#ffffff"
                  },
                  "stop": {
                    "value": "#000000"
                  }
                },
                "radius": 1000
              },
              "shadow": {
                "color": {
                  "value": "#000000"
                },
                "length": 2000
              }
            }
          }
        },
        "manualParticles": [],
        "particles": {
          "bounce": {
            "horizontal": {
              "value": 1
            },
            "vertical": {
              "value": 1
            }
          },
          "collisions": {
            "absorb": {
              "speed": 2
            },
            "bounce": {
              "horizontal": {
                "value": 1
              },
              "vertical": {
                "value": 1
              }
            },
            "enable": false,
            "maxSpeed": 50,
            "mode": "bounce",
            "overlap": {
              "enable": true,
              "retries": 0
            }
          },
          "color": {
            "value": "#fff",
            "animation": {
              "h": {
                "count": 0,
                "enable": false,
                "speed": 1,
                "decay": 0,
                "delay": 0,
                "sync": true,
                "offset": 0
              },
              "s": {
                "count": 0,
                "enable": false,
                "speed": 1,
                "decay": 0,
                "delay": 0,
                "sync": true,
                "offset": 0
              },
              "l": {
                "count": 0,
                "enable": false,
                "speed": 1,
                "decay": 0,
                "delay": 0,
                "sync": true,
                "offset": 0
              }
            }
          },
          "effect": {
            "close": true,
            "fill": true,
            "options": {},
            "type": {}
          },
          "groups": [],
          "move": {
            "angle": {
              "offset": 0,
              "value": 90
            },
            "attract": {
              "distance": 200,
              "enable": false,
              "rotate": {
                "x": 3000,
                "y": 3000
              }
            },
            "center": {
              "x": 50,
              "y": 50,
              "mode": "percent",
              "radius": 0
            },
            "decay": 0,
            "distance": {},
            "direction": "bottom",
            "drift": 0,
            "enable": true,
            "gravity": {
              "acceleration": 9.81,
              "enable": false,
              "inverse": false,
              "maxSpeed": 50
            },
            "path": {
              "clamp": true,
              "delay": {
                "value": 0
              },
              "enable": false,
              "options": {}
            },
            "outModes": {
              "default": "out",
              "bottom": "out",
              "left": "out",
              "right": "out",
              "top": "out"
            },
            "random": false,
            "size": false,
            "speed": 2,
            "spin": {
              "acceleration": 0,
              "enable": false
            },
            "straight": true,
            "trail": {
              "enable": false,
              "length": 10,
              "fill": {}
            },
            "vibrate": false,
            "warp": false
          },
          "number": {
            "density": {
              "enable": true,
              "width": 1920,
              "height": 1080
            },
            "limit": {
              "mode": "delete",
              "value": 0
            },
            "value": 400
          },
          "opacity": {
            "value": 1,
            "animation": {
              "count": 0,
              "enable": false,
              "speed": 2,
              "decay": 0,
              "delay": 0,
              "sync": false,
              "mode": "auto",
              "startValue": "random",
              "destroy": "none"
            }
          },
          "reduceDuplicates": false,
          "shadow": {
            "blur": 0,
            "color": {
              "value": "#000"
            },
            "enable": false,
            "offset": {
              "x": 0,
              "y": 0
            }
          },
          "shape": {
            "close": true,
            "fill": true,
            "options": {},
            "type": "circle"
          },
          "size": {
            "value": 10,
            "animation": {
              "count": 0,
              "enable": false,
              "speed": 5,
              "decay": 0,
              "delay": 0,
              "sync": false,
              "mode": "auto",
              "startValue": "random",
              "destroy": "none"
            }
          },
          "stroke": {
            "width": 0
          },
          "zIndex": {
            "value": {
              "min": 0,
              "max": 100
            },
            "opacityRate": 10,
            "sizeRate": 10,
            "velocityRate": 10
          },
          "destroy": {
            "bounds": {},
            "mode": "none",
            "split": {
              "count": 1,
              "factor": {
                "value": 3
              },
              "rate": {
                "value": {
                  "min": 4,
                  "max": 9
                }
              },
              "sizeOffset": true,
              "particles": {}
            }
          },
          "roll": {
            "darken": {
              "enable": false,
              "value": 0
            },
            "enable": false,
            "enlighten": {
              "enable": false,
              "value": 0
            },
            "mode": "vertical",
            "speed": 25
          },
          "tilt": {
            "value": 0,
            "animation": {
              "enable": false,
              "speed": 0,
              "decay": 0,
              "sync": false
            },
            "direction": "clockwise",
            "enable": false
          },
          "twinkle": {
            "lines": {
              "enable": false,
              "frequency": 0.05,
              "opacity": 1
            },
            "particles": {
              "enable": false,
              "frequency": 0.05,
              "opacity": 1
            }
          },
          "wobble": {
            "distance": 10,
            "enable": true,
            "speed": {
              "angle": 10,
              "move": 10
            }
          },
          "life": {
            "count": 0,
            "delay": {
              "value": 0,
              "sync": false
            },
            "duration": {
              "value": 0,
              "sync": false
            }
          },
          "rotate": {
            "value": 0,
            "animation": {
              "enable": false,
              "speed": 0,
              "decay": 0,
              "sync": false
            },
            "direction": "clockwise",
            "path": false
          },
          "orbit": {
            "animation": {
              "count": 0,
              "enable": false,
              "speed": 1,
              "decay": 0,
              "delay": 0,
              "sync": false
            },
            "enable": false,
            "opacity": 1,
            "rotation": {
              "value": 45
            },
            "width": 1
          },
          "links": {
            "blink": false,
            "color": {
              "value": "#fff"
            },
            "consent": false,
            "distance": 100,
            "enable": false,
            "frequency": 1,
            "opacity": 1,
            "shadow": {
              "blur": 5,
              "color": {
                "value": "#000"
              },
              "enable": false
            },
            "triangles": {
              "enable": false,
              "frequency": 1
            },
            "width": 2,
            "warp": false
          },
          "repulse": {
            "value": 0,
            "enabled": false,
            "distance": 1,
            "duration": 1,
            "factor": 1,
            "speed": 1
          }
        },
        "pauseOnBlur": true,
        "pauseOnOutsideViewport": true,
        "responsive": [],
        "smooth": false,
        "style": {},
        "themes": [],
        "zLayers": 100,
        "name": "Snow",
        "motion": {
          "disable": false,
          "reduce": {
            "factor": 4,
            "value": true
          }
        }
      }),
      [],
    );
    
    return (
        <div>
            {/* nav bar */}
           <div className='h-[100vh] '>
                {init && <Particles
                    id="tsparticles-navbar"
                    particlesLoaded={particlesLoaded}
                    options={options}
                    className='h-[100vh] absolute inset-0 z-1111'
                />}
           <div className='relative justify-between px-8 py-10 flex text-white'>
                <div className='relative z-10'>
                    <h2 className='text-white font-poppins text-2xl font-bold tracking-[0.075px]'>OwlNest</h2>
                </div>
                <div className='relative z-10 flex items-center gap-12'>
                    <ul className='flex gap-10'>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>Home</li>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>Features</li>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>How it Works</li>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>Testimonials</li>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>Blog</li>
                        <li className='hover:text-gray-200 hover:cursor-pointer'>Subscribe</li>
                    </ul>
                    <div className='flex gap-6'>
                        <button className='border text-base border-white hover:bg-white hover:cursor-pointer hover:text-black py-2 px-4 rounded' onClick={() => navigate('/login')}>Login</button>
                        <button className='bg-accent text-base hover:bg-accentHover hover:cursor-pointer py-2 px-4 rounded' onClick={() => navigate('/signUp')}>Register</button>
                    </div>
                </div>
            </div>
            
            {/* hero section */}
            <div className='relative  px-40 pb-10 flex text-center justify-between'>
                <img className='relative z-10 rounded w-[400px]' src={herpImage} />
                <div className='relative z-10 ml-24 flex flex-col items-center'>
                    <h1 className='text-white text-[64px] leading-tight font-semibold mt-8 '>Learn Everyday & Any New Skills Online with Top Instructors.</h1>
                    <p className='text-xl text-white mt-10 mx-40'>
                        We allow companies to train their employees in the way they want.
                    </p>
                    <button onClick={() => navigate('/signUp')} className='bg-accent btn hover:bg-accentHover px-6 mt-10 text-white '>
                        Get Started
                    </button>
                </div>
            </div>
           </div>

            <div className='relative z-2000'>
                {/* section two */}
                <div className='flex bg-white items-center gap-14 mt-20 py-20 px-40'>
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
                <div className='flex bg-white items-center gap-16 py-20  px-40'>
                    <img src={thirdSectionImage} />
                    <div className='mt-6'>
                        <h3 className='text-5xl font-semibold mb-6'>Quality Education Suporior human resources</h3>
                        <p className='text-gray-700 mb-6 text-2xl font-normal'>By connecting patients all over the world to the best instructors, resort like home helping individuals</p>
                        <button className='bg-accent text-base hover:bg-accentHover hover:cursor-pointer py-2 px-4 rounded text-white'>Explore More</button>
                    </div>
                </div>

                {/* forth section */}
                <div className='px-40 bg-secondary text-white py-20'>
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
                                    <h6 className='text-xl font-semibold'>
                                        Angela Karamoy
                                    </h6>
                                    <p className='text-gray-500'>
                                        CEO at Eduka
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                {/* fifth section */}
                <div className='px-40 bg-white  py-20'>
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

export default LandingPage;
