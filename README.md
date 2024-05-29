## How to Run the API

1. **Setting up Virtual Environment:**
   - This API has been tested in Python 3.11, but it will most likely work in lower Python versions. Create a virtual environment using:
     ```
     python3.11 -m venv venv
     ```
   - Activate with:
     ```
     source venv/bin/activate
     ```

2. **Install Requirements:**
   - Install the requirements using:
     ```
     pip install -r requirements.txt
     ```

3. **Running the API Locally:**
   - Run the API locally with:
     ```
     uvicorn app:app --reload
     ```
   - It will serve the app on localhost, port 8000.

3. **Running the tests :**
   - Run the unit tests:
     ```
     pytest test_app.py
     ```


## Suggested Workflow

- **Creating a New Pull Request (PR):**
  1. Switch to the main branch:
     ```
     git checkout main
     ```
  2. Pull the latest changes:
     ```
     git pull
     ```
  3. Create a new branch for your feature with an appropriate description:
     ```
     git checkout -b feature/description
     ```

- **Adding and Committing Changes:**
  - Add changes:
    ```
    git add .
    ```
  - Commit changes with a descriptive message:
    ```
    git commit -m 'named changes'
    ```

- **Pushing Changes and Creating Pull Requests:**
  - Push changes to the remote repository:
    ```
    git push
    ```
  - Create a pull request against the main branch to merge your changes.
  
---

Feel free to contribute and improve this project! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.
