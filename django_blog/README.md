# Authentication System Documentation

This Django blog project includes a comprehensive authentication system with the following features:

1. User Registration
2. User Login
3. User Logout
4. Profile Management

## Setup

1. Ensure you have Django installed: `pip install django`
2. Run migrations: `python manage.py migrate`
3. Create a superuser: `python manage.py createsuperuser`

## Features

### User Registration
- URL: `/register/`
- Users can create an account by providing a username, email, and password.
- After successful registration, users are automatically logged in.

### User Login
- URL: `/login/`
- Users can log in using their username and password.

### User Logout
- URL: `/logout/`
- Logged in users can log out, ending their session.

### Profile Management
- URL: `/profile/`
- Logged in users can view and edit their profile information.
- Currently, users can update their email, first name, and last name.

## Testing

1. Registration:
   - Navigate to `/register/`
   - Fill in the registration form and submit
   - You should be redirected to the home page and be logged in

2. Login:
   - Navigate to `/login/`
   - Enter your credentials and submit
   - You should be redirected to the home page

3. Profile Management:
   - Log in and navigate to `/profile/`
   - Update your information and submit
   - Your changes should be saved and reflected in the form

4. Logout:
   - Click the logout link or navigate to `/logout/`
   - You should be logged out and redirected to the home page

## Security

- CSRF protection is enabled for all forms
- Passwords are securely hashed using Django's default password hasher
- Always use HTTPS in production to encrypt data in transit



## Blog Post Management

This Django project includes full CRUD (Create, Read, Update, Delete) functionality for blog posts. Here's an overview of the features:

- **Viewing Posts**: All users can view the list of blog posts and individual post details.
- **Creating Posts**: Authenticated users can create new blog posts.
- **Editing Posts**: Authors can edit their own posts.
- **Deleting Posts**: Authors can delete their own posts.

### Usage

- To view all posts, navigate to the home page or `/posts/`.
- To create a new post, click the "Create New Post" button (requires authentication).
- To view a post's details, click on its title in the post list.
- To edit or delete a post, use the respective buttons on the post detail page (only available to the post's author).

### Permissions

- Viewing posts is available to all users.
- Creating posts requires user authentication.
- Editing and deleting posts are restricted to the post's author.

For more details on implementation, please refer to the `views.py`, `forms.py`, and `urls.py` files in the `blog` app.