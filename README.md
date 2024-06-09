# Run Locally

- Clone the repository

- Create Virtual Environment

  ```
  $ pip install venv
  $ python -m venv venv
  ```

  On Windows, run:

  ```
  $ venv\Scripts\activate.bat
  ```

- install dependencies
  ```
  $ pip install -r requirements.txt
  ```
- finally, You can run the project 🎉
  ```
  $ python manage.py runserver
  ```
  Open http://localhost:8000 to view it in the browser.

# Create System Admin

- System admin is necessary to access admin panel: `localhost:8000/admin`
- `python manage.py createsuperuser`

# Blog

- Layout file path `blog/templates/layout.html`
- You'll need to add your github, mail, linkedin link to the icons [Static work]
