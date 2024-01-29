from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


from flask import Flask, request, jsonify
from Equation_slover_module import solve_equation_with_one_variable, solve_equations_with_two_variables

app = Flask(__name__)
 
@app.route("/")
def index():
    return "<h1>Hello!</h1>"

@app.route('/solve_equation_with_one_variable', methods=['POST'])
def solve_equation_with_one_variable_api():
    try:
        data = request.get_json()
        equation = data.get('equation', '')
        solution = solve_equation_with_one_variable(equation)
        if solution is not None:
        
            return jsonify({'solution': [float(val) for val in solution]})
        else:
            return jsonify({'error': 'Unable to solve the equation'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/solve_equations_with_two_variables', methods=['POST'])
def solve_equations_with_two_variables_api():
    try:
        data = request.get_json()
        equation1 = data.get('equation1', '')
        equation2 = data.get('equation2', '')
        solution = solve_equations_with_two_variables(equation1, equation2)
        print(solution)
        if solution is not None:
          return jsonify({'solution':solution})
        else:
            return jsonify({'error': 'Unable to solve the equations'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 400


def create_app():
    from waitress import serve
    port = 8080
    host = "0.0.0.0"
    print(f'server is Running... port:{port}')
    serve(app, host=host, port=port)


# if __name__ == '__main__':
#     app.run()

# if __name__ == '__main__':
#     from waitress import serve
#     port = 8080
#     host = "0.0.0.0"
#     print(f'server is Running... port:{port}')
#     serve(app, host=host, port=port)