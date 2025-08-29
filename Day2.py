# Day - 2
# Author : Leo Programmer-011
# Date : 2025-08-29

from fastapi import FastAPI

app = FastAPI()

# In Memory - Database
blogs = []

@app.get("/")
def root():
    return {"Hello my dear leo programmers...! Welcome to the Blog API Day-2 world...!"}

@app.get("/create-blog")
def create_blog(title: str, author: str, content: str):
    blog = {
        "title": title,
        "author": author,
        "content": content
    }
    blogs.append(blog) 
    return {"message": "Blog Created Successfullyy...!", "blog": blog}
    
@app.get("/get-blogs")
def get_blogs():
    return {
    "message": "Welcome, here are all the blogs...!",
    "blogs": blogs
    }

@app.get("/get-blog/{blog_id}")
def get_blog(blog_id: int):
    
    if blog_id < 0 or blog_id >= len(blogs):
        return {"error": "Blog not found"}
    
    return {
        "message": f"your searched blog {blog_id} is here...",
        "blog": blogs[blog_id]
    }

# @app.delete("/delete-blog/{blog_id}")
'''
When you type something in the browser address bar, it always makes a GET request — because that’s the only method browsers support directly in the URL. That’s why:

You can read data using GET from the address bar.

But you cannot send POST, PUT, or DELETE requests directly from the address bar.
'''

@app.get("/delete-blog/{blog_id}")
def delete_blog(blog_id: int):
    if blog_id < 0 or blog_id >= len(blogs):
        return {"error": "Blog not found"}
    
    deleted_blog = blogs.pop(blog_id)
    return {
        "message": f"Blog {blog_id} deleted successfully...!",
        "deleted_blog": deleted_blog
    }
