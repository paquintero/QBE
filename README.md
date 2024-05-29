# README

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
