import os
import shutil
import check_dir_file_existence as cdfe

#Taking target directory path as input
print('Please input the exact folder path for organizing')
tar_dir = input()

def organize(dir):
    folder = []
    file_n = []
    #Intializing list of required directories for orgaization
    req = ['Documents', 'Images','Audio', 'Videos', 'Programming', 'Others']
    #Initializing quick access dictionaries with file formats as keys and their respective subdirectories as values
    doc_type = {'doc':'\\Docs','docx':'\\Docs', 'html':'\\PDFs', 'htm':'\\PDFs', 'odt':'\\PDFs', 'pdf':'\\PDFs', 'xls':'\\Excel', 'xlsx':'\\Excel','ods':'\\Excel', 'csv':'\\Excel','xml':'\\Excel','ppt':'\\PPts','pptx':'\\PPts','txt':'\\Txt'} 
    img_type = {'tif':'\\Others' , 'tiff':'\\Others', 'bmp':'\\Others', 'jpg':'\\JPEGs', 'jpeg':'\\JPEGs', 'gif':'\\GIFs', 'png':'\\PNGs', 'eps':'\\Others'}
    vid_type = {'mp4':'\\MP4s', 'wmv':'\\WMVs', 'mkv':'MKVs', 'mov':'\\Others','avi':'\\Others','flv':'\\Others','webm':'\\Others'}
    aud_type = {'mp3': '\\MP3s', 'aac': '\\AACs', 'wma':'\\WMAs', 'aiff' :'\\Others','alac':'\\Others','flac':'\\Others','ocg':'\\Others'}
    prg_type = {'py':'\\Python', 'ipynb':'\\Jupyter', 'sql':'\\SQL'}

    with os.scandir(tar_dir) as files:
        for f in files:
            if not f.is_file():
                folder.append(f.name) #Storing folder names in list
            elif f.is_file():
                file_n.append(f.name)#storing file names in list
        for ele in req :    #loop to check if all directories in req are present
            if ele not in folder:
                path = tar_dir + f'\\{ele}'
                os.mkdir(path) #creating the directories which are absent

        #looping over file names to define source and destination file paths
        for f in file_n:
                src = tar_dir+f'\\{f}'   #definition of source filepath
                type = f.split('.')[-1] #storing file format
                type = type.lower()
                if type in doc_type.keys():
                    dst = tar_dir+'\\Documents'+doc_type[type]
                    cdfe.check_dir(dst)
                elif type in img_type.keys():
                    dst = tar_dir+'\\Images'+img_type[type]
                    cdfe.check_dir(dst)
                elif type in vid_type.keys():
                    dst = tar_dir+'\\Videos'+vid_type[type]
                    cdfe.check_dir(dst)
                elif type in aud_type.keys():
                    dst = tar_dir+'\\Audio'+aud_type[type]
                    cdfe.check_dir(dst)
                elif type in prg_type.keys():
                    dst = tar_dir+'\\Programming'+prg_type[type]
                    cdfe.check_dir(dst)
                else:
                    dst = tar_dir+'\\Others'
                    cdfe.check_dir(dst)
            
                dst = dst + f'\\{f}'   #appending file name to destination path
                dst = cdfe.rename_file(dst)  #checking existence of file in destination then renaming if present
                shutil.move(src,dst)    #moving file to the destination path
    print('Done :)')

organize(tar_dir)