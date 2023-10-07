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

**Main app** : backend/app/main.py

**Services** : backend/app/services

**Tests**   : backend/app/test_main.py

**product_names.json** - Json File carrying the brand representations and their original names.Only those product patterns are recognised during pattern detection.Otherwise error message is returned for the
product

**config.py**        -  Common variables that are used across the module

sample_input_for_test -Python file defining variables for test inputs and outputs

**Services:**

**api_service.py** is responsible for initialising and defining the layout.For a given layout,it has list of product arrangements.

**arrange_service.py** is responsible for deducing the pattern of a given brand and identifies it's shape as RECTANGLE,SQUARE,POLYGON etc...

It also identifies the location of the product group as top left,right,etc..
 


**TESTS:**

Sample inputs and expected output are verified through the test file "backend/app/test_main.py"

COMMAND TO EXECUTE TESTS: python -m pytest



