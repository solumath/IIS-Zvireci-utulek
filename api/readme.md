# API

## How to
Install all requirements
```
$ pip install -r requirements.txt
```
Start main
```
$ python3 main.py
```

## Endpoints

* **User sessions**
    * Login     [POST]  
      * json body: 
       ```{ "login":<username>, "password":<password>}```
    * Logout    [GET]   
       * cookies:
       ```{ "token":<token> }``` - token cookie is sent in Login response
    <!-- * Register  [POST]  - not implemented yet -->