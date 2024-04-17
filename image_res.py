import cv2
from rembg import remove
from PIL import Image
import numpy as np

def main():
    
    pass

def removeBackground(input_path, filename): 
    try:
        input = Image.open(input_path)
        result = remove(input, alpha_matting=True);
        file_path = './src/processed_image/{}.png'.format(filename);
        result.save(file_path)
        return (True, file_path, '{}.png'.format(filename));
    except:
        return (False, None, '')



def sharpenImage(image_path, filename):
    try:
        file_path = './src/processed_image/{}'.format(filename);
        model_name = 'ESPCN'.lower();
        model_scale = 4;
        sr = cv2.dnn_superres.DnnSuperResImpl_create();
        sr.readModel("./bin/models/ESPCN_x4.pb");
        sr.setModel(model_name, model_scale);
        image = cv2.imread(image_path);
        up_scaled = sr.upsample(image);       
        cv2.imwrite(file_path, up_scaled);

        return (True, file_path, '{}'.format(filename));
    except Exception as e:
        print('error! {}'.format(e))
        return (False, None, "")


main();