import numpy as np

# Monthly sales data (numerical data requiring calculations)
monthly_sales = np.array([320, 450, 500, 480, 350, 610, 720, 640, 510, 470, 420, 580])

# Unique user IDs who logged in during a day
user_ids = {1023, 2045, 1098, 2045, 3098, 1023}

# A product record
product = (2134, 'Wireless Mouse')

# An ordered collection of tasks (requires frequent updates)
tasks = ['Send report', 'Review code', 'Update website', 'Fix bug']

print(f"monthly_sales type: {type(monthly_sales)}")
print(f"user_ids type: {type(user_ids)}")
print(f"product type: {type(product)}")
print(f"tasks type: {type(tasks)}")