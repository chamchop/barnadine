import React, { useEffect, useState } from 'react';
import Table from 'react-bootstrap/Table';
import Footer from '../Footer';
import '../../App.css';

export default function Gdp() {

  const [highest, setData] = useState([]);
  useEffect(() => {
    fetch('http://localhost:5000/gdp-highest/gdp_data')
      .then(response => response.json())
      .then(highest => {
        setData(highest);
      })
      .catch(error => console.error('Error fetching highest:', error));
  }, []);

  const [lowest] = useState([]);
  useEffect(() => {
    fetch('http://localhost:5000/gdp-lowest/gdp_data')
      .then(response => response.json())
      .then(lowest => {
        setData(lowest);
      })
      .catch(error => console.error('Error fetching lowest:', error));
  }, []);

  return (
    <>
      <h2 className='gdp'>GDP Data</h2>
      <div>
        <h3>Highest by Quarter</h3>
        <Table striped bordered hover>
          <thead>
            <th>Quarter</th>
            <th>Number</th>
          </thead>
          <tbody>
            {highest.map(([quarter, number], index) => (
              <tr key = {index}>
                <td>{quarter}</td>
                <td>{number}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
      {/* <div>
        <h3>Lowest by Quarter</h3>
        <Table striped bordered hover>
          <thead>
            <th>Quarter</th>
            <th>Number</th>
          </thead>
          <tbody>
            {lowest.map(([quarter, number], index) => (
              <tr key = {index}>
                <td>{quarter}</td>
                <td>{number}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </div> */}
      <Footer />
    </>
  )
}

