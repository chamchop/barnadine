import React from 'react';
import './Footer.css';
import { Button } from './Button';
import { Link } from 'react-router-dom';

export default function Footer() {
  return (
    <div className='footer-container'>
      {/* <section className='footer-subscription'>
        <p className='footer-subscription-heading'></p>
        <p className='footer-subscription-text'></p>
      </section> */}
      <div class='footer-links'>
        <div className='footer-link-wrapper'>
          <div class='footer-link-items'>
            <h2>Data</h2><Link to='/data'>Data</Link>
          </div>
          <div class='footer-link-items'>
            <h2>Reports</h2><Link to='/reports'>Reports</Link>
          </div>
          <div class='footer-link-items'>
            <h2>Essays</h2><Link to='/essays'>Essays</Link>
          </div>
          <div class='footer-link-items'>
            <h2>About</h2><Link to='/about'>About</Link>
          </div>
        </div>
      </div>
      <section class='social-media'>
        <div class='social-media-wrap'>
          <div className='input-areas'>
          <form><input className='footer-input' name='email' type='email' placeholder='Your Email'/><Button buttonStyle='btn--outline'>Subscribe</Button></form>
        </div>
          <small class='website-rights'>OM © 2020</small>
          <div class='social-icons'><Link class='social-icon-link facebook' to='/' target='_blank' aria-label='Facebook'><i class='fab fa-facebook-f' /></Link>
            <Link class='social-icon-link instagram' to='/' target='_blank' aria-label='Instagram'><i class='fab fa-instagram' /></Link>
            <Link class='social-icon-link youtube' to='/' target='_blank' aria-label='Youtube'><i class='fab fa-youtube' /></Link>
            <Link class='social-icon-link twitter' to='/' target='_blank' aria-label='Twitter'><i class='fab fa-twitter' /></Link>
            <Link class='social-icon-link twitter' to='/' target='_blank' aria-label='LinkedIn'><i class='fab fa-linkedin' /></Link>
          </div>
        </div>
      </section>
    </div>
  );
}
