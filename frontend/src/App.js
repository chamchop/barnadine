import './App.css';
import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/pages/Home';
import Data from './components/pages/Data';
import Reports from './components/pages/Reports';
import Essays from './components/pages/Essays';
import About from './components/pages/About';
import SignUp from './components/pages/SignUp';
import article1 from './components/articles/article1';

export default function App() {
  return (
    <>
      <Router>
        <Navbar/>
        <Switch>
          <Route path='/' exact component={Home}/>
          <Route path='/data' component={Data}/>
          <Route path='/reports' component={Reports}/>
          <Route path='/essays' component={Essays}/>
          <Route path='/about' component={About}/>
          <Route path='/sign-up' component={SignUp}/>
        </Switch>
          <Route path='/article1' component={article1}/>
      </Router>
    </>
  );
}