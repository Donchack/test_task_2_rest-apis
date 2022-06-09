from flask import Blueprint, jsonify, request, abort, make_response
from random import randint

guess_color = Blueprint('guess_color', __name__)

def guess_clr(item_number: int) -> str:
    """
    Returns the color of the item. 
    The color is guessed as the probability of pulling an object 
    of a certain color out of a set ordered by color, 
    where the first objects of that color, 
    which are more in the set, are located.
    """
    num_ord_color = randint(1, 100)
    percent_blue = 70
    percent_green = 16
    # percent_red = 14
    if num_ord_color <= percent_blue:
        color = 'blue'
    elif percent_blue < num_ord_color <= percent_blue + percent_green:
        color = 'green'
    else:
        color = 'red'
    return color

@guess_color.errorhandler(400)
def bad_request(error: str) -> dict:
    return make_response(jsonify({"error": str(error)}), 400)

@guess_color.route('/guessclr/api/v1.0/color', methods=['GET'])
def get_color() -> dict:
    """
    Returns JSON the color of the item.
    """
    if not request.json:
        abort(400, description='No data')
    try:
        item_number = int(request.json.get('number', ''))
    except ValueError:
        message = 'There are no necessary factors or the values are not a int number'
        abort(400, description=message)
    if item_number < 1 or item_number > 100:
        abort(400, description='The item number must be from 1 to 100')
    return jsonify({'color': guess_clr(item_number)}), 201