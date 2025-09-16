# Blogging-API
Blogging API built with Python, Django, and MySQL
A Django REST Framework (DRF) based Blogging API that allows users to register, create posts, comment, and follow/unfollow other users. This project demonstrates full-stack backend skills including user authentication, permissions, and relationships between models.

Features
1. User Authentication
- User registration with username, email, and password.
- JWT-based authentication for secure login and access.
- Supports retrieving and updating user information.

2. Profile Management
- Automatic profile creation upon user registration.
- View all user profiles (GET /auth/profiles/).
- Users can update their own profiles.
- Profiles include:
- user (username)
- email
- bio
- profile_picture
- followers & following
  
3. Posts
- Create, list, retrieve, update, and delete posts.
- Only authors can update or delete their posts.
  Posts include:
- author
- title
- content
- created_at & updated_at

4. Comments
- Create, list, retrieve, update, and delete comments.
- Only authors can update or delete their comments.
- Comments are tied to posts and users.

5. Follow / Unfollow Users
Logged-in users can follow or unfollow other users’ profiles.
Endpoints:
- POST /auth/profiles/<profile_id>/follow/
- POST /auth/profiles/<profile_id>/unfollow/
- Prevents following/unfollowing self.
- Shows followers and following in each profile.

6. Permissions
- Authenticated users can create/update their content.
- Read-only access for unauthenticated users.
- Proper error handling for unauthorized actions.

- API Endpoints
User

Method	Endpoint	Description
POST	/auth/register/	Register a new user
POST	/auth/jwt/create/	Login and get JWT token

Read-only access for unauthenticated users.

Proper error handling for unauthorized actions.

API Endpoints
User
Method	Endpoint	Description
POST	/auth/register/	Register a new user
POST	/auth/jwt/create/	Login and get JWT token

Profiles
Method	Endpoint	Description
GET	/auth/profiles/	List all profiles
GET	/auth/profiles/<id>/	Retrieve a profile
PUT	/auth/profiles/<id>/	Update your profile
POST	/auth/profiles/<id>/follow/	Follow a user
POST	/auth/profiles/<id>/unfollow/	Unfollow a user

Posts
Method	Endpoint	Description
GET	/auth/posts/	List all posts
POST	/auth/posts/	Create a post
GET	/auth/posts/<id>/	Retrieve post details
PUT	/auth/posts/<id>/	Update a post (author only)
DELETE	/auth/posts/<id>/	Delete a post (author only)

Comments
Method	Endpoint	Description
GET	/auth/comments/	List all comments
POST	/auth/comments/	Create a comment
GET	/auth/comments/<id>/	Retrieve a comment
PUT	/auth/comments/<id>/	Update a comment (author only)
DELETE	/auth/comments/<id>/	Delete a comment (author only)

Technologies
- Python 3.12
- Django 4.x
- Django REST Framework (DRF)
- PostgreSQL (or SQLite for development)
- JWT Authentication
