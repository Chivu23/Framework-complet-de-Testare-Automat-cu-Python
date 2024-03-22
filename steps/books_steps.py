from pages.books_page import BooksPage
from behave import *

books_page = BooksPage()


@when('books: I click the login button')
def step_impl(context):
    books_page.click_login_button()