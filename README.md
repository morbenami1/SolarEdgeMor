# Mor Benami - Django Blog App

This is a SolarEdge Django-based blog project application that fetches posts and comments from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)
and displays them.

## Features

- **Post List**: Displays all posts fetched from the JSONPlaceholder API with a snippet of the content.
- **Post Detail View**: Allows users to click on a post to view its full content and associated comments.
- **Pagination**: Divides the posts into multiple pages for better navigation.
- **Responsive Design**: Styled using custom CSS for a clean and user-friendly interface.



## Installation

1. **Clone the Repository**

   Use the following command to clone the repository:

   ```bash
   git clone https://github.com/morbenami1/SolarEdgeMor.git
   cd SolarEdge_project

2. **Install Dependencies**
   ```bash
    pip install -r requirements.txt
   
3. **Run Database Migrations**
   ```bash
   python manage.py migrate
   
4. **Run the Development Server**
   ```bash 
    python manage.py runserver
   
5. **Access the Application**

   Open your web browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

