import os


def extract_file_info(file_path):
    path, full_filename = os.path.split(file_path)
    filename, extension = os.path.splitext(full_filename)
    return path, filename, extension


file_path = '/path/to/your/file.txt'
path, filename, extension = extract_file_info(file_path)
print(f"Path: {path}")
print(f"Filename: {filename}")
print(f"Extension: {extension}")
