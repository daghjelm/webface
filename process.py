import os

data_path = 'data/casia-webface'

#get number of folders in data_path
num_folders = len(os.listdir(data_path))

train_size = 0.8 * num_folders
test_size = 0.2 * num_folders

train_path = 'data/train'
test_path = 'data/test'

#loop over all folders in data_path and add the first 80% to train_path and the rest to test_path
for i, folder in enumerate(os.listdir(data_path)):
    if i < train_size:
        os.rename(os.path.join(data_path, folder), os.path.join(train_path, folder))
    else:
        os.rename(os.path.join(data_path, folder), os.path.join(test_path, folder))