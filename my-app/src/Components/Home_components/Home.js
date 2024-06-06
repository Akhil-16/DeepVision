
import Section1 from './Homejs/Section1'
import NewProducts from './Homejs/New_products'
import Footer from './Homejs/Footer';
import Carousel from './Homejs/carousel';
import React, { useContext, useEffect, useState } from 'react'

import { useNavigate } from 'react-router-dom';
import { AlertContext } from '../../Context/AlertState';
import similarImgaesContext from '../../Context/similarImgaesContext';

function Home({data}) {
  const context=useContext(similarImgaesContext)
  const {loginverification}=context
  const {Managealert}=useContext(AlertContext)
  const navigate=useNavigate()
  useEffect(() => {
    if(!loginverification){
      console.log("Login is ",loginverification)
      navigate("/login")
      // Managealert("Please Login","error")

      
    }
   
  },[])
 
  

  return (
    <div className='Home'>
    <Section1 />
    <NewProducts />
    <Carousel/>
    <Footer/>
     </div>
  )
}

export default Home