from models import app, Widget
from flask import jsonify, request
from crud.user_crud import get_all_widgets, get_one_widget


@app.route('/')
def home():
    return jsonify(message='Welcome to home page')




# GET all widgets
# POST add a widget
@app.route('/widgets', method=['GET', 'POST'])
def widget_index()
    if request.method == 'GET'
        return get_all_widgets()
    if request.method == 'POST' 
        print(request.form)
        return add_widget()
    else:
        return jsonify(message='Widgets coming soon')



# GET one widget
# PUT update one widget
# DELETE delete one widget
@app.route('/widgets/<id>', method=['GET', 'PUT', 'DELETE'])
def one_widget(id)
    if response.method == 'GET'
        return get_one_widget(id)
    elif response.method == 'PUT'
        return update_widget(id)
    elif response.method == 'DELETE'
        return destory_widget(id)
    else:
        return jsonify(message='error, please choose a valid input id')










