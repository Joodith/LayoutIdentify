**ABOUT**

An API Service using FASTAPI to analyse the arrangement of products at shops given the shelf layout with various brands arranged in some pattern and the goal is to detect the pattern(shape) and find the overall location of the products.


**STEPS FOR RUNNING IN LOCAL:**

1)Activate a virtual environment with python 3.11

2)pip install -r requirements.txt

3)Run the server using the command:   uvicorn backend.app.main:main_app --host 0.0.0.0 --port 8000

This will start the server at localhost 8000

**STEPS FOR RUNNING IN DOCKER CONTAINER:**

1)docker build -t <image_name> .

2)docker run -d -p <port_on_host>:8000 <image_name>

**IMPLEMENTATION:**

POST SERVICE FOR FINDING PATTERN OF PRODUCTS IN THE GIVEN LAYOUT:    http://localhost:8000/shape_of_brand
 
Request body:A 2D array representing shelf layout

Respose: Shape and Location of each of the arranged product pattern

**TESTS:**

Sample inputs and expected output are verified through the test file "backend/app/test_main.py"

COMMAND TO EXECUTE TESTS: python -m pytest



