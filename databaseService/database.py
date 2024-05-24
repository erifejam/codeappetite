import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
surplus_table = dynamodb.Table('surplus_food')
needs_table = dynamodb.Table('user_needs')

def add_surplus_food(food_details):
    try:
        response = surplus_table.put_item(
            Item={
                'id': food_details['id'],
                'name': food_details['name'],
                'description': food_details['description'],
                'location': food_details['location'],
                'quantity': food_details['quantity']
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Surplus food added successfully")

def add_user_need(user_need):
    try:
        response = needs_table.put_item(
            Item={
                'id': user_need['id'],
                'name': user_need['name'],
                'description': user_need['description'],
                'location': user_need['location'],
                'quantity': user_need['quantity']
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("User need added successfully")

def get_surplus_food():
    try:
        response = surplus_table.scan()
        surplus_food = response['Items']
    except ClientError as e:
        print(e.response['Error']['Message'])
        surplus_food = []
    else:
        return surplus_food

def get_user_needs():
    try:
        response = needs_table.scan()
        user_needs = response['Items']
    except ClientError as e:
        print(e.response['Error']['Message'])
        user_needs = []
    else:
        return user_needs

def store_feedback(user_id, food_id, rating, feedback_text):
    try:
        feedback_table = dynamodb.Table('feedback')
        response = feedback_table.put_item(
            Item={
                'user_id': user_id,
                'food_id': food_id,
                'rating': rating,
                'feedback_text': feedback_text
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return False
    else:
        print("Feedback stored successfully")
        return True

def get_feedback_for_food(food_id):
    try:
        feedback_table = dynamodb.Table('feedback')
        response = feedback_table.query(
            KeyConditionExpression=Key('food_id').eq(food_id)
        )
        feedback_list = response['Items']
    except ClientError as e:
        print(e.response['Error']['Message'])
        feedback_list = []
    else:
        return feedback_list
