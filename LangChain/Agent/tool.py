import pandas as pd

# Sample DataFrame setup
data = {
    'name': ['Artisan Bakers', 'Peak Performance Co.', 'Tech Innovators', 'Peak Performance Co.'],
    'contact': ['John Doe', 'Jane Smith', 'Emily Davis', 'Michael Johnson'],
    'email': ['john@artisan.com', 'jane@peakco.com', 'emily@techinn.com', 'michael@peakco.com']
}
customers = pd.DataFrame(data)

# Define a function to retrieve customer info by name
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    # Filter customers for the customer's name
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()

# Call the function on Peak Performance Co.
print(retrieve_customer_info("Peak Performance Co."))
