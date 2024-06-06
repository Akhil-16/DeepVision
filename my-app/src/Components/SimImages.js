import React from 'react';

function SimImages({ finalimgs }) {
  
  if (finalimgs.length === 0) {
    return null; 
  }
  

  return (
    <div>
    <div className='Title'>
        <span className='new' style={{color:'red'}}>SIMILAR I</span>MAGES
      </div>
      <div className="row">
        {finalimgs.map((imageData, index) => (
          <div key={index} className="col-md-2 mb-4 g-3" > 
            <div className="card product-item" >
              <img
                className="card-img-top "
                src={`data:image/jpeg;base64,${imageData.image_data}`}
                alt={`Image ${index}`}
              />
              <div className="card-body">
                <p className="card-text">{imageData.combined_text}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SimImages;
