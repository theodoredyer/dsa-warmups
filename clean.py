import os
import shutil

def create_subdirectories(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.py')]
    if files:
        print(f"Found files in directory: {directory}")
        for i in range(1, max(int(f.split('_')[0]) for f in files) // 200 + 2):
            subdirectory = f"{i*200-199}_{i*200}"
            subdirectory_path = os.path.join(directory, subdirectory)
            if not os.path.exists(subdirectory_path):
                print(f"Creating subdirectory: {subdirectory_path}")
                os.makedirs(subdirectory_path)
            for file in files:
                start, _ = file.split('_')
                if int(start) >= (i*200-199) and int(start) <= (i*200):
                    print(f"Moving file {file} to subdirectory: {subdirectory_path}")
                    shutil.move(os.path.join(directory, file), os.path.join(subdirectory_path, file))

def organize_directories():
    base_directory = "dsa-warmups"
    for root, dirs, files in os.walk(base_directory):
        for directory in dirs:
            if directory in ['easy', 'medium', 'hard']:
                directory_path = os.path.join(root, directory)
                create_subdirectories(directory_path)
                
if __name__ == "__main__":
    organize_directories()
