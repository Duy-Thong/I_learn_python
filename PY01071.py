def is_python_file(filename):
    if filename[-3:].lower() == '.py':
        return "yes"
    else:
        return "no"

filename = input()
print(is_python_file(filename))
