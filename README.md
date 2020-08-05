# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) DIY API — Python Edition!

## **Deliverable**:

It's time to make your own API again! 

Using what you have learned about Flask, RESTful routing, CRUD operations, and SQLAlchemy, use the SQLAlchemy ORM to implement full CRUD functionality on a model (subject of your choosing).

-----

## **Requirements**: 

1. The model you choose to use should have at least three fields, as well an id field. 

*Example for Widget Model:*

| column name | type |
|:-----------:|:----:|
|id | integer |
|name | text |
|wodgets | integer |
|quantity | integer |


2. Your API should be accessible via five routes: 

*Example:*

| Method | Action | URL | Functionality |
|--------|:------:|:---:|:--------------|
| GET | index | /widgets | list all widgets |
| POST | create | /widgets | add a widget |
| GET | detail/show | /widgets/:id | show one widget |
| PUT | update | /widgets/:id | update one widget |
| DELETE | delete | /widgets/:id | delete one widget |

-------

## **Steps to Achieve**

**You will need to:**
1. Fork and clone this repository!
2. Create your virtual environment `python -m venv venv`
4. Create a `.gitignore` and add your virtual environment folder. _(check out [github's suggestions](https://github.com/github/gitignore/blob/master/Python.gitignore) for `.gitignore`)_
5. Activate your virtual environment
6. Install dependencies `pip install Flask Flask-SQLAlchemy psycopg2`
7. Copy our installs into a requirements.txt file. `pip freeze >> requirements.txt`
8. Create a `models.py` file for your models and an `api.py` for your flask server.

**Recommended Workflow:**
1. Stub out your routes
2. Write you `models.py` file 
3. Link your model to your server
4. Update your routes and make the magic happen!

-------

## Bonus:
Add a second model to your API. This model should relate to your first model via a 1:M relationship. 

Once added, update your GET and POST routes for this second model which allow you do the following with your API: 
1. Show all elements from second model that relate to your element from first model at :id. 
2. Add a new element to your original model that include related elements from this second model at :id.

### Double Bonus

Make another model and create a N:M relationship!
