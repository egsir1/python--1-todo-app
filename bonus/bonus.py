def get_average():
    with open("files\data.txt", "r") as file:
        data = file.readlines()
        values = data[1:]
        values = [float(i) for i in values]
        print(values)
        average = sum(values) / len(values)
    return average


result = get_average()
print(result)
