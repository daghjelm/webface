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

def identity_size_split(size: int, root, dataset_name, new_name):
    new_dir, source_dir = create_folder(size, root, dataset_name, new_name)
    
    for i, folder in enumerate(sorted(os.listdir(source_dir))):
        folder_path = os.path.join(source_dir, folder)
        if i >= size:
            break
        shutil.copytree(folder_path, os.path.join(new_dir, folder))
    
def image_size_split(size: int, root, dataset_name, new_name):
    new_dir, source_dir = create_folder(size, root, dataset_name, new_name)
    n = 0
    for identity in sorted(os.listdir(source_dir)):
        identity_path = os.path.join(source_dir, identity)
        new_folder_path = os.path.join(new_dir, identity)
        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)
        for image in sorted(os.listdir(identity_path)):
            if n >= size: 
                return 'done'
            source_image_path = os.path.join(identity_path, image)
            dest_image_path = os.path.join(new_folder_path, image)
            shutil.copy(source_image_path, dest_image_path)
            n += 1

def merge_datasets(root: str, new_name: str, paths):
    dest_dir = os.path.join(root, new_name)

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    #data/path
    for path in paths:
        source_path = os.path.join(root, str(path)) 

        #data/path/identity
        for identity in os.listdir(source_path):
            identsourcepath = os.path.join(source_path, identity)
            identdestpath = os.path.join(dest_dir, identity)
            if not os.path.exists(identdestpath):
                os.mkdir(identdestpath)
            #data/path/identity/img
            for img in os.listdir(identsourcepath):
                imgsourcepath = os.path.join(identsourcepath, img)
                imgdestpath = os.path.join(identdestpath, img)
                shutil.copy(imgsourcepath, imgdestpath)

def main():
    while True:
        print('''
            Enter the "keyword" to run the "function"
            ----------------------------
            function            : keyword
            ----------------------------
            identity size split : ident
            image size split    : image
            merge datasets      : merge''')
        inp = input('enter keyword : ')
        if inp == 'ident':
            print('identity size split')
            size = input('Enter amount of identities: ')
            root = input('Enter path to data sets: ')
            dataset_name = input('Enter name of the folder you want to copy: ')
            new_name = input('Enter new dataset name: ')
            return identity_size_split(int(size), root, dataset_name, new_name)
        elif inp == 'image':
            print('Image size split')
            size = input('Enter amount of images: ')
            root = input('Enter path to data sets: ')
            dataset_name = input('Enter name of the folder you want to copy: ')
            new_name = input('Enter new dataset name: ')
            return image_size_split(int(size), root, dataset_name, new_name)
        elif inp == 'merge':
            print('Merge datasets')
            root = input('Enter path to data sets: ')
            new_name = input('Enter new dataset name: ')
            paths = input('Enter names of the folders you want to merge: ').split()
            return merge_datasets(root, new_name, paths)
        else:
            print('Wrong keyword')

if __name__ == '__main__':
    main()
