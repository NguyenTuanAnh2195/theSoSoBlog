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
import Error from "./components/errors";
import BlogIndex from "./components/blogs";
import BlogDetail from "./components/blogs/detail";
import {
  blogByIdLoader
} from "./components/utilities/loaders";

const NotFound = function() {
  return (
    <CommonInfo message="You will have to look elsewhere for this page!" />
  );
};

const router = createBrowserRouter([
  {
    path: `/${rootUrl}/`,
    element: <MainPage />,
    errorElement: <Error />,
    chidlren: [
      { path: "", element: <BlogIndex /> },
      { path: "/:blogId", element: <BlogDetail />, loader: blogByIdLoader}
    ]
  },
  {
    path: `/${rootUrl}/*`,
    element: <NotFound />,
  }
]);


const container = document.getElementById("root");
const root = createRoot(container);
root.render(
  <React.StrictMode>
    <RecoilRoot>
      <RouterProvider router={router}/>
    </RecoilRoot>
  </React.StrictMode>
);
