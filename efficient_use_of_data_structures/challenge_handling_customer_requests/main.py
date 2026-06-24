from collections import deque

# Initialize an empty customer support queue
customer_queue = deque()

# Add requests to the end
customer_queue.append('Request 1')
customer_queue.append('Request 2')

# Add a high-priority request tp the front
customer_queue.appendleft('High-Priority Request')

# Process requests in the correct order
while customer_queue:
    # Remove from the front
    current_request = customer_queue.popleft()
    print(f"Processing: {current_request}")