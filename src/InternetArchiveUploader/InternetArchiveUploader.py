from internetarchive import get_item,ArchiveSession,Item,search_items,configure
import configparser
import os



# add ability to write full tracebacks Done
class InternetArchiveUploader():
    def __init__(self,identifier,base_metadata,username,password) -> None:
     
        configure(username,password,config_file='config.ini')
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.S3_ACCESS_KEY=config['s3']['access'] 
        self.S3_SECRET_KEY=config['s3']['secret'] 
        
        self.metadata=base_metadata
        self.identifier=identifier
        self.archivesession= ArchiveSession()
        self.item = Item(identifier=identifier,archive_session=self.archivesession)
    
        
   
    def retrieveFilesFromInternetArchive(self):
        searchIdentifiers=search_items(f'identifier:{self.identifier}')
        if not searchIdentifiers.num_found:
            return []
        for result in searchIdentifiers.iter_as_items():
            return [file_name['name'] for file_name in result.files]
    # upload file and upload directory need to be optionally async  
    def uploadFile(self,file:str):
        files_in_archive=self.retrieveFilesFromInternetArchive()
        if(os.path.isdir(file) or file in files_in_archive):
            return
        #try:
        r = self.item.upload(file, metadata=self.metadata, access_key=self.S3_ACCESS_KEY, secret_key=self.S3_SECRET_KEY,verbose=True)
       
    def uploadDirectory(self,dir_path):
        files_in_archive=self.retrieveFilesFromInternetArchive()
        for file in os.listdir(dir_path):
            full_path=f'{dir_path}/{file}'
            # If file is a directory or the file is already in the archive just skip it
            if(os.path.isdir(full_path) or file in files_in_archive):
                continue
        
            r = self.item.upload(full_path, metadata=self.metadata, access_key=self.S3_ACCESS_KEY, secret_key=self.S3_SECRET_KEY,verbose=True)

