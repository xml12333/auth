import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { Login } from './components/login/Login'
import {Register} from './components/Register'
import {Forgot} from './components/Forgot'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {Nav} from './components/Nav'
import {Home} from './components/Home'
import {Reset} from './components/Reset'

function App() {
 
   return (
    <BrowserRouter>
    <Nav/>
    <Routes>
      <Route path="/home" element={<Home/>}/>
      <Route path="/login" element={<Login/>}/>
      <Route path="/register" element={<Register/>}/>
      <Route path="/forgot" element={<Forgot/>}/>
      <Route path="/reset/:token" element={<Reset/>}/>

    </Routes>
   </BrowserRouter>)
  
}

export default App;
