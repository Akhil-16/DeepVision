import React, { useContext } from 'react'
import { AlertContext } from '../Context/AlertState';

function Alert() {
    console.log("this is akhil")
    function capitilize(word){
      const text=word.toLowerCase()
       return text.charAt(0).toUpperCase()+text.slice(1)
    
  }
    const {alert,Managealert}=useContext(AlertContext);
    return (
      (alert!=null &&<div style={{ zIndex: 10 }}className="alert alert-warning alert-dismissible fade show" role="alert">
      <strong>{capitilize(alert.type)}</strong>:{alert.message}
      
       </div>)
  
      
      
    
   
  
    )
}

export default Alert