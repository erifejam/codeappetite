import boto3

sns_client = boto3.client('sns')
ses_client = boto3.client('ses')

def send_notification(user, food_details):
    """
    Send a notification to the user about the surplus food.

    Args:
        user (dict): User details, including email or other contact information.
        food_details (dict): Details of the surplus food item.
    """
    # Implement the logic to send notifications using AWS SNS, SES, or other services
    # Example implementation using AWS SNS
    message = f"New surplus food item available: {food_details['item']}, Quantity: {food_details['quantity']}, Location: {food_details['location']}"
    sns_client.publish(
        TopicArn='your-topic-arn',
        Message=message,
        Subject='New Surplus Food Item'
    )
