# Day - 5 : HTTP Methods
# Author : The Leo Programmer - 011
# Date : 2025-09-01

from fastapi import FastAPI

app = FastAPI()

# Let's create some posts data by our own
posts = [
    {"id": 1, "title": "First Day", "content": "FastAPI is python framework"},
    {"id": 2, "title": "Second Day", "content": "We are learning FastAPI"},
    {"id": 3, "title": "Third Day", "content": "We are creating APIs"},
    {"id": 4, "title": "Fourth Day", "content": "We are creating more APIs"},
]

'''
GET Method:

Purpose: Retrieve data (safe & read-only).

Why: Clients often need to fetch information without changing anything.

Example Use: Get a user profile, fetch list of products.
'''

@app.get("/")
def read_root():
    return {"message": "Welcome to the Leo Blogs..."}

@app.get("/posts")
def get_posts():
    return {"message": "Here is your feed.", "data": posts}

@app.get("/posts/{id}")
def get_post(id: int):
    for post in posts:
        if post["id"] == id:            
            return {"message": f"Here is your searched post -  {posts[id-1]}"}
    return {"message": "Post Not Found!"}


'''
POST Method:
Purpose: Create new data (not safe, modifies server state).
Why: Used when client wants to send new data to the server.
Example Use: Register new user, add a blog post.
'''

@app.post("/createpost")
def create_post(new_post: dict):
    posts.append(new_post)
    return {"message": "Post Created Successfully!", "data": posts}

'''
PUT Method:

Purpose: Update an existing resource (replace fully).
Why: Sometimes we need to replace all fields of a resource.
Example Use: Update entire user profile.
'''

@app.put("/updatepost/{id}")
def update_post(id: int, updated_post: dict):
    for post in posts:
        if post["id"] == id:
            post["Updated Title"] = updated_post.get("title")
            post["Updated Content"] = updated_post.get("content")
            return {"message": "Post Updated Successfully!", "data": post}
    return {"message": "Post Not Found!"}

'''
PATCH Method:
Purpose: Partially update an existing resource.
Why: Sometimes we only need to change a few fields.
Example Use: Update user's email or password.
'''

@app.patch("/updatepost/{id}")
def patch_post(id: int, updated_post: dict):
    for post in posts:
        if post['id'] == id:
            if 'title' in updated_post:
                post['title'] = updated_post['title']
            if 'content' in updated_post:
                post['content'] = updated_post['content']
            return {"message": "Post Patched Successfully!", "data": post}
    return {"message": "Post Not Found!"}

'''
PUT vs PATCH

PUT → Replace the entire resource.

If the object has {id, title, content}, then you must send all fields again (even unchanged ones).

PATCH → Update only the given fields.

If you only send "title", it updates only title, keeps content unchanged.

Your code is behaving more like a PATCH, because you’re updating only fields present in the body
'''

'''
DELETE Method:
Purpose: Remove a resource.
Why: To delete unwanted or obsolete data.
Example Use: Delete a user account, remove a blog post.
'''

@app.delete("/deletepost/{id}")
def delete_post(id: int):
    for index, post in enumerate(posts):
        if post["id"] == id:
            posts.pop(index)
            return {"message": "Post Deleted Successfully!", "data": posts}
    return {"message": "Post Not Found!"}  

# ---------------- API Testing Guide ---------------- #
# 1. GET Requests
#    - Get welcome message:
#        http://127.0.0.1:8000/
#    - Get all posts:
#        http://127.0.0.1:8000/posts
#    - Get specific post by ID:
#        http://127.0.0.1:8000/posts/2
#
# 2. POST Request
#    - URL: http://127.0.0.1:8000/createpost
#    - Method: POST
#    - Body (raw JSON):
#        {
#          "id": 5,
#          "title": "My Fifth Post",
#          "content": "This is the content of 5th post"
#        }
#
# 3. PUT Request
#    - URL: http://127.0.0.1:8000/updatepost/2
#    - Method: PUT
#    - Body (raw JSON):
#        {
#          "title": "Updated Title",
#          "content": "Updated Content"
#        }
#
# 4. PATCH Request
#    - URL: http://127.0.0.1:8000/updatepost/3
#    - Method: PATCH
#    - Body (raw JSON):
#        {
#          "title": "Partially Updated Title"
#        }
#
# 5. DELETE Request
#    - URL: http://127.0.0.1:8000/deletepost/1
#    - Method: DELETE
#
# --------------------------------------------------- #
# Note: Use tools like Postman or curl to test POST, PUT, PATCH, DELETE requests.
