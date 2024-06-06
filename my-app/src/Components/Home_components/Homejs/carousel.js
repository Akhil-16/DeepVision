import React from 'react'
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import C1 from '../../../images/c1.jpg'
import C2 from '../../../images/c2.jpg'
import C3 from '../../../images/c3.jpg'
import C4 from '../../../images/c4.jpg'
import C5 from '../../../images/c5.jpg'
import '../Homecss/carousel.css'


function carousel() {

  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    fade: true,
    cssEase: 'ease-in-out',
  };

  return (

    <Slider {...settings} className='carousel'>
      <div className='carousel1'>
        <img src={C1} className='carouselimage' alt='img' />
      </div>

        <div className='carousel1' >
        <img src={C2} className='carouselimage' alt='img' />
        </div>

        <div className='carousel1'>
        <img src={C3} className='carouselimage' alt='img' />
        </div>

        <div className='carousel1'>
        <img src={C4} className='carouselimage' alt='img' />
        </div>

        <div className='carousel1'>
        <img src={C5} className='carouselimage' alt='img' />
        </div>
    </Slider>

  )
}

export default carousel