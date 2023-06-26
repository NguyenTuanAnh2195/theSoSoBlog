import React from "react";

import Header from "./header";
import "../styles/base/mainpage.scss";
import "../styles/base/common.scss";

function CommonInfo(props) {
  const { message } = props;
  return (
    <div className="main-page">
      <Header />
      <div className="main-content">
        <div className="common-text">{message}</div>
      </div>
    </div>
  )
}

export default CommonInfo;
