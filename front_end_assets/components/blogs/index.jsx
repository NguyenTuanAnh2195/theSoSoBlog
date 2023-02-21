import React from "react";
import BlogPreview from "./previews";
import "../../styles/blogs/index.scss";

function BlogIndex(props) {
  const blogs = [
    {"category": "PROGRAMMING", "thumbnail": "#", "title": "Top 6 free website mockup tools 2022", "content": "This is the content for post 1", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"category": "WRITING", "thumbnail": "#", "title": "Post 2", "content": "This is the content for post 2", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"category": "LIFE", "thumbnail": "#", "title": "Post 3", "content": "This is the content for post 3", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"category": "PROGRAMMING", "thumbnail": "#", "title": "Post 4", "content": "This is the content for post 4", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"category": "WRITING", "thumbnail": "#", "title": "Post 5", "content": "This is the content for post 5", "author": {"fullName": "Anon", "email": "anony@mail.com"}},
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
