import unittest
from unittest.mock import patch
from notificationService.notification import send_notification

class NotificationTestCase(unittest.TestCase):
    @patch('notificationService.notification.sns_client')
    def test_send_notification(self, mock_sns_client):
        user = {"name": "John Doe", "email": "john@example.com"}
        food_details = {"item": "Apples", "quantity": 10, "location": (37.7749, -122.4194)}

        send_notification(user, food_details)

        mock_sns_client.publish.assert_called_once_with(
            TopicArn='your-topic-arn',
            Message=f"New surplus food item available: {food_details['item']}, Quantity: {food_details['quantity']}, Location: {food_details['location']}",
            Subject='New Surplus Food Item'
        )

if __name__ == '__main__':
    unittest.main()
