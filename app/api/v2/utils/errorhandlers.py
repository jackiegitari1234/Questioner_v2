from flask import Flask, jsonify



# edge cases
def invalid_method(error):
    return jsonify({
        'error': str(error),
        'status': 405
        }), 405

# bad request
def bad_request(error):
    return jsonify({
        'error': str(error),
        'status': 400
        }), 400

# unexisting url
def page_not_found(error):
    return jsonify({
        'error': str(error),
        'status': 404
        }), 404

# internal server error
def server_error(error):
    return jsonify({
        'error': str(error),
        'status': 500
        }), 500
