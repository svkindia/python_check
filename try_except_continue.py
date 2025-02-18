def example_function(i):
    if i == 3:
        raise ValueError("An error occurred with i = 3")
    return i * 2

for i in range(5):
    try:
        result = example_function(i)
        print(f"Result for i={i}: {result}")
    except Exception as e:
        print(f"Error occurred for i={i}: {e}. Skipping...")
        #continue
