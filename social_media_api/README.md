


# API Documentation: Posts and Comments

## Base URL
`/api/`

## Authentication
Most endpoints require authentication. Include your authentication token in the header of your requests:
```
Authorization: Token your_token_here
```

## Endpoints

### Posts

#### List Posts
- **URL**: `/posts/`
- **Method**: GET
- **Auth required**: No
- **Permissions**: None
- **URL Params**: 
  - `page=[integer]` (optional)
  - `search=[string]` (optional)
  - `title=[string]` (optional)
- **Success Response**: 
  - Code: 200
  - Content: 
    ```json
    {
      "count": 123,
      "next": "http://api.example.org/posts/?page=4",
      "previous": "http://api.example.org/posts/?page=2",
      "results": [
        {
          "id": 1,
          "author": {
            "id": 1,
            "username": "john_doe"
          },
          "title": "Sample Post",
          "content": "This is a sample post content.",
          "created_at": "2024-09-19T10:00:00Z",
          "updated_at": "2024-09-19T10:00:00Z",
          "comments": []
        },
        // ... more posts
      ]
    }
    ```

#### Create Post
- **URL**: `/posts/`
- **Method**: POST
- **Auth required**: Yes
- **Permissions**: IsAuthenticated
- **Data constraints**:
  ```json
  {
    "title": "[1 to 200 chars]",
    "content": "[1 to 1000 chars]"
  }
  ```
- **Success Response**:
  - Code: 201
  - Content: `{<post_object>}`

#### Retrieve Post
- **URL**: `/posts/<id>/`
- **Method**: GET
- **Auth required**: No
- **URL Params**: None
- **Success Response**:
  - Code: 200
  - Content: `{<post_object>}`

#### Update Post
- **URL**: `/posts/<id>/`
- **Method**: PUT/PATCH
- **Auth required**: Yes
- **Permissions**: IsAuthorOrReadOnly
- **Data constraints**: Same as POST
- **Success Response**:
  - Code: 200
  - Content: `{<updated_post_object>}`

#### Delete Post
- **URL**: `/posts/<id>/`
- **Method**: DELETE
- **Auth required**: Yes
- **Permissions**: IsAuthorOrReadOnly
- **Success Response**:
  - Code: 204

### Comments

#### List Comments for a Post
- **URL**: `/posts/<post_id>/comments/`
- **Method**: GET
- **Auth required**: No
- **Permissions**: None
- **URL Params**: 
  - `page=[integer]` (optional)
- **Success Response**: 
  - Code: 200
  - Content: List of comment objects

#### Create Comment
- **URL**: `/posts/<post_id>/comments/`
- **Method**: POST
- **Auth required**: Yes
- **Permissions**: IsAuthenticated
- **Data constraints**:
  ```json
  {
    "content": "[1 to 500 chars]"
  }
  ```
- **Success Response**:
  - Code: 201
  - Content: `{<comment_object>}`

#### Retrieve Comment
- **URL**: `/posts/<post_id>/comments/<id>/`
- **Method**: GET
- **Auth required**: No
- **Success Response**:
  - Code: 200
  - Content: `{<comment_object>}`

#### Update Comment
- **URL**: `/posts/<post_id>/comments/<id>/`
- **Method**: PUT/PATCH
- **Auth required**: Yes
- **Permissions**: IsAuthorOrReadOnly
- **Data constraints**: Same as POST
- **Success Response**:
  - Code: 200
  - Content: `{<updated_comment_object>}`

#### Delete Comment
- **URL**: `/posts/<post_id>/comments/<id>/`
- **Method**: DELETE
- **Auth required**: Yes
- **Permissions**: IsAuthorOrReadOnly
- **Success Response**:
  - Code: 204

## Error Responses

- **Condition**: If a request is made with invalid data or to a non-existent resource.
- **Code**: 400 BAD REQUEST
- **Content**: `{ "error": "Error message here" }`

- **Condition**: If a request is made without proper authentication.
- **Code**: 401 UNAUTHORIZED
- **Content**: `{ "detail": "Authentication credentials were not provided." }`

- **Condition**: If a request is made without proper permissions.
- **Code**: 403 FORBIDDEN
- **Content**: `{ "detail": "You do not have permission to perform this action." }`

- **Condition**: If a request is made to a non-existent resource.
- **Code**: 404 NOT FOUND
- **Content**: `{ "detail": "Not found." }`