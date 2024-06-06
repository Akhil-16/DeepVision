import React, { useContext, useEffect, useState } from 'react';
import './login.css';
import login_bg from '../images/login_bg.jpg'; 
import axios from 'axios'
import { AlertContext } from '../Context/AlertState';
import similarImgaesContext from '../Context/similarImgaesContext';
import { useNavigate } from 'react-router-dom';

function Login() {
    const navigate=useNavigate()
    const {Managealert}=useContext(AlertContext)
    const context=useContext(similarImgaesContext)
    const {loginverification,checklogin}=context
    const [email,setemail]=useState('')
    const[pass,setpass]=useState('')
    const data={
        email:email,
        password:pass
    }
    function navigatecreateuser(){
      navigate('/createuser')
    }
    async function  Signin(e){
         
        e.preventDefault()
        try {
            if(data.email!="" && data.password!=""){
                await checklogin(data)


    
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
        <h2>Login</h2>
        <form >
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input type="text" id="email" name="email" onChange={(e)=>{setemail(e.target.value)}} />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input type="password" id="password" name="password"  onChange={(e)=>{setpass(e.target.value)}}/>
          </div>
          <button className='login'  type='submit' onClick={Signin}>Log in</button>
          <button className='signin'onClick={navigatecreateuser}> Sign in</button>

       
        </form>
      </div>
    </div>
  );
}

export default Login;