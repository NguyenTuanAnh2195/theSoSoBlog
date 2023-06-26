import React from "react";
import { Link } from "react-router-dom";
import "../styles/base/header.scss";

import { rootUrl } from "../common";

export default function Header(props) {
  return (
    <div id="header">
      <p id="blog-title">The So So Blog</p>
      <div id="blog-quicklinks">
        <Link to={`/${rootUrl}/`}>Home</Link>
      </div>
    </div>
  );
}
