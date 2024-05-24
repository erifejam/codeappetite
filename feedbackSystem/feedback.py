import sqlite3

def submit_feedback(user_id, food_id, rating, feedback_text):
    """
    Submit feedback and rating for a food item.

    Args:
        user_id (int): ID of the user submitting the feedback.
        food_id (int): ID of the food item.
        rating (int): Rating score (1-5).
        feedback_text (str): Feedback text.

    Returns:
        bool: True if feedback was submitted successfully, False otherwise.
    """
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO feedback (user_id, food_id, rating, feedback_text) VALUES (?, ?, ?, ?)",
                  (user_id, food_id, rating, feedback_text))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error submitting feedback: {e}")
        return False

def get_feedback(food_id):
    """
    Get feedback and ratings for a food item.

    Args:
        food_id (int): ID of the food item.

    Returns:
        list: A list of feedback and ratings for the specified food item.
    """
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT f.rating, f.feedback_text, u.name FROM feedback f JOIN users u ON f.user_id = u.id WHERE f.food_id = ?", (food_id,))
    feedback_list = c.fetchall()
    conn.close()
    return feedback_list
