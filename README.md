# Project Title

# Assignment Submission Portal

# Description

A backend system for managing assignment submissions by users and admins.
# Technologies Used
Python
Django 
MongoDB
RESTful API

# Setup Instructions
Clone the repository:


# Create a virtual environment:
python -m venv venv
source venv/bin/activate


# Install dependencies:
pip install -r requirements.txt


# Set up MongoDB:

Ensure you have MongoDB running locally or provide a MongoDB Atlas connection string.
# Run the application: python manage.py runserver
# API Endpoints
# User Endpoints:
POST /register - Register a new user.
POST /login - User login.
POST /uploadassignments - Upload an assignment.
GET /admins - Fetch all admins.
# Admin Endpoints:
POST /register - Register a new admin.
POST /login - Admin login.
GET /assignments - View assignments tagged to the admin.
POST /assignments/:id/accept - Accept an assignment.
POST /assignments/:id/reject - Reject an assignment.

# Validation and Error Handling
Input Validation:

All inputs to the API endpoints are validated using serializers. This ensures that only valid data is processed.
For example, when a user registers or uploads an assignment, the data is passed through a serializer that checks for required fields, data types, and any other constraints.
Error Messages:

When validation fails, the serializer returns specific error messages that inform the user about what went wrong. Here are examples of common validation errors:
