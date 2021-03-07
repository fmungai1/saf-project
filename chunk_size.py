import math

def split_list_into_variable_parts(data: list, chunk_size: int) -> dict:
    chunk_dict = dict()

    try:
        for i in range(math.ceil(len(data)/chunk_size)):
            chunk_dict[f"Key{i + 1}"] = data[chunk_size*i:chunk_size*(i+1)]
    except ZeroDivisionError:
        print("Chunk size cannot be 0!")

    return chunk_dict

if __name__ == "__main__":
    some_data = ["path/to/file/1", "path/to/file/2", "path/to/file/3", "path/to/file/4", "path/to/file/5",
                 "path/to/file/6", "path/to/file/7", "path/to/file/8", "path/to/file/9", "path/to/file/10"]
    chunk_size = int(input("Enter chunk size: "))

    for key, value in split_list_into_variable_parts(some_data, chunk_size).items():
        print(f"{key}:")

        for item in value:
            print(item)

        print() 