import os
import shutil
#Taking target directory path as input
print('Please input the exact folder path for organizing')
tar_dir = input()
folder = []
file_n = []
#Intializing list of required directories for orgaization
req = ['Documents', 'Images','Audio', 'Videos', 'Programming', 'Others']
#Initializing quick access dictionaries with file formats as keys and their respective subdirectories as values
doc_type = {'doc':'/Docs','docx':'/Docs', 'html':'/PDFs', 'htm':'/PDFs', 'odt':'/PDFs', 'pdf':'/PDFs', 'xls':'/Excel', 'xlsx':'/Excel','ods':'/Excel', 'csv':'/Excel','xml':'/Excel','ppt':'/PPts','pptx':'/PPts','txt':'/Txt'} 
img_type = {'tif':'/Others' , 'tiff':'/Others', 'bmp':'/Others', 'jpg':'/JPEGs', 'jpeg':'/JPEGs', 'gif':'/GIFs', 'png':'/PNGs', 'eps':'/Others'}
vid_type = {'mp4':'/MP4s', 'wmv':'/WMVs', 'mkv':'MKVs', 'mov':'/Others','avi':'/Others','flv':'/Others','webm':'/Others'}
aud_type = {'mp3': '/MP3s', 'aac': '/AACs', 'wma':'/WMAs', 'aiff' :'/Others','alac':'/Others','flac':'/Others','ocg':'/Others'}
prg_type = {'py':'/Python', 'ipynb':'/Jupyter', 'sql':'/SQL'}

def docs():
    os.makedirs(tar_dir+'/Documents/Docs', exist_ok= True)
    os.makedirs(tar_dir+'/Documents/PDFs', exist_ok= True)
    os.makedirs(tar_dir+'/Documents/Excel', exist_ok= True)
    os.makedirs(tar_dir+'/Documents/PPts', exist_ok= True)
    os.makedirs(tar_dir+'/Documents/Txt', exist_ok= True)

def images():
    os.makedirs(tar_dir+'/Images/JPEGs', exist_ok= True)
    os.makedirs(tar_dir+'/Images/GIFs', exist_ok= True)
    os.makedirs(tar_dir+'/Images/PNGs', exist_ok= True)
    os.makedirs(tar_dir+'/Images/Others', exist_ok= True)

def videos():
    os.makedirs(tar_dir+'/Videos/MP4s', exist_ok= True)
    os.makedirs(tar_dir+'/Videos/WMVs', exist_ok= True)
    os.makedirs(tar_dir+'/Videos/MKVs', exist_ok= True)
    os.makedirs(tar_dir+'/Videos/Others', exist_ok= True)

def audio():
    os.makedirs(tar_dir+'/Audio/MP3s', exist_ok= True)
    os.makedirs(tar_dir+'/Audio/AACs', exist_ok= True)
    os.makedirs(tar_dir+'/Audio/WMAs', exist_ok= True)
    os.makedirs(tar_dir+'/Audio/Others', exist_ok= True)

def program():
    os.makedirs(tar_dir+'/Programming/Python', exist_ok= True)
    os.makedirs(tar_dir+'/Programming/Jupyter', exist_ok= True)
    os.makedirs(tar_dir+'/Programming/SQL', exist_ok= True)

def rename_file(s):
    if os.path.exists(s):
        str, dst = "","/"
        loc = s.split('/')[:-1]
        fname = s.split('/')[-1]
        lst = fname.split('.')
        str = str.join(lst[:-1])+'_new.'+lst[-1]
        dst = dst.join(loc)+f'/{str}'
        return dst
    else:
        return s

with os.scandir(tar_dir) as files:
    for f in files:
        if not f.is_file():
            folder.append(f.name) #Storing folder names in list
        elif f.is_file():
            file_n.append(f.name)#storing file names in list
    for ele in req :    #loop to check if all directories in req are present
        if ele not in folder:
            path = tar_dir + f'/{ele}'
            os.mkdir(path) #creating the directories which are absent
    docs()  #creates document format subdirectories
    images()    #creates image format subdirectories
    program()   #creates programming file format subdirectories
    videos()    #creates video format subdirectories
    audio() #creates audio format subdirectories
    
    #looping over file names to define source and destination file paths
    for f in file_n:
            src = tar_dir+f'/{f}'   #definition of source filepath
            type = f.split('.')[-1] #storing file format
            type = type.lower()
            if type in doc_type.keys():
                dst = tar_dir+'/Documents'+doc_type[type]+f'/{f}'   #appending file name to destination path
            elif type in img_type.keys():
                dst = tar_dir+'/Images'+img_type[type]+f'/{f}'
            elif type in vid_type.keys():
                dst = tar_dir+'/Videos'+vid_type[type]+f'/{f}'
            elif type in aud_type.keys():
                dst = tar_dir+'/Audio'+aud_type[type]+f'/{f}'
            elif type in prg_type.keys():
                dst = tar_dir+'/Programming'+prg_type[type]+f'/{f}'
            else:
                dst = tar_dir+'/Others'+f'/{f}'
            dst = rename_file(dst)  #checking existence of path in destination then renaming if present
            shutil.move(src,dst)    #moving file to the destination path
print('Done :)')