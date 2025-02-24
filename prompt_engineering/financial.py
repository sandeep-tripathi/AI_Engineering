prompt = f"""
Given the following Python function:

{function_string}

Let's analyze this function step by step to understand what it does.

Step 1: Identify the purpose of the function. What is the function name and what does it aim to achieve?
Step 2: Examine the first part of the function where a list called 'returns' is initialized. Why is this list being created?
Step 3: Look at the loop iterating over the 'portfolio'. What is the loop doing for each investment in the portfolio?
Step 4: What are the variables 'initial_value' and 'final_value' used for, and how is 'return_percentage' calculated?
Step 5: Why are we appending 'return_percentage' to the 'returns' list?
Step 6: What does the line of code `total_return = sum(returns) / len(returns)` do?
Step 7: Finally, what does the function return and what does this value represent?

Now, let's explain the function step by step:
"""
