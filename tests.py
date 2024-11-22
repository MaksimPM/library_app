import unittest
from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library("test_storage.json")

    def tearDown(self):
        self.library.books = []
        self.library._save_books()

    def test_add_book(self):
        book = self.library.add_book("Test Book", "Test Author", 2024)
        self.assertEqual(book.title, "Test Book")

    def test_remove_book(self):
        book = self.library.add_book("Test Book", "Test Author", 2024)
        self.assertTrue(self.library.remove_book(book.id))

    def test_search_books(self):
        self.library.add_book("Searchable Book", "Author", 2024)
        results = self.library.search_books("Searchable")
        self.assertEqual(len(results), 1)

    def test_update_status(self):
        book = self.library.add_book("Test Book", "Test Author", 2024)
        self.assertTrue(self.library.update_status(book.id, "выдана"))
        self.assertEqual(book.status, "выдана")


if __name__ == "__main__":
    unittest.main()