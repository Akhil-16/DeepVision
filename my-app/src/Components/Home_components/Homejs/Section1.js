import React from 'react'
import "../Homecss/Section1.css"
import half1 from '../../../images/half1.png'
import grid1 from '../../../images/grid1.png'
import grid2 from '../../../images/grid2.png'
import grid3 from '../../../images/grid3.png'
import grid4 from  '../../../images/grid4.png'


function Section1() {
  return (
    <div className='section1'>
        <div className='half1'>
            <div className='text1'>
                <p className='heading'>
                    Women's fashion
                </p>
                <p className='discription'>
                Fashion is part of the daily air and 
                it changes all the time, with all the events.
                You can even see the approaching of a revolution in clothes.
                </p>
                <p className='shop_now'>
                    SHOP NOW
                </p>
                
            </div>
            <div className='image'>
            <img src={half1} className='image1' alt='img' />
            </div>
        </div>


        <div className='half2'>
            <div className='grid1'>
                <div className='text2'>
                    <p className='heading'>
                        Shoes
                    </p>
                    <p className='items'>
                        4506 items
                    </p>
                    <p className='shop_now'>
                        SHOP NOW
                    </p>
                </div>
                <div className='gridimg'>
                    <img src={grid1} className='image1g' alt='img' />
                </div>
            </div>

            <div className='grid2'>
            <div className='text2'>
                    <p className='heading'>
                        Shoes
                    </p>
                    <p className='items'>
                        4506 items
                    </p>
                    <p className='shop_now'>
                        SHOP NOW
                    </p>
                </div>
                <div className='gridimg'>
                    <img src={grid3} className='image2g' alt='img' />
                </div>
            </div>

            <div className='grid3'>
            <div className='text2'>
                    <p className='heading'>
                        Men's FashionS
                    </p>
                    <p className='items'>
                        4506 items
                    </p>
                    <p className='shop_now'>
                        SHOP NOW
                    </p>
                </div>
                <div className='gridimg'>
                    <img src={grid2} className='image3g' alt='img' />
                </div>
            </div>
            
            <div className='grid4'>
            <div className='text2'>
                    <p className='heading'>
                        Shoes
                    </p>
                    <p className='items'>
                        4506 items
                    </p>
                    <p className='shop_now'>
                        SHOP NOW
                    </p>
                </div>
                <div className='gridimg'>
                    <img src={grid4} className='image4g' alt='img' />
                </div>
            </div>
        </div>
    </div>
  )
}

export default Section1