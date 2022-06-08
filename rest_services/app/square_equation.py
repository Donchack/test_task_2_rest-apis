from flask import Blueprint, jsonify, request, abort, make_response

square_equation = Blueprint('square_equation', __name__)

def get_roots(a: float, b: float, c: float) -> tuple:
    """
    Returns the roots of the quadratic equation.
    """
    discriminant = (b*b -4 * a * c) ** 0.5
    if discriminant < 0:
        solution = ()
    elif discriminant == 0:
        solution = (-b / (2 * a),)
    else:
        solution = ((-b + discriminant) / (2 * a),
                    (-b - discriminant) / (2 * a)
        )
    return solution

@square_equation.errorhandler(400)
def bad_request(error: str) -> dict:
    return make_response(jsonify({"error": str(error)}), 400)

@square_equation.route('/square/api/v1.0/sq-equation', methods=['GET'])
def get_solution() -> dict:
    """
    Returns JSON the roots of the quadratic equation.
    """
    if not request.json:
        abort(400, description='No data')
    try:
        a = float(request.json.get('a', ''))
        b = float(request.json.get('b', ''))
        c = float(request.json.get('c', ''))
    except ValueError:
        message = 'There are no necessary factors or the values are not a int number'
        abort(400, description=message)
    if a == 0:
        abort(400, description='index a cannot be zero')
    return jsonify({'solution': get_roots(a, b, c)}), 201