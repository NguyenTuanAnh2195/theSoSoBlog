import React from "react";
import "../../styles/blogs/preview.scss";

function BlogPreview({props}) {
  const { thumbnail, title, content, author } = props;
  const credit = author?.fullName || author.email;
  return (
    <div className="blog-preview">
      <img src={thumbnail} />
      <h3>{title}</h3>
      <p>{content}</p>
      <p>By {credit}</p>
    </div>
  )
}

export default BlogPreview;
