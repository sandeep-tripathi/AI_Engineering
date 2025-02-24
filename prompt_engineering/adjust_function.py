client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""
Given the following function:

{function}

Modify the function to:
1. Test if the inputs to the function are positive.
2. If any input is not positive, display an appropriate error message.
3. Otherwise, return both the area and perimeter of the rectangle.

The updated function should look like this:

def calculate_area_perimeter_rectangular_floor(width, length):
    # Check if the inputs are positive
    if width <= 0 or length <= 0:
        return "Error: Both width and length must be positive numbers."
    else:
        area = width * length
        perimeter = 2 * (width + length)
        return area, perimeter
"""

response = get_response(prompt)
print(response)
