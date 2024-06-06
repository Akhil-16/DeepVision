import React from 'react'

function Loading({loading}) {

  return (
    
  (loading  && 
    <div
        style={{
            position: 'fixed',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            backgroundColor: 'rgba(0, 0, 0, 0.5)', // Semi-transparent black overlay
            zIndex: 9999, // Ensure the overlay is on top of other content
        }}
    >
       
        
       <div className="d-flex justify-content-center align-items-center" style={{ height: '100vh' }}>
      <div className="spinner-border text-white" role="status"></div>
    </div>
        
    </div>
)
  


  )
}

export default Loading