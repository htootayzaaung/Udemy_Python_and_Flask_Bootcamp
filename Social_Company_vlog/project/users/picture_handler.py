import os
from PIL import Image
from flask import url_for, current_app

def add_profile_pic(pic_upload, username):

    filename = pic_upload.filename
    file_extension = filename.split('.')[-1]                                        #Retrieves the file extension of an image file
    storage_filename = str(username) + '.' + file_extension

    filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename)
    output_size = (100, 100)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath, quality = 200)

    return storage_filename 