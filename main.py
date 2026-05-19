# Модель: Метод Ньютона (5 семестр)
# Автор: Боденчук Олександр, група АІ-235

def newton_method(f, df, x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            print("Похідна дорівнює нулю. Зупинка.")
            return None
            
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tol:
            print(f"Знайдено корінь: {x_new} за {i+1} ітерацій")
            return x_new
            
        x = x_new
        
    print("Перевищено ліміт ітерацій")
    return x

# Приклад використання для рівняння x^2 - 4 = 0
if __name__ == "__main__":
    f = lambda x: x**2 - 4
    df = lambda x: 2*x
    newton_method(f, df, x0=3.0)