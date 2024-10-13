def safe_divide(numerator, denominator):
    """Performs safe division and handles potential errors."""
    try:
     
        num = float(numerator)
        denom = float(denominator)
        
      
        result = num / denom
        return f"The result of the division is {result:.1f}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

if __name__ == "__main__":
    print(safe_divide(10, 2)) 
