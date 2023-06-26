import React from "react";
import { createRoot }from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import { RecoilRoot } from "recoil";

import { rootUrl } from "./common";
import MainPage from "./components/main_page.jsx";
import CommonInfo from "./components/common_info.jsx";


const NotFound = function () {
  return (
    <CommonInfo message="You will have to look elsewhere for this page!" />
  );
};

const router = createBrowserRouter([
  {
    path: `/${rootUrl}`,
    element: <MainPage />,
  },
  {
    path: `/${rootUrl}/not_found`,
    element: <NotFound />,
  }
]);


const container = document.getElementById("root");
const root = createRoot(container);
root.render(
  <RecoilRoot>
    <RouterProvider router={router}/>
  </RecoilRoot>
);