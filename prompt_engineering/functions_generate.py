client = OpenAI(api_key="<OPENAI_API_TOKEN>")

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = f"""
Write a Python function that takes a list of integers and returns the sum of the integers. Use the following examples as a guide:

{examples}
"""

response = get_response(prompt)
print(response)




""" 
#Output: 
You can create a Python function to sum a list of integers using the built-in `sum()` function. Here's how you can implement it:
    
    ```python
    def sum_of_integers(int_list):
        return sum(int_list)
    
    # Test cases
    print(sum_of_integers([10, 5, 8]))  # Output: 23
    print(sum_of_integers([5, 2, 4]))    # Output: 11
    print(sum_of_integers([2, 1, 3]))    # Output: 6
    print(sum_of_integers([8, 4, 6]))    # Output: 18
    ```
    
    This function takes a list of integers as input and returns their sum. The test cases demonstrate its functionality.
 """
