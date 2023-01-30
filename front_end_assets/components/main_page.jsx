import React from "react";
import Header from "./header";
import Navbar from "./navbar";
import BlogIndex from "./blogs";
import "../styles/base/mainpage.scss";;

function MainPage(props) {
  
  return (
    <div className="main-page">
      <Header />
      <div className="main-content">
        <Navbar />
        <BlogIndex />   
      </div>
    </div>
  )
}

export default MainPage;
