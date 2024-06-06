
import React,{createContext,useState} from 'react'

const AlertContext=createContext();

function Alertstate(props) {
  const [alert,setalert]=useState(null)
  const Managealert=(message,type)=>{
    setalert({message,type})
    console.log("message is ",type)
    setTimeout(() => {
      setalert(null)
      
    }, 2000);

  }
  
  return (
    <AlertContext.Provider value={{alert,Managealert}}>
        {props.children}
      
    </AlertContext.Provider>
    
  )
}

export  {Alertstate,AlertContext}