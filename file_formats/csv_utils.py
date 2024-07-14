import os
import json
import csv
import pickle

def traverse_directory(directory_path):
    """
    Recursively traverses a directory and its subdirectories.
    Saves results to JSON, CSV, and Pickle files.

    Args:
        directory_path (str): Absolute path to the directory.

    Returns:
        None
    """
    result = []

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            result.append({
                'path': file_path,
                'type': 'file',
                'size_bytes': file_size
            })

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size = sum(os.path.getsize(os.path.join(dir_path, f)) for f in os.listdir(dir_path))
            result.append({
                'path': dir_path,
                'type': 'directory',
                'size_bytes': dir_size
            })

    # Save results to files
    with open('result.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)

    with open('result.csv', 'w', newline='') as csv_file:
        fieldnames = ['path', 'type', 'size_bytes']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result)

    with open('result.pkl', 'wb') as pickle_file:
        pickle.dump(result, pickle_file)
