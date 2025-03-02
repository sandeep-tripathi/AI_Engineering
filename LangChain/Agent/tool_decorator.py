import pandas as pd

data = {
    'name': ['Artisan Bakers', 'Peak Performance Co.', 'Tech Innovators', 'Peak Performance Co.'],
    'contact': ['John Doe', 'Jane Smith', 'Emily Davis', 'Michael Johnson'],
    'email': ['john@artisan.com', 'jane@peakco.com', 'emily@techinn.com', 'michael@peakco.com']
}
customers = pd.DataFrame(data)

# Assume that the @tool decorator is defined and available for use
def tool(func):
    func.is_tool = True
    func.args = func.__annotations__
    return func

# Convert the retrieve_customer_info function into a tool
@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()
  
# Print the tool's arguments
print(retrieve_customer_info.args)

# Call the tool on Peak Performance Co.
print(retrieve_customer_info("Peak Performance Co."))
