1. Create virtual environment with Python 3.8 to 3.9
```.env
python -m venv env
```
2. Activate virtual environment
```shell script
. env/bin/activate
```
3. Install dependencies
```shell script
pip install -r requirements.txt
```
4. Create .env files with the following variables
```.env
DB_NAME=example_db_name
DB_USER=example_db_user
DB_PASSWORD=example_password
DB_PORT=example_db_port
DB_HOST=example_db_host
SECRET_KEY=example_secret
TIME_ZONE=Asia/Ho_Chi_Minh
```

 