def print_full_name(first_name, last_name):
    # Write your code here
    full_name = f"Hello {first_name + last_name}! You just delved into python"
    return full_name

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print(print_full_name(first_name, last_name))