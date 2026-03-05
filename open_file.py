try:
    with open("file.log") as file:
        read_data = file.read()
        print(read_data)
except FileNotFoundError as fnf_error:
    print(fnf_error)
