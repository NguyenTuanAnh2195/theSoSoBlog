import React from "react";
import "../styles/base/navbar.scss";

function Navbar(props) {
  return (
    <div id="navbar">
      <img src="#" />
      <p id="bio">
        Hi, I'm Tuan Anh. A programmer and an aspiring writer. Welcome to my blog.
        If you want to contact me, you can do so at the email address below:
        Email: anhnt20101995@gmail.com
      </p>
      <div id="blog-sections">
        <div className="section-container">
          <a href="#"><b>Programming</b></a>
        </div>
        <div className="section-container">
          <a href="#"><b>Life Stories</b></a>
        </div>
        <div className="section-container">
          <a href="#"><b>Written Stories</b></a>
        </div>
        <div className="section-container">
          <a href="#"><b>Misc</b></a>
        </div>
      </div>
    </div>
  )
}

export default Navbar;
