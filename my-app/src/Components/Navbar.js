import React, { useState, useEffect, useContext } from 'react';
import './Navbar.css';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { AlertContext } from '../Context/AlertState';
function Navbar({onImageData}) {
  const navigate = useNavigate();
  const [selectedPhoto, setSelectedPhoto] = useState(null);
  const {Managealert}=useContext (AlertContext)

useEffect(() => {
  console.log("selected photo is ",selectedPhoto)
  
}, [selectedPhoto])

  const handlePhotoUpload = (event) => {
    const file = event.target.files[0];
    setSelectedPhoto(file);
  };

  const sendPhotoToAPI = async () => {
    try {
      if (selectedPhoto) {
        const formData = new FormData();
        formData.append('photo', selectedPhoto);
        onImageData (formData)
        
        // const response = await fetch(' http://127.0.0.1:5000/upload', {
        //   method: 'POST',
        //   body: formData
        // });

        // if (response.ok) {
        //   console.log('Photo uploaded successfully!');
        // } else {
        //   console.error('Error uploading photo:', response.statusText);
        // }
      } else {
        console.log('No photo selected.');
      }
    } catch (error) {
      console.error('Network error:', error);
    }
  };
  const logout=async()=>{
    let x=await axios.get("http://localhost:8081/api/auth/clear-cookie",{ withCredentials:true})
    console.log("logout ",x.data)
    window.location.reload()
    Managealert("Logged Out","Success")
    
   
  }


  return (
    <nav className="navbar">
      <div className="logo">Shopiy</div>
      <input type="text" className="search-bar" placeholder="Search..." />
      <div className="nav-icons">
        <label htmlFor="photo-upload" className="upload-label">
          Insert Photo
          <input type="file" id="photo-upload" accept="image/*" onChange={handlePhotoUpload} style={{ display: 'none' }} />
        </label>
        <button onClick={sendPhotoToAPI}>Upload</button>
        <button onClick={logout}> Logout</button>
        
      </div>
    </nav>
  );
}

export default Navbar;
