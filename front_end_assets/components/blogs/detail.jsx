import React from "react";

import { useLoaderData } from "react-router-dom";


export default function BlogDetail() {
  const { blog } = useLoaderData();

  return (
    <div className="blog">
      <p>{blog.title || "No Title"}</p>
      Category: <p>{blog.caregory}</p>
      <p>By: {blog.author.username} </p>
      <br />
      <p>{blog.content || "Ooops, looks like this page is empty!"}</p>
    </div>
  )
}
