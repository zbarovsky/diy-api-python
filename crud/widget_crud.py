from flask import jsonify
from models import Widget, db

# GET all widgets
def get_all_widgets():
    all_widgets = Widget.query.all()
    results = [widget.as_dict() for widget in all_widgets]
    # for widget in all_widgets:
    #     results.append(widget.as_dict)
    return jsonify(results)

# GET one widget
def get_one_widget(id):
    one_widget = Widget.query.get(id)
    if one_widget:
        return jsonify(one_widget.as_dict())
    else:
        return jsonify(message='not a valid widget, please try again')

# POST 
def add_widget(name, wodget, quantity):
    new_widget = Widget(name=name, wodget=wodget, quantity=quantity)
    db.session.add(new_widget)
    db.session.commit()
    return jsonify(new_widget.as_dict())

# PUT
def update_widget(id, name, wodget, quantity):
    widget = Widget.query.get(id)
    if widget:
        widget.name = name or widget.name
        widget.wodget = wodget or widget.wodget
        widget.quantity = quantity or widget.quantity
        return jsonify(widget.as_dict())
    else:
        return jsonify(message='error, please update where there is an id')
    session.commit()

# DESTROY
def destory_widget(id):
    widget = Widget.query.get(id)
    if widget:
        db.session.delete(widget)
        db.session.commit()
        return f'deleted'
    else:
        return jsonify(message='Please indicate a valid widget to delete')