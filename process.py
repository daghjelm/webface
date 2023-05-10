import os
import shutil

"""
    This is a script for splitting dataset into train and test folders.

    Just change folder name to use another dataset. Make sure the dataset is in the data folder.

    Structure of the test and train folders:
    data
    ├── data-set-name
    │   ├── train
    │   │   ├── identity-1
    │   │   │   ├── image-1
    │   │   │   ├── image-2
    │   │   │   ├── ...
    │   │   ├── identity-2
    │   │   │   ├── image-1
    │   │   │   ├── image-2
    │   │   │   ├── ...
    │   │   ├── ...
    │   ├── test
    │   │   ├── identity-1
    │   │   │   ├── image-1
    │   │   │   ├── image-2
    │   │   │   ├── ...
    │   │   ├── identity-2
    │   │   │   ├── image-1
    │   │   │   ├── image-2
    │   │   │   ├── ...
    │   │   ├── ...
    ├── ...
"""

def split(folder_name):
    data_path = 'data/' + folder_name

    train_size = 0.8 
    test_size = 0.2 

    train_path = 'data/train/' 
    test_path = 'data/test/' 

    if not os.path.exists(train_path):
        os.mkdir(train_path)
    if not os.path.exists(test_path):
        os.mkdir(test_path)

    train_path = 'data/train/' + folder_name
    test_path = 'data/test/' + folder_name

    #create train and test folders if they don't exist
    if not os.path.exists(train_path):
        os.mkdir(train_path)
    if not os.path.exists(test_path):
        os.mkdir(test_path)

    #loop over all folders in data_path and add the first 80% to train_path and the rest to test_path
    for i, folder in enumerate(os.listdir(data_path)):
        folder_path = os.path.join(data_path, folder)
        n = len(os.listdir(folder_path))
        for i, image in enumerate(os.listdir(folder_path)):
            image_path = os.path.join(folder_path, image)

            new_folder_path = train_path if i < n * train_size else test_path 
            new_folder_path = os.path.join(new_folder_path, folder) 

            #create folder for specific identity if it doesn't exist
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
            
            #copy image to new folder
            shutil.copy(image_path, os.path.join(new_folder_path, image))

if __name__ == '__main__':
    # split('casia-144000')
    # split('digiface_subjects_0-1999_72_imgs')
    folder = input('Enter folder name: ')
    split(folder)