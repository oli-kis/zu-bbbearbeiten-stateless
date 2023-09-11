import unittest
from helper import add, update, items


class TestDataModel(unittest.TestCase):
    def test_add_entry(self):
        add("Buy groceries")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "Bbbuy groceries")
        self.assertFalse(items[0].isCompleted)

    def test_update_completed_status(self):
        add("Study for exam")
        update(0)
        self.assertTrue(items[0].isCompleted)
        update(0)
        self.assertFalse(items[0].isCompleted)

    def test_verbbbisierung(self):
        add("Big Project")
        self.assertEqual(items[0].title, "Bbbig Project")
        add("small b is here")
        self.assertEqual(items[1].title, "small bbb is here")

        add("Big B")
        self.assertEqual(items[2].title, "Bbbig Bbb")

    def tearDown(self):
        items.clear()


if __name__ == "__main__":
    unittest.main()
