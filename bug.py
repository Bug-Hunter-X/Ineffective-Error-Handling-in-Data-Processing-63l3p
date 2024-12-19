def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with potential error
averages = []
for i in range(5):
    data = []
    try:
        # Simulate getting data from external source which can fail
        # This might raise exceptions like IOError, TypeError, etc. 
        data = get_data_from_source(i) 
        average = calculate_average(data)
        averages.append(average)
    except Exception as e:
        print(f"Error processing data for iteration {i}: {e}")
        # Here, we are not handling the error effectively; we just print it and continue
        # We might want to log the error more robustly or re-try or skip the problematic data etc. 
        averages.append(None)  # Append None to maintain list length
        
print(averages)