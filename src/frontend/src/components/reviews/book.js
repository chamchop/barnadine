import React, { useEffect, useState } from 'react';
import Table from 'react-bootstrap/Table';


export default function Book() {
    const [reviews, setReviews] = useState([]);

    useEffect(() => {
      fetch('http://localhost:5000/reviews/all')
        .then(response => response.json())
        .then(data => {
          setReviews(data);
        })
        .catch(error => console.error('Error fetching reviews:', error));
    }, []);
  
    return (
      <div className="App">
        <h1>Reviews</h1>
        <ul>
          {reviews.map((review, index) => (
            <li key={index}>
              <h2>{review.title}</h2>
              <p>{review.content}</p>
            </li>
          ))}
        </ul>
      </div>
    );
  }