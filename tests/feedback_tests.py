import unittest
from unittest.mock import patch
from feedbackSystem.feedback import submit_feedback, get_feedback

class FeedbackTestCase(unittest.TestCase):
    @patch('feedbackSystem.feedback.sqlite3')
    def test_submit_feedback(self, mock_sqlite3):
        user_id = 1
        food_id = 2
        rating = 4
        feedback_text = "Fresh and delicious!"

        result = submit_feedback(user_id, food_id, rating, feedback_text)

        self.assertTrue(result)
        mock_sqlite3.connect.assert_called_once_with('database.db')
        mock_cursor = mock_sqlite3.connect.return_value.cursor.return_value
        mock_cursor.execute.assert_called_once_with("INSERT INTO feedback (user_id, food_id, rating, feedback_text) VALUES (?, ?, ?, ?)", (user_id, food_id, rating, feedback_text))

    @patch('feedbackSystem.feedback.sqlite3')
    def test_get_feedback(self, mock_sqlite3):
        food_id = 2
        mock_cursor = mock_sqlite3.connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [
            (4, "Fresh and delicious!", "John Doe"),
            (3, "Could be better", "Jane Smith"),
        ]

        feedback_list = get_feedback(food_id)

        self.assertEqual(feedback_list, mock_cursor.fetchall.return_value)
        mock_sqlite3.connect.assert_called_once_with('database.db')
        mock_cursor.execute.assert_called_once_with("SELECT f.rating, f.feedback_text, u.name FROM feedback f JOIN users u ON f.user_id = u.id WHERE f.food_id = ?", (food_id,))

if __name__ == '__main__':
    unittest.main()
