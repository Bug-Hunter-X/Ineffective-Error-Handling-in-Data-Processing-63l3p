import logging

# Configure logging to write errors to a file
logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def get_data_from_source(i):
    # Simulate potential errors in data acquisition
    if i == 2:
        raise IOError("Simulated IOError")
    elif i == 3:
        raise TypeError("Simulated TypeError")
    return [i * j for j in range(1, 4)]

averages = []
for i in range(5):
    data = []
    try:
        data = get_data_from_source(i)
        average = calculate_average(data)
        averages.append(average)
    except IOError as e:
        logging.error(f"IOError during data processing for iteration {i}: {e}")
        # Handle IOError specifically (e.g., retry, skip, use default value)
        averages.append(0)  # Example: Use 0 as default
    except TypeError as e:
        logging.error(f"TypeError during data processing for iteration {i}: {e}")
        # Handle TypeError specifically (e.g., data transformation)
        averages.append(None) #Example: Use None
    except Exception as e:
        logging.exception(f"An unexpected error occurred during data processing for iteration {i}: {e}")
        averages.append(None)  # Log other exceptions

print(averages)
print("Check error.log for detailed error messages.") 