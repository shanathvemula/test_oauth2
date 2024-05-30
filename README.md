# OAuth2 

## Setup

The first thing to do is to clone the repository:

```shell
git clone https://github.com/shanathvemula/test_oauth2.git
cd test_oauth2
```

Create a virtual environment to install dependencies in and activate it:

```shell
# Creating virtual environment
python -m venv venv

# In cmd.exe
venv\Scripts\activate.bat
```

Then install the dependencies:

```shell
(venv)$ pip install -r requirements.txt
```

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies. 

Default it will connect sqlite3 database.
For connecting Postgresql

#### * Open settings.py in test_oauth2 folder

Remove :

```shell
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Add:
```shell
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': '<Database Name>',
        'USER': '<postgres username>',
        'PASSWORD': '<postgres password>',
        'HOST': '<postgres host address>',
        'PORT': <postgres port>
    }
}
```
Run this commands in CMD:
```shell
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py createsuperuser
Username (leave blank to use '---'): <Enter username>
Email address:<Enter email address>
Password: <Enter Password>
Password (again): <Enter Password Again>
(venv)$ python manage.py runserver
```

And navigate to http://127.0.0.1:8000.

Endpoints:
```shell
1. admin/
2. o/
3. contenttypes/
4. permissions/
5. groups/
6. groups/<pk>
7. user_list/
8. user_create/
9. users/<username>
10. check_permission/
```

## 1. admin/

Admin Panel
http://127.0.0.1:8000/admin

![img.png](static/README/admin.png)

* To Login into Admin Panel

## 2. o/
Authorization Endpoints

### I. applications/

* This endpoint is helps to create applications. you create application using this link http://127.0.0.1:8000/o/applications/ 
* If you want to create the application before you need to log in admin panel

![img.png](static/README/CreateApplication.png)

* Click on the `click here` link

![img.png](static/README/CreateApplication1.png)

* Here need to save the `Client id
, Client secret` for the token generation.
  
* You need to enter name
* select Client type as `Confidential`
* select Authorization grant type as `Resource owner password-based` 
* Once we have clicked the save button. Client secret key will be hash.
* Click save button

![img.png](static/README/Application.png)


### II. token

* To get the access token.
* Here we need to utilize the client_id, client_secret 

```shell
URL : http://127.0.0.1:8000/o/token/
Request Method: POST
payload:
  grant_type = password
  username = <username>
  password = <password>
  client_id = <client_id>
  client_secret = <client_secret>
