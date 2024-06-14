README.md
markdown
Copy code
# ASCII Random RPG

This project is an ASCII-based RPG game that integrates a Django server for backend management and a web-based drawing application for visualizing different ASCII art. The project is organized into several modules with object-oriented programming principles.

## Project Structure

ASCII_Random_RPG/
├── ASCII_RPG/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── MainActivity/
│ │ ├── Battle.py
│ │ ├── Character.py
│ │ ├── Dungeon.py
│ │ ├── Inventory.py
│ │ ├── Quest.py
│ │ ├── Shop.py
│ │ ├── item.py
│ │ ├── monster.py
│ │ ├── skill.py
│ │ ├── pycache/
│ │ ├── legacy/
│ │ └── web_drawing_app/
│ │ ├── index.html
│ │ ├── styles.css
│ │ └── script.js
├── UI/
├── db.sqlite3
├── manage.py
├── static/

python
Copy code

## Setup Instructions

### Setting Up the Django Server

1. **Install Dependencies**: Ensure you have Python and Django installed. You can install Django using pip:

    ```sh
    pip install django
    ```

2. **Navigate to the Project Directory**:

    ```sh
    cd /Users/ASCII_Random_RPG
    ```

3. **Apply Migrations**:

    ```sh
    python manage.py migrate
    ```

4. **Run the Server**:

    ```sh
    python manage.py runserver
    ```
