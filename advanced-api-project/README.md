# Book API Documentation

This API provides endpoints for managing books in our library system.

## Endpoints

### List Books
- URL: `/api/books/`
- Methods: GET
- Permissions: Read access for all, write access for authenticated users only

### Retrieve a Book
- URL: `/api/books/<int:pk>/`
- Methods: GET
- Permissions: Read access for all, write access for authenticated users only

### Create a Book
- URL: `/api/books/create/`
- Method: POST
- Permissions: Authenticated and Admin users only

### Update a Book
- URL: `/api/books/update/<int:pk>/`
- Methods: PUT, PATCH
- Permissions: Authenticated users only

### Delete a Book
- URL: `/api/books/delete/<int:pk>/`
- Method: DELETE
- Permissions: Authenticated and Admin users only

## Custom Behaviors

- When creating or updating a book, the API automatically sets the `created_by` or `updated_by` field to the current user.
- List view supports pagination to display 10 books per page and filtering is set to allow filtering by `name`, `author` or `publication_year`.
- Detail view provides full information about a single book.
