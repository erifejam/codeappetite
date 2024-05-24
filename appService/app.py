import os
from flask import Flask, render_template, request
from geolocationService.geolocation import match_locations
from notificationService.notification import send_notification
from flask import Flask, render_template, request
import os

from databaseService.database import (
    add_surplus_food,
    add_user_need,
    get_surplus_food,
    get_user_needs,
    store_feedback,
    get_feedback_for_food,
)
from geolocationService.geolocation import match_locations
from notificationService.notification import send_notification
from feedbackSystem.feedback import submit_feedback, get_feedback

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_surplus", methods=["POST"])
def add_surplus():
    food_details = request.form
    add_surplus_food(food_details)
    matched_users = match_locations(food_details["location"])
    for user in matched_users:
        send_notification(user, food_details)
    return "Surplus food added successfully"

@app.route("/add_need", methods=["POST"])
def add_need():
    user_need = request.form
    add_user_need(user_need)
    return "User need added successfully"

@app.route("/get_surplus")
def get_surplus():
    surplus_food_list = get_surplus_food()
    feedback_list = [get_feedback_for_food(item['id']) for item in surplus_food_list]
    return render_template("surplus_list.html", surplus_food=surplus_food_list, feedback_list=feedback_list)

@app.route("/get_needs")
def get_needs():
    user_needs_list = get_user_needs()
    return render_template("needs_list.html", user_needs=user_needs_list)

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback_route():
    user_id = request.form.get("user_id")
    food_id = request.form.get("food_id")
    rating = request.form.get("rating")
    feedback_text = request.form.get("feedback_text")
    success = submit_feedback(user_id, food_id, rating, feedback_text)
    if success:
        return "Feedback submitted successfully"
    else:
        return "Failed to submit feedback"

@app.route("/get_feedback/<food_id>")
def get_feedback_route(food_id):
    feedback_list = get_feedback(food_id)
    return render_template("feedback_list.html", feedback_list=feedback_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
