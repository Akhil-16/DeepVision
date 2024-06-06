import similarImgaesContext from "./similarImgaesContext";
import { useState,useEffect, useContext } from "react";
import axios from 'axios';

import React from 'react'
import { AlertContext } from "./AlertState";

function SimilarState(props) {
    const {Managealert}=useContext(AlertContext)
    const [loginverification,setloginverification]=useState(document.cookie.includes("isLoggedin"))
    async function checklogin(data){
        const config={
            headers:{"Content-Type":"application/json"},
            withCredentials:true
          }
        const response = await axios.post('http://localhost:8081/api/auth/login', data,config)
        console.log("response is",response.data)
        setloginverification(document.cookie.includes("isLoggedin"))
        Managealert(response.data,"Msg")
        
       

    }
    async function Createuser(data){
      const config={
        headers:{"Content-Type":"application/json"},
        withCredentials:true
      }
      
      const response=await axios.post("http://localhost:8081/api/auth/createuser",data,config)
      console.log("response is ",response.data)
      setloginverification(document.cookie.includes("isLoggedin"))
      Managealert(response.data,"Msg")

    }
  return (
    <similarImgaesContext.Provider value={{loginverification,checklogin,Createuser}}>
    {props.children}
  
</similarImgaesContext.Provider>
  )
}

export default SimilarState