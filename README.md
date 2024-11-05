# Chocolate House Management System

A Django-based application for managing seasonal chocolate flavors, ingredient inventory, and customer suggestions for a fictional chocolate house.

## Features

1. **Seasonal Flavor Offerings**: Track seasonal chocolate flavors with descriptions.
2. **Ingredient Inventory**: Manage inventory with quantities and units.
3. **Customer Suggestions**: Store customer flavor suggestions and allergy concerns.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- SQLite (default Django database)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/chocolate-house.git
   cd chocolate-house
2. Install required packages:
    pip install -r requirements.txt
3. Set up the database:
    python manage.py makemigrations
    python manage.py migrate
4. Create a superuser for the admin interface:
    python manage.py createsuperuser
5. Run the server:
    python manage.py runserver
6. Visit http://127.0.0.1:8000/ in your browser to view the application.

Usage:

Flavors: View, add, and edit seasonal chocolate flavors.
Ingredients: Manage the inventory of ingredients with quantity and unit.
Customer Suggestions: Store customer flavor suggestions and their allergy concerns.

Project Structure

chocoapp/ – Main application folder with views, models, forms, and templates.
templates/chocoapp/ – Contains HTML templates for UI.
urls.py – URL routing for each page.
views.py – View functions to handle requests and responses.
