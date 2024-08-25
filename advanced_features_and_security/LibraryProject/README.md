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


# DETAIL EXPLANATION OF THE SECURITY MEASURES IMPLEMENTED

# Enables the X-XSS-Protection header to prevent cross-site scripting (XSS) attacks.
# This setting tells the browser to block pages that try to perform XSS.
SECURE_BROWSER_XSS_FILTER = True

# Prevents the site from being displayed in a frame on other websites, protecting against clickjacking attacks.
# 'DENY' means the site cannot be embedded into a frame at all.
X_FRAME_OPTIONS = 'DENY'

# Adds the X-Content-Type-Options: nosniff header to responses, which prevents browsers from interpreting files as a different MIME type.
# This helps protect against attacks where a file is interpreted differently than its actual type.
SECURE_CONTENT_TYPE_NOSNIFF = True

# SECURE_PROXY_SSL_HEADER: This setting tells Django to trust the X-Forwarded-Proto header
# that comes from our proxy. We use this when the proxy handles SSL termination, and the
# Django app is actually receiving plain HTTP traffic but needs to know that the original
# request was via HTTPS.
# Proxy SSL Header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# Ensures that the CSRF cookie is only sent over HTTPS, enhancing the security of the CSRF protection.
# This setting should be enabled when your site is served over HTTPS.
CSRF_COOKIE_SECURE = True

# Ensures that the session cookie is only sent over HTTPS, preventing it from being sent over insecure connections.
# This setting should also be enabled when your site is served over HTTPS.
SESSION_COOKIE_SECURE = True

# Redirects all HTTP requests to HTTPS, ensuring that all communication with the server is encrypted.
# This is important to prevent man-in-the-middle attacks and to ensure data privacy.
SECURE_SSL_REDIRECT = True

# Enables HTTP Strict Transport Security (HSTS) for a specified period (in seconds).
# It forces browsers to communicate only over HTTPS and helps prevent protocol downgrade attacks.
SECURE_HSTS_SECONDS = 3600  # 1 hour

# Applies HSTS to all subdomains, ensuring that they are also protected by HTTPS.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allows the site to be included in browsers' preload lists, which ensures that HSTS is applied from the first visit.
# This setting should only be used if you are confident that your site will always support HTTPS.
SECURE_HSTS_PRELOAD = True

# Defines the Content Security Policy (CSP) for the site, specifying which sources are allowed for content like scripts, styles, and images.
# 'self' means that only content from the same origin is allowed.
CSP_DEFAULT_SRC = ("'self'",)

# Specifies the allowed sources for JavaScript. This allows scripts from the site's own domain and from ajax.googleapis.com.
CSP_SCRIPT_SRC = ("'self'", 'ajax.googleapis.com')

# Specifies the allowed sources for CSS styles. This allows styles from the site's own domain and from fonts.googleapis.com.
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')

# Specifies the allowed sources for images. This allows images from the site's own domain and data URIs.
CSP_IMG_SRC = ("'self'", 'data:')


Security Measures Implemented:

HTTPS Enforcement: All HTTP traffic is redirected to HTTPS, ensuring encrypted communication between the client and server.
HSTS: Instructs browsers to only access the site over HTTPS for a year, including subdomains, and allows preloading.
Secure Cookies: Session and CSRF cookies are set to be transmitted only over HTTPS.
Clickjacking Protection: X-Frame-Options header set to DENY, preventing the site from being framed.
Content Type Sniffing Prevention: Stops browsers from MIME-sniffing responses.
XSS Protection: Enables the browser's built-in XSS filter.

These measures significantly enhance the security of the application by ensuring encrypted communication, preventing various types of attacks (like MITM, session hijacking, clickjacking, and XSS), and instructing browsers to implement stricter security policies.
