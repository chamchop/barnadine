import React from 'react';
import './Cards.css';
import CardItem from './CardItem';

export default function Cards() {
  return (
    <div className='cards'>
      <h1>ARTICLES</h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <CardItem src='images/img-9.jpg' text='Data: UK GDP - Top 10 Quarters' label='Adventure' path='/gdp'/>
            <CardItem src='images/img-2.jpg' text='Reviews: Book - ' label='Luxury' path='/book'/>
          </ul>
          <ul className='cards__items'>
            <CardItem src='images/img-3.jpg' text='3' label='Mystery' path='/reports'/>
            <CardItem src='images/img-4.jpg' text='4' label='Adventure' path='/reports'/>
            <CardItem src='images/img-8.jpg' text='5' label='Adrenaline' path='/reports'/>
          </ul>
        </div>
      </div>
    </div>
  );
}
