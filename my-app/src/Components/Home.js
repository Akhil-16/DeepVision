import React, { useContext, useEffect, useState } from 'react'
import similarImgaesContext from '../Context/similarImgaesContext'
import { useNavigate } from 'react-router-dom';
import { AlertContext } from '../Context/AlertState';

function Home({data}) {
  const context=useContext(similarImgaesContext)
  const {loginverification}=context
  const {Managealert}=useContext(AlertContext)
  const navigate=useNavigate()
  useEffect(() => {
    if(!loginverification){
      console.log("Login is ",loginverification)
      navigate("/login")
      Managealert("Please Login","error")

      
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