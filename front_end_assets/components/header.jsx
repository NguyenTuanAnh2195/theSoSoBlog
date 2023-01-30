import React from "react";
import "../styles/base/header.scss";

export default function Header(props) {
  return (
    <div id="header">
      <p id="blog-title">The So So Blog</p>
      <div id="blog-quicklinks">
        <a href="#">Home</a>
      </div>
    </div>
  );
}
