function MainPage(props) {
  const blogs = [
    {"title": "Post 1", "content": "This is the content for post 1", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"title": "Post 2", "content": "This is the content for post 2", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"title": "Post 3", "content": "This is the content for post 3", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"title": "Post 4", "content": "This is the content for post 4", "author": {"fullName": "Tuan Anh Nguyen", "email": "tuananhnguyen@mail.com"}},
    {"title": "Post 5", "content": "This is the content for post 5", "author": {"fullName": "Anon", "email": "anony@mail.com"}},
  ]
  return (
    <>
      <h1>Welcome to the So So Blog</h1>
      <h2>It's not good, not bad, just so so</h2>
      <h3>Feel free to browse a selection of blogs made available by the author</h3>
      {
        blogs.map(blog => {
          <>
            <h4>{blog.title}</h4>
            <p>{blog.content}</p>
            <p>Written by: {blog.author.fullName}</p>
            <p>contact the author at: {blog.author?.email}</p>
          </>
        })
      }
    
    </>
  )
}

export default MainPage;
