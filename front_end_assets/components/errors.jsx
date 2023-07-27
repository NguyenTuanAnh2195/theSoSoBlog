import React from "react";

import { useRouteError } from "react-router";
import Header from "./header";
import "../styles/base/mainpage.scss";
import "../styles/base/common.scss";

function Error() {
  const error = useRouteError();
  return (
    <div className="main-page">
      <Header />
      <div className="main-content">
        <div className="common-text">
          Sorry, an unexpected error occured:
          {error.statusText || error.message}
        </div>
      </div>
    </div>
  )
}

export default Error;
