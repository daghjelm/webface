import os
import shutil

def create_folder(size, root, dataset_name, new_name):
    if not new_name:
        new_name = dataset_name + str(size)
    
    new_dir = os.path.join(root, new_name)
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    source_dir = os.path.join(root, dataset_name)
        
    return new_dir, source_dir

def identity_size_split(size, root, dataset_name, new_name):
    new_dir, source_dir = create_folder(size, root, dataset_name, new_name)
    
    for i, folder in enumerate(sorted(os.listdir(source_dir))):
        folder_path = os.path.join(source_dir, folder)
        if i >= size:
            break
        shutil.copytree(folder_path, os.path.join(new_dir, folder))
    
def image_size_split(size, root, dataset_name, new_name):
    new_dir, source_dir = create_folder(size, root, dataset_name, new_name)
    n = 0
    for i, identity in enumerate(sorted(os.listdir(source_dir))):
        identity_path = os.path.join(source_dir, identity)
        new_folder_path = os.path.join(new_dir, identity)
        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)
        for j, image in enumerate(sorted(os.listdir(identity_path))):
            if n >= size: 
                return 'done'
            source_image_path = os.path.join(identity_path, image)
            dest_image_path = os.path.join(new_folder_path, image)
            shutil.copy(source_image_path, dest_image_path)
            n += 1

if __name__ == '__main__':
    # identity_size_split(5, 'data/', 'casia-webface', 'webface-5')
    # image_size_split(20, 'data/', 'casia-webface', 'webface-20st')
    # image_size_split(100, 'data/', 'digiface_subjects_0-1999_72_imgs', 'digiface-100st')
    identity_size_split(100, 'data/', 'digiface_subjects_0-1999_72_imgs', 'digiface-100')