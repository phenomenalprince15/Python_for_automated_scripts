import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

def divide(a, b):
    try:
        result = a/b
        logging.info(f"Division Successfull: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted")
        return None


divide(10, 2)
divide(10, 0)

