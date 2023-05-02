import os
import shutil

folder_name = 'webface-10'
data_path = 'data/' + folder_name

#get number of folders in data_path
num_folders = len(os.listdir(data_path))

train_size = 0.8 
test_size = 0.2 

train_path = 'data/train/' + folder_name
test_path = 'data/test/' + folder_name

#loop over all folders in data_path and add the first 80% to train_path and the rest to test_path
for i, folder in enumerate(os.listdir(data_path)):
    folder_path = os.path.join(data_path, folder)
    n = len(os.listdir(folder_path))
    for i, image in enumerate(os.listdir(folder_path)):
        image_path = os.path.join(folder_path, image)
        if i < n * train_size:
            train_image_path = os.path.join(train_path, folder, image)
            shutil.copy(image_path, train_image_path)
        else: 
            test_image_path = os.path.join(test_path, folder, image)
            shutil.copy(image_path, test_image_path)

    # if i < train_size:
    #     os.rename(os.path.join(data_path, folder), os.path.join(train_path, folder))
    # else:
    #     os.rename(os.path.join(data_path, folder), os.path.join(test_path, folder))