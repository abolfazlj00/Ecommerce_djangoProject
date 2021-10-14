# Ecommerce_djangoProject

## How run the project?


##### Clone the repository :
```bash
$ git clone https://github.com/abolfazlj00/Ecommerce_djangoProject.git
```
##### Create a virtualenv and activate it:
 ```bash
$ python3 -m venv venv
$ . venv/bin/activate
```
##### Or on Windows cmd : 
 ```bash
> py -3 -m venv venv
> venv\Scripts\activate.bat
```
##### Install the requirements :
```bash
$ pip3 install -r requirements.txt
```
##### Go to teh configuration folder and creating a .env file from file .evn_sample.txt : 
```bash
$ cd core
```

### Open and read config_sample.txt 
### back to the Ecommerce_djangoProject folder

#####  Run makemigrations and migrate :
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

#####  Run the development server :
```bash
python3 manage.py runserver
```
Open http://127.0.0.1:8000 in your browser. 
