import React from 'react';
import {BrowserRouter as Router, Route} from "react-router-dom";
//import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";

import MainPage from "./Components/MainPage.js";

function App() {
  return (
    <Router>
      <br/>
      <Route path ="/" exact component = {MainPage} />
    </Router>
  );
}

export default App;
