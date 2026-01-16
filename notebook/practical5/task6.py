import sys

# Check if no arguments were provided
if len(sys.argv) == 1:
    print("No arguments were provided")
else:
    # Get the count of arguments (including program name)
    count = len(sys.argv)
    total = 0
    
    # Loop through all arguments except the first (program name)
    while count > 1:
        count -= 1
        # Add each argument to the total (converting to float)
        total += float(sys.argv[count])
    
    # Print the total
    print("Total is", total)
    
    # Calculate and print the average
    average = total / (len(sys.argv) - 1)
    print("Average is", average)