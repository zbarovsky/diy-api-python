from models import app, Widget
from flask import jsonify, request
from crud.widget_crud import get_all_widgets, get_one_widget, add_widget, update_widget, destory_widget


@app.route('/')
def home():
    return jsonify(message='Welcome to home page')


# GET all widgets
# POST add a widget
@app.route('/widgets', methods=['GET', 'POST'])
def widget_index():
    if request.method == 'GET':
        return get_all_widgets()
    elif request.method == 'POST': 
        # print(request.form)
        return add_widget(name=request.form['name'], wodget=request.form['wodget'], quantity=request.form['quantity'])
    else:
        return jsonify(message='Widgets coming soon')



# GET one widget
# PUT update one widget
# DELETE delete one widget
@app.route('/widgets/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def one_widget(id):
    if request.method == 'GET':
        return get_one_widget(id)
    elif request.method == 'PUT':
        return update_widget(id, name=request.form['name'], wodget=request.form['wodget'], quantity=request.form['quantity'])
    elif request.method == 'DELETE':
        return destory_widget(id)
    else:
        return jsonify(message='error, please choose a valid input id')










