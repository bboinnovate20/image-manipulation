import os
from werkzeug.utils import secure_filename
from image_res import removeBackground, sharpenImage
from datetime import datetime, timedelta

def upload_image(file):
    try:
        print(file);
        if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            return False;
        
        upload_folder = 'uploads'
        os.makedirs(upload_folder, exist_ok=True)
        ext = file.filename.split('.')[-1];
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = 'image-'+timestamp+"."+ext;
        file_path = os.path.join(upload_folder, secure_filename('image-'+timestamp+"."+ext));
        file.save(file_path)
        return (file_path, file_name);
    
    except:
      return (False, None)

    

def features(feature, path, filename):

    if(feature == 'remove-bg'):
        result = removeBackground(path, filename.split('.')[0]);
        return result
    
    if(feature == 'img-quality'):
        result = sharpenImage(path, filename);
        return result;
         
def schedule_deletion(folder_path):
    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # Loop through files in the folder
        for filename in os.listdir(folder_path):
            # Check if the current item is a file
            try:
                get_time_stamp = filename.split('-')[1].split('.')[0];
                timestamp_datetime = datetime.strptime(get_time_stamp, "%Y%m%d%H%M%S")
                time_difference = datetime.now() - timestamp_datetime
                expire_time = timedelta(minutes=10);
                
                if(time_difference > expire_time):
                    file_path = os.path.join(folder_path, filename)
                    if os.path.isfile(file_path):
                        delete_file(file_path)
            except:
                pass
            


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")