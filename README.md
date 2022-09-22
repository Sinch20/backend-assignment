
# backend-assignment
### True Value Access - Backend Assignment
Create REST APIs using Python (Flask, Django, any other web framework of your choice) for managing the user’s data.
The rest framework used is Django and the database selected for managing the user data is SQLite. 
The user data has been taken from the sample data already given. It is assumed as employee (user) data. 
The API has the following functionalities:

#### 1. List users 
This functionality lists all the users in the database (There are 500 users in the given sample data). The endpoint for this is taken as - '/api/users GET'

#### 2. Search for a user by name 
Search functionality has been implemented which checks for the first_name and last_name and renders the user whose name matches.
Example Response: for searching a particular name (first name or last name). Here we are searching for Josephine
```js
   [
   {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
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

![image](https://user-images.githubusercontent.com/83527617/190898445-86ab0966-2866-441c-9267-d74f258abda6.png)


#### 3. Sort list by field name
Django filters have been used (ordering class) which gives a drop down box in a 'filters' option of ascending and descending order of all the field names which can be chosen. Also the endpoint can be changed as '/api/usersearch?ordering=company_name'. Here, url has been made as usersearch.
![image](https://user-images.githubusercontent.com/83527617/190898851-83ece6a0-7fb4-4bdc-a4ed-8b8c3d906894.png)


#### 4. Pagination of users list 
Pagination has been done where there are page numbers for listing the users. Limits and offsets have been applied which gives the limit of the number of users to be listed in a particular page. The endpoint created for pagination is 'api/usersearch?limit=3&offset=4'.
![image](https://user-images.githubusercontent.com/83527617/190898828-c6aedbf7-06cf-4799-a29b-44e0bf08928a.png)

 
#### 5. Create new user (/api/users - POST) 
New users are created
![image](https://user-images.githubusercontent.com/83527617/190898747-142c6d09-5c47-4a3e-bf1d-d868d45f87a4.png)
```js
[
    {
        "id": 502,
        "first_name": "Chanel",
        "last_name": "Motley",
        "company_name": "Affiliated With Travelodge",
        "city": "Orlando",
        "state": "FL",
        "zip": 32804,
        "email": "chauncey_motley@aol.com",
        "web": "http://www.affiliatedwithtravelodge.com",
        "age": 32
    }
]
```

#### 6. Get detail of a user (/api/users/ - GET) 
Using the id the details of the user can be fetched. The endpoint is '/api/users/23'. Here <id> is 23. 
![image](https://user-images.githubusercontent.com/83527617/190898957-f10a60f8-249e-4e5a-994b-c1dd330480df.png)

Example Response: for getting 
```js
    {
    "id": 23,
    "first_name": "Willard",
    "last_name": "Kolmetz",
    "company_name": "Ingalls, Donald R Esq",
    "city": "Irving",
    "state": "TX",
    "zip": 75062,
    "email": "willard@hotmail.com",
    "web": "http://www.ingallsdonaldresq.com",
    "age": 75
    },
```

#### 7. Update details of a user (/api/users/ - PUT) 
Details of the user can be updated
![image](https://user-images.githubusercontent.com/83527617/190898903-baa09fdf-2dae-49e1-a4e4-a46a4125100f.png)


#### 8. Delete a user (/api/users/ - DELETE) 
Details of a user can be deleted by selecting the id of the user. The endpoint is '/api/users/3'. Here <id> is 3. 
```js
HTTP 200 OK
Allow: DELETE, OPTIONS, GET, PUT
Content-Type: application/json
Vary: Accept

"User deleted successfully"
```

### How to setup and run this project:-
1) Install the latest version of Python. 
2) Install MySQL server and workbench 
3) Install Django and Django rest framework
4) Install VS Code 
5) create .env file and and connect the framework to database with fileds like Database name, user,password and host.
6) run the project using startapp and make a folder called base (in our case the name is base).
