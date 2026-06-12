import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Функція Методу Ньютона для розв'язання x^2 - 4 = 0
def newton_method_solve(x0, tol=1e-5, max_iter=100):
    f = lambda x: x**2 - 4
    df = lambda x: 2*x
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return None, "Похідна дорівнює нулю."
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    return x, max_iter

# Додано підтримку GET-запитів для сумісності з методичкою
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    x_val = None
    
    if request.method == 'GET':
        x_val = request.args.get('x')
    elif request.method == 'POST':
        data = request.get_json()
        if data:
            x_val = data.get('x')
            
    if x_val is None:
        return jsonify({"error": "Передайте параметр 'x' (наприклад: /calculate?x=5)"}), 400
    
    try:
        x0 = float(x_val)
    except (ValueError, TypeError):
        return jsonify({"error": "Параметр 'x' має бути числом"}), 400
    
    root, iterations = newton_method_solve(x0)
    
    if root is None:
        return jsonify({"error": iterations}), 400
        
    return jsonify({
        "input_x0": x0,
        "result_root": root,
        "iterations": iterations,
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
