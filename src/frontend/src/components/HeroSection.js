import React from 'react';
import '../App.css';
import { Button } from './Button';
import './HeroSection.css';

export default function HeroSection() {
  return (
    <div className='hero-container'>
      {/* <video src='/videos/video-1.mp4' autoPlay loop muted /> */}
      <h1>WELCOME</h1>
      <p>To another website</p>
      <div className='hero-btns'>
        <Button className='btns' buttonStyle='btn--outline' buttonSize='btn--large'>EMPTY</Button>
      </div>
    </div>
  );
}
