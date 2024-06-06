import React, { useContext, useEffect, useState } from 'react'

import login_bg from '../images/login_bg.jpg'; 
import similarImgaesContext from '../Context/similarImgaesContext';
import { AlertContext } from '../Context/AlertState';
import { useNavigate } from 'react-router-dom';


function Sigin() {
    const navigate=useNavigate()
    const [email,setemail]=useState('')
    const[pass,setpass]=useState('')
    const [username,setusername]=useState('') 
    const context=useContext(similarImgaesContext)
    const {loginverification,Createuser}=context
    const {Managealert}=useContext(AlertContext)
    const data={
        name:username,
        email:email,
        password:pass

    }
    
    async function Signup(e){
        e.preventDefault()
        try {
            if(data.name!=""&&data.email!="" && data.password!=""){
                await Createuser(data)


    
            }else{
                Managealert("Enter details","danger")
    
            }
        } catch (error) {
            console.error('Error:', error);
            
            
        }



    }
    useEffect(() => {
        if(loginverification){
          console.log("loginverification is",loginverification)
            navigate("/")
            Managealert("Logged in","success")
        }
        
     
    }, [loginverification])
  return (
    <div className="background-container">
    <img src={login_bg} style={{ zIndex: -1 }} className="background-img" alt="Background" />
    <div className='login-form'>
      <h2>SIGNUP</h2>
      <form >
      <div className="form-group">
          <label htmlFor="name">name</label>
          <input type="text" id="name" name="name"  onChange={(e)=>{setusername(e.target.value)}}/>
        </div>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input type="text" id="email" name="email" onChange={(e)=>{setemail(e.target.value)}} />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input type="password" id="password" name="password"  onChange={(e)=>{setpass(e.target.value)}}/>
        </div>
        
        <button className='login'  type='submit' onClick={Signup}>Submit</button>
     
      </form>
    </div>
  </div>
  )
}

export default Sigin