## API Endpoints
- login/
    - **POST** =>  Login user
- users/
    - **POST** => create users
    - **GET** => Get Users
- users/:id
    - **GET** => Get User
    - **PUT** => update user
- create_expense/
    - **POST** => Create Expenses


## Start The Server
```bash
cd splitwise-main
env/Script/activate
python -m pip install -r requirments.txt
cd splitwise
python manage.py runserver
```
