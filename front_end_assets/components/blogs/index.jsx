import React from "react";
import BlogPreview from "./previews";
import "../../styles/blogs/index.scss";

function BlogIndex(props) {
  const blogs = [
    {"thumbnail": "#", "title": "Post 1", "content": "This is the content for post 1", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"thumbnail": "#", "title": "Post 2", "content": "This is the content for post 2", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"thumbnail": "#", "title": "Post 3", "content": "This is the content for post 3", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"thumbnail": "#", "title": "Post 4", "content": "This is the content for post 4", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"thumbnail": "#", "title": "Post 5", "content": "This is the content for post 5", "author": {"fullName": "Anon", "email": "anony@mail.com"}},
  ]

  return (
    <div className="blog-index">
      {
        blogs.map(blog => {
          return <BlogPreview props={blog} />
        })
      }
    </div>
  )
}

export default BlogIndex;