```

Example cURL Code:
```shell
curl --location 'http://127.0.0.1:8000/o/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'username=<username>' \
--data-urlencode 'password=<password>' \
--data-urlencode 'client_id=PkKyETl9a98VCTxR4b2jMBwGQNjnGRSizFCdOGvl' \
--data-urlencode 'client_secret=cgyKqn2NG3ys5Dp7WcoliDadw858cUxUlAiZ2TGnrzGrSHes6aa3fxd0hNGi4YRGWnd1SFy6xhM57ycAzkMr2gd8lVytyN9Ea1Soc6qIfEH89CsrksoiO6thq1FEMfHn'
```

Example Output:

```shell
{
    "access_token": "UuOSEQSPz53uE04SMdzbS4VGPXDxjZ",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write groups",
    "refresh_token": "hqhPDjmsTs9l92ILdKaHl25vx6FO0y"
}
```

* This access_token is used for the Authorization
* Need to pass the access_token in headers like below
    
        Authorization: Bearer <access_token>

## 3. contenttypes/

* This endpoint helps to List and create the Content Types

### I. Listing Content Types

* Getting list of Content Types

```shell
URL : http://127.0.0.1:8000/contenttypes/
Request Method: GET
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
```

Example cURL Code:

```shell
curl --location 'http://127.0.0.1:8000/contenttypes/' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ'
```

### II. Creating Content Types

* Creating a Content Types

```shell
URL : http://127.0.0.1:8000/contenttypes/
Request Method: POST
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
payload:
  {
    "app_label": "<App Label>",
    "model": "<model>",
}
```

Example cURL Code:

```shell
curl --location 'http://127.0.0.1:8000/contenttypes/' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ' \
--header 'Content-Type: application/json' \
--data '{
    "app_label": "<App Label>",
    "model": "<model>",
}'
```
## 4. permissions/

* This endpoint helps to List and create the Permissions

### I. Listing Permissions

* Getting list of Permissions

```shell
URL : http://127.0.0.1:8000/permissions/
Request Method: GET
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
```

Example cURL Code:

```shell
curl --location 'http://127.0.0.1:8000/permissions/' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ'
```

### II. Creating Permissions

* Creating a Permission

```shell
URL : http://127.0.0.1:8000/permissions/
Request Method: POST
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
payload:
  {
    "name": "<Permission Name>",
    "codename": "<Permission codename>",
    "content_type": <Content Type Id>
}
```

Example cURL Code:

```shell
curl --location 'http://127.0.0.1:8000/permissions/' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ' \
--header 'Content-Type: application/json' \
--data '{
    "name": "<Permission Name>",
    "codename": "<Permission codename>",
    "content_type": <Content Type Id>
}'
```
## 5. groups

* This endpoint helps to List and create the Group(Role)

### I. Listing Groups

* Getting list of Groups(Roles)

```shell
URL : http://127.0.0.1:8000/groups/
Request Method: GET
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
```

Example cURL Code:

```shell
curl --location 'http://127.0.0.1:8000/groups/' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ'```
```

* The Output will be List of Groups or Roles

### II.Creating Group

* Creating a Group or Role

```shell
URL : http://127.0.0.1:8000/groups/
Request Method: POST
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
payload:
  {
    "name": "<Name of Group>",
    "permissions": []
}
```
Example cURL Code:

```shell
curl --location 'http://127.0.0.1:8000/groups/' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ' \
--header 'Content-Type: application/json' \
--data '{
    "name": "<Name of Group>",
    "permissions": []
}'
```
## 6. groups/<pk>

* This endpoint helps to Update, Delete and Retrieve the Group(Role)

### I. Getting Group by using id

* Getting Group using the Primary Key(id)

```shell
URL : http://127.0.0.1:8000/groups/<pk(id)>
Request Method: GET
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
```

Example cURL Code:

```shell
curl --location 'http://127.0.0.1:8000/groups/<pk(id)>' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ'```
```


### II. Updating Group 

* Updating Group using the Primary Key(id)

```shell
URL : http://127.0.0.1:8000/groups/<pk(id)>
Request Method: PUT
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
payload:
  {
    "name": "<Name of Group>",
    "permissions": [<Permission Ids>]
}
```

Example cURL code:

```shell
curl --location --request PUT 'http://127.0.0.1:8000/groups/<pk(id)>' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ' \
--header 'Content-Type: application/json' \
--data '{
    "name": "<Name of Group>",
    "permissions": [<Permission Ids>]
}'
```

### III. Deleting Group

* Deleting Group using Primary Key(id)

```shell
URL : http://127.0.0.1:8000/groups/<pk(id)>
Request Method: DELETE
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
```

Example cURL code:

```shell
curl --location --request DELETE 'http://127.0.0.1:8000/groups/<pk(id)>' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ' \
--header 'Content-Type: application/json'
```



## 7. user_list

* This Endpoint helps to get the list of users

```shell
URL : http://127.0.0.1:8000/user_list/
Request Method: GET
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
```
Example cURL Code:
```shell
curl --location 'http://127.0.0.1:8000/user_list/' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ'
```


## 8. user_create

* This Endpoint helps to create the user

```shell
URL : http://127.0.0.1:8000/user_create/
Request Method: POST
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
payload:
  {
    "password": "<password>",
    "username": "<username>",
    "first_name": "<First Name>",
    "last_name": "<Last Name>",
    "email": "<Email ID>",
    "groups": [<Assigning roles(group ids)>],
    "user_permissions": [<Assigning permissions(permission id)>]
  }
```

Example cURL Code:
```shell
curl --location 'http://127.0.0.1:8000/user_create/' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "password": "<password>",
    "username": "<username>",
    "first_name": "<First Name>",
    "last_name": "<Last Name>",
    "email": "<Email ID>",
    "groups": [<Assigning roles(group ids)>],
    "user_permissions": [<Assigning permissions(permission id)>]
}'
```

## 9. users/<username>

* This Endpoint helps to Update and Delete

### I. Update User

* Updating User

* Here need to pass the data what are the fields to update 

```shell
URL : http://127.0.0.1:8000/users/<username>
Request Method: PUT
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
payload:
  {
    "password": "<Password>",
    "first_name": "<First Name>",
    "last_name": "<Last Name>",
    "email": "<Email>",
    "groups": [<Assigning roles(group ids)>],
    "user_permissions": [<Assigning permissions(permission id)>]
  }
```

Example cURL Code:

```shell
curl --location --request PUT 'http://127.0.0.1:8000/users/<username>' \
--header 'Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "password": "<Password>",
    "first_name": "<First Name>",
    "last_name": "<Last Name>",
    "email": "<Email>",
    "groups": [<Assigning roles(group ids)>],
    "user_permissions": [<Assigning permissions(permission id)>]
}'
```

### 2. Delete User

* Deleting User

```shell
URL : http://127.0.0.1:8000/users/<username>
Request Method: DELETE
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
```

Example cURL Code:

```shell
curl --location --request DELETE 'http://127.0.0.1:8000/users/<username>' \
--header 'Authorization: Bearer 1FxEHf647kC0fxawTzgz3htBKftM4B' \
--header 'Content-Type: application/json'
```

## 10. check_permission

* This Endpoint helps to check the user has the permission or not by using access_token.

```shell
URL : http://127.0.0.1:8000/check_permission/
Request Method: POST
Headers:
  Authorization: Bearer UuOSEQSPz53uE04SMdzbS4VGPXDxjZ
payload:
   {
    "permission": "<Permission codename>"
  }
```

Example cURL Code:

```shell
curl --location 'http://localhost:8000/check_permission/' \
--header 'Authorization: Bearer ZH0SGfRGdfZQAQNs6RmqpW9GvJlZcB' \
--header 'Content-Type: application/json' \
--data '{
    "permission": "add_task"
}'
```

