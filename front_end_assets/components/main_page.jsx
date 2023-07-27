import React from "react";
import { Outlet } from "react-router-dom";

import Header from "./header";
import Navbar from "./navbar";
import "../styles/base/mainpage.scss";


function MainPage() {
  return (
    <div className="main-page">
      <Header />
      <div className="main-content">
        <Navbar />
        <Outlet />
      </div>
    </div>
  )
}

export default MainPage;
