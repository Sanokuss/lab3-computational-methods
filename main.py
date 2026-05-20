# Модель: Метод Ньютона (5 семестр)
# Автор: Боденчук Олександр Сергійович, група АІ-235

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

@app.route('/calculate', methods=['POST'])
def calculate():
    # Отримуємо дані у форматі JSON
    data = request.get_json()
    
    if not data or 'x' not in data:
        return jsonify({"error": "Передайте параметр 'x' у JSON тілі запиту"}), 400
    
    try:
        x0 = float(data['x'])
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)