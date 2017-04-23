# flask-rest-jsonapi-skeleton-app
A bare minimum skeleton app for
[miLibris/flask-rest-jsonapi](https://github.com/miLibris/flask-rest-jsonapi)
 . This is a really basic api example which is based on the original
 [First example](http://flask-rest-jsonapi.readthedocs.io/en/latest/quickstart.html#first-example)
 by miLibris. The simple skeleton app can be used as starting point for
 more ambitious projects which requires well modularized organization of code.

### Installation
Clone the repository:
```
git clone https://github.com/zengoma/flask-rest-jsonapi-skeleton-app.git <project-directory>
```
Install dependencies:
```
pip install requirements.txt
```
Create a database, <project-dir>/dev.db , by default.

### Configuration

* **config.py:** Setup your database and other global app settings here.

### Running the app

Simply run the bootstrap, run.py, file from the root directory
```
python run.py
```

### Project Structure

#### Database/Models
* **database/models.py:** sqlalchemy model class declarations.
* **database/ \_\_init\_\_.py:** sqlalchemy database initialization
* **database/database_setup.py:** Add sample data, administrator users or
perform routine database functions at startup.

#### Api
The packaged flask-rest-jsonapi. Please read the
[documentation](http://flask-rest-jsonapi.readthedocs.io/en/latest/index.html)
for more information.

* **api/resources.py:** [Resources](http://flask-rest-jsonapi.readthedocs.io/en/latest/resource_manager.html)
go here.
* **api/schemas.py:** [Schemas](http://flask-rest-jsonapi.readthedocs.io/en/latest/logical_data_abstraction.html)
go here.
* **api/views.py** [Routes/Api Views/Endpoints](http://flask-rest-jsonapi.readthedocs.io/en/latest/routing.html)
go here.

By default the api is served on the path http://localhost:5000/api. This is achieved by using flask
[blueprints](http://flask.pocoo.org/docs/0.12/blueprints/). You can modify
the path or remove it by modifying the api initialization in run.py.

#### Auth
* **auth/permissions.py:** [Permission manager setup](http://flask-rest-jsonapi.readthedocs.io/en/latest/permission.html)

### Extending the project structure

Feel free to add other aspects to the application by including additional
packages and blueprints. For example add a frontend package and blueprint
on the root "/" url path to create a frontend for you project with static files etc.

##### Special thanks:
To the [miLibris/flask-rest-jsonapi](https://github.com/miLibris/flask-rest-jsonapi) team.
This project has finally convinced me to abandon my php micro-framework api's
and finally embrace python. I have seen the light!




