from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookAPITest(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create and assign token to the user
        self.token = Token.objects.create(user=self.user)

        # Include the token in the request headers for authentication
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create an author and book
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            publication_year=2021
        )

        # URLs
        self.list_url = reverse('book-list')  # Replace 'book-list' with the actual URL name for listing books
        self.detail_url = reverse('book-detail', args=[self.book.id])  # Replace with the correct URL name for detail view
        self.create_url = reverse('book-create')  # Replace with your actual create view URL name

    def test_create_book(self):
        # Test creating a new book
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_year': 2020
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_list_books(self):
        # Test listing all books
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_book(self):
        # Test retrieving a single book
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        # Test updating an existing book
        data = {
            'title': 'Updated Title',
            'author': self.author.id,
            'publication_year': 2022
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
