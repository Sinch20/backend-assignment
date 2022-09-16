# Backend Assignment

**Assignment:** True Value Access - Create REST APIs using Python (Flask, Django, any other web framework of your choice) for managing the user’s data.
The rest framework used is Django and the database selected for managing the user data is MySQL. 
The user data has been taken from the sample data already given. It is assumed as employee (user) data. 
The API has the following functionalities:
- list users - This functionality lists all the users in the database (There are 500 users in the given sample data). The endpoint for this is taken as - **'/api/users GET'**
- search for a user by name - Search functionality has been implemented which checks for the first_name and last_name and renders the user whose name matches. 
- sort list by field name - Django filters have been used (ordering class) which gives a drop down box in a 'filters' option of ascending and descending order of all the field names which can be chosen. Also the endpoint can be changed as **'/api/usersearch?ordering=company_name'**. Here, url has been made as usersearch. 
- pagination of users list - Pagination has been done where there are page numbers for listing the users. Limits and offsets have been applied which gives the limit of the number of users to be listed in a particular page. The endpoint created for pagination is **'api/usersearch?limit=3&offset=4'**. 
- create new user (/api/users - POST) - new users are created
- get detail of a user (/api/users/ - GET) - using the id the details of the user can be fetched. The endpoint is **'/api/users/3'**. Here id is 3. 
- update details of a user (/api/users/ - PUT) - details of the user can be updated
- delete a user (/api/users/ - DELETE) - details of a user can be deleted by selecting the id of the user. The endpoint is **'/api/users/3'**. Here id is 3. 

**How to setup and run this project:- **
1) Install the latest version of Python. 
2) Install MySQL server and workbench 
3) Install Django and Django rest framework
4) Install VS Code 
5) Create .env file and and connect the framework to database with fileds like Database name, user,password and host.
6) Run the project using startapp and make a folder called base (in our case the name is base).
 

## **Task Overview**

User should have the following attributes:-

```
ID
First Name
Last Name
Company Name
Age
City
State
Zip
Email
Web
```

Application should have the following endpoints:

- `/api/users - GET` - To list the users

  - Response with HTTP status code 200 on success

    ```json
    [
      {
        "id": 1,
        "first_name": "James",
        "last_name": "Butt",
        "company_name": "Benton, John B Jr",
        "city": "New Orleans",
        "state": "LA",
        "zip": 70116,
        "email": "jbutt@gmail.com",
        "web": "http://www.bentonjohnbjr.com",
        "age": 70
      },
      {
        "id": 2,
        "first_name": "Josephine",
        "last_name": "Darakjy",
        "company_name": "Chanay, Jeffrey A Esq",
        "city": "Brighton",
        "state": "MI",
        "zip": 48116,
        "email": "josephine_darakjy@darakjy.org",
        "web": "http://www.chanayjeffreyaesq.com",
        "age": 48
      }
    ]
    ```

  - Also, supports some query parameters:
  - page - a number for pagination
  - limit - no. of items to be returned, default limit is 5
  - name - search user by name as a substring in First Name or Last Name (Note, use substring matching algorithm/pattern to match the name). It should be case-insensitive.
  - Sort - name of attribute, the items to be sorted. By default it returns items in ascending order if this parameter exist, and if the value of parameter is prefixed with ‘-’ character, then it should return items in descending order

  Sample query endpoint:- `/api/users?page=1&limit=10&name=James&sort=-age` This endpoint should return list of 10 users whose first name or last name contains substring given name and sort the users by age in descending order of page 1.

- `/api/users - POST` - To create a new user

  - Request Payload should be like in json format :-

    ```json
    {
      "id": 2,
      "first_name": "Josephine",
      "last_name": "Darakjy",
      "company_name": "Chanay, Jeffrey A Esq",
      "city": "Brighton",
      "state": "MI",
      "zip": 48116,
      "email": "josephine_darakjy@darakjy.org",
      "web": "http://www.chanayjeffreyaesq.com",
      "age": 48
    }
    ```

  - Response with HTTP status code 201 on success
    ```json
    {}
    ```
  - This endpoint will create a new user inside the database

- `/api/users/{id} - GET` - To get the details of a user

  1. Here {id} will be the id of the user in path parameter
  1. Response with HTTP status code 200 on success

  ```json
  {
    "id": 1,
    "first_name": "James",
    "last_name": "Butt",
    "company_name": "Benton, John B Jr",
    "city": "New Orleans",
    "state": "LA",
    "zip": 70116,
    "email": "jbutt@gmail.com",
    "web": "http://www.bentonjohnbjr.com",
    "age": 70
  }
  ```

  Sample query looks like:- `/api/users/1 GET`

- `/api/users/{id} PUT` - To update the details of a user

  - Here {id} will be the id of the user in path parameter
  - Request Payload should be like in json format for updating first name, last name and age:-
    ```json
    {
      "first_name": "Josephine",
      "last_name": "Darakjy",
      "age": 48
    }
    ```
  - Response with HTTP status code 200 on success
    {}

- `/api/users/{id} DELETE` - To delete the user

  - Here {id} will be the id of the user in path parameter
  - Response with HTTP status code 200 on success

    ```json
    {}
    ```

## Resources:

- For sample data [https://datapeace-storage.s3-us-west-2.amazonaws.com/dummy_data/users.json](https://datapeace-storage.s3-us-west-2.amazonaws.com/dummy_data/users.json)

## **Instructions**

- [ ] README.md should have all the details and instructions like how to setup and run the project
- [ ] Repo should not contain irrelevant folders/files like cache files, build/dist directories etc.
- [ ] Create API documentation using Swagger or similar framework
- [ ] Follow these steps for submission:
  1. Fork the repository
  1. Create issues and work on them in their respective branches
  1. Complete the tasks while following all instructions
  1. Create MRs and merge into main branch
  1. When done, Test if all task requirements are met and instructions followed
  1. Push code to github
  1. Deploy/Host your solution
  1. Reply to the same email with the URLs for **repo**, **hosted API** and **hosted documentation** 
- For any queries please email us at [hiring@truevalueaccess.com](mailto:hiring@truevalueaccess.com)
