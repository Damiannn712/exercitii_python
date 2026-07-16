def evaluate_polynomial(poly, value):
    # Inlocuieste simbolurile folosite in reprezentare cu forma valida in Python
    expression = poly.replace('^', '**')

    # Evalueaza polinomul pentru valoarea data
    return eval(expression, {"__builtins__": {}}, {"x": value})


# Exemplu de utilizare
print(evaluate_polynomial("3x^3 + 5x^2 - 2x - 5", 2))
