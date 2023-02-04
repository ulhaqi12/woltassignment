# Wolt Assignment for Summer Internship 2023

This is a private repository containing the solution of Assignment provided by Wolt for Engineering Intern in Summer 2023.

Python 3.9 or higher is required. More specifically this code was written in environment having Python 3.9.15

## RUN

After installing Python 3.9 or higher and pulling this repository, Create a virtual environment using following command.

```
$ python3 -m venv .wolt
```

A virtual environment named '.wolt' will be created in your current working directory. To install all the required packages. Run the following command.

```
$ pip install -r requirements.txt
```

All the required packages will be installed in the virtual environment and the code will run without any error. To run application, first you need to run the Flask api server in your machine that can listen to requests. To run server, Run the following command.

```angular2html
$ python api.py
```

This will run server on specific port, Check the url and port number in 'run.py' It should be same. To run, open the 'run.py' and change the input values for delivery information as you want and run the script by running this command.

```
$ python run.py
```

## Test
This repository also contains the testing code for this delivery fee calculator. To test all the functionalities, Run the following command.

```
$ pytest tests.py
```

## Descriptions of Files

``````
delivery_fee.py - This file contains all the required code to calculate the delivery fee for an order.

api.py - This file contains the implementation of Flask api that receives the request.

tests.py - This file contains all the test for main functionality of the code.

run.py - This file contains the code to generate an api request based on an order information to calculate delivery fee.

requirements.txt - This file contains the information about all the required packages to run the application.
``````

### Author(s)

Ikram Ul Haq
