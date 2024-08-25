Welcome to the “Introduction to Django” project. This project is tailored to help you gain hands-on experience with Django, one of the most popular web frameworks for building robust web applications. Throughout this project, you will set up a Django development environment, learn about Django models and ORM, and explore the Django admin interface.


# Permissions and Groups Setup

## Custom Permissions
Custom permissions have been added to the `Book` model:
- `can_view`: Permission to view books.
- `can_create`: Permission to create new books.
- `can_edit`: Permission to edit existing books.
- `can_delete`: Permission to delete books.

## Groups Configuration
Three groups have been created to manage access control:
- **Editors**: Can create and edit books.
- **Viewers**: Can only view books.
- **Admins**: Can create, edit, view, and delete books.

## Applying Permissions in Views
Permissions are enforced in the following views:
- `book_list`: Requires `can_view`.
- `create_book`: Requires `can_create`.
- `edit_book`: Requires `can_edit`.
- `delete_book`: Requires `can_delete`.

## Testing
To test, assign users to the appropriate groups and verify that permissions are applied as expected.
