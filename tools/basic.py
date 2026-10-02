from datetime import datetime


def get_time() -> str:
    """Returns the current local date and time."""
    return datetime.now().strftime("%A, %d %B %Y, %I:%M %p")


def calculate(expression: str) -> str:
    """Evaluates a basic math expression such as '12*7+3' and returns the result."""
    allowed = set("0123456789+-*/(). %")
    if not set(expression) <= allowed:
        return "Error: only numbers and + - * / ( ) . % are allowed"
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"Error: {e}"