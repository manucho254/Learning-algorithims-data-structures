def load_numbers(file: str) -> list:
    if ".txt" not in file:
        return ["Invalid file or filename"]
    with open(file, "r+") as f:
        items = list(map(lambda x: int(x.split("\n")[0]), f.readlines()))
        return items
    
print(load_numbers("test.txt"))
    
