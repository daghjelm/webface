import os
import shutil

def main(size, root, dataset_name, new_name):
    if not new_name:
        new_name = dataset_name + str(size)
    
    source_dir = os.path.join(root, dataset_name)
    new_dir = os.path.join(root, new_name)
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    for i, folder in enumerate(sorted(os.listdir(source_dir))):
        folder_path = os.path.join(source_dir, folder)
        if i >= size:
            break
        shutil.copytree(folder_path, os.path.join(new_dir, folder))

if __name__ == '__main__':
    main(5, 'data/', 'casia-webface', 'webface-5')