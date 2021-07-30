import os
subdirectories= {
    "DOCUMENTS":['.pdf','.txt',',rtf'],
    "AUDIO":['.mp3','.m4v','.m4a'],
    "IMAGES":['.jpg','.jpeg','png'],
    "VIDEOS":['.mp4','.avi','.mov']

}
def pickDirectory(value):
    for category, suffixes in subdirectories.items():
        for suffix in suffixes:
            if suffix ==value:
                return category
    return 'MISC'
print(pickDirectory('.pdf'))

def organize():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath= Path(item)
        fileType=filePath.suffix.lower()
        directory=pickDirectory(fileType)
        directorypath=Path(directory)
        if directorypath.is_dir()!=True:
            directorypath.mkdir()
        filePath.rename(directorypath.joinpath(filePath))
