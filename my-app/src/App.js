import Navbar from "./Components/Navbar";
import Home from "./Components/Home_components/Home";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import React, { useState } from 'react';
import axios from 'axios';
import SimImages from "./Components/SimImages";
import Login from "./Components/Login";
import { Alertstate } from "./Context/AlertState";
import Alert from "./Components/Alert";
import SimilarState from "./Context/SimilarState";

import './App.css';
import Loading from "./Components/Loading";
import Sigin from "./Components/Sigin";

function App() {
  const [imageData, setImageData] = useState(null);
  const [finalimages, setfinalImages] = useState([]);
  const [loading,setloading]=useState(false)

    const handleImageData = async (dataFromNavbar) => {
      
        
        try {
          setloading(true)
          const response = await fetch(' http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: dataFromNavbar
          });
          
         
  
          if (response.ok) {
            console.log('Photo uploaded successfully!');
            const data = await response.json();
            const data_to_send = data.top_5;
            console.log("data_to_send is",data_to_send)

            const response_from = await fetch('http://127.0.0.1:5001/getimageswithid', {
                method: 'POST',
                body: JSON.stringify({ ids: data_to_send }), 
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            if(response_from.ok){
              const data=await response_from.json()
              setloading(false)
              console.log("images data recievd",data.images);
              setfinalImages(data.images);
            }

          } else {
            console.error('Error uploading photo:', response.statusText);
          }
          
        } catch (error) {
          console.log("Network error",error)

          
        }
          
      

    };

  
  return (
    <>
    <Alertstate>
   <SimilarState>
    <Router> 
  <Alert ></Alert>
   <Navbar onImageData={handleImageData}  ></Navbar>
   <Loading loading={loading}></Loading>
   <SimImages finalimgs={finalimages}></SimImages>
        <Routes>
        <Route exact path="/Login" element={<Login> </Login>}/>
        <Route exact path="/createuser" element={<Sigin> </Sigin>}/>
        
        <Route exact path="/" element={<Home data={imageData} />} />
        
       
      </Routes>

    </Router>
    </SimilarState>
   
    </Alertstate>
    </>
  );
}

export default App;
