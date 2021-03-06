import exifread
import glob
import os
import time
import cv2


def get_photo_date(file_name):
    # Open image file for reading (binary mode)
    file = open(file_name, 'rb')
    # Return Exif tags
    tags = exifread.process_file(file, stop_tag="EXIF DateTimeOriginal")
    # print("Number: ", "\t", tags)             # For testing
    time_n_date = tags["EXIF DateTimeOriginal"]
    new_time_n_date = str(time_n_date)
    date = new_time_n_date.split(" ")[0]
    new_date = date.split(":")
    # year = new_date[0]        # For remembering of order
    # month = new_date[1]
    # day = new_date[2]
    return new_date


def get_year(new_list):
    res = new_list[0]
    return res


def get_month(new_list):
    res = new_list[1]
    return res


def get_day(new_list):
    res = new_list[2]
    return res


def create_dirs(fisrPart, year_loc, month_loc):
    # n_path = str("C:/Sorted/" + year_loc + "/" + month_loc)
    n_path = str(fisrPart+"/" + year_loc + "/" + month_loc)
    try:
        os.makedirs(n_path, exist_ok = True)
        print("Directory '%s' created successfully" % n_path)
    except OSError as error:
        print("Directory '%s' can not be created")


def process_all(file, destination_folder):
    file_name = file.split("\\")[1]
    photo = get_photo_date(file)
    day = get_day(photo)    # Currently not used
    month = get_month(photo)
    year = get_year(photo)
    image = cv2.imread(file)
    # create_dirs("C:/Sorted/", str(year), str(month))
    # name = str('C:/Sorted/' + year + '/' + month + '/' + file_name)
    create_dirs(destination_folder, str(year), str(month))
    name = str(destination_folder + '/' + year + '/' + month + '/' + file_name)
    cv2.imwrite(name, image)
    # print(name)


def creation_date_video(path_to_file):
    """
        Currently not implemented
        First print returns date of modifications to the video file
        Second print prints date of Creation of the video file, literally time when it was written to folder
    """
    print("Last modified: %s" % time.ctime(os.path.getmtime(path_to_file)))
    print("Created: %s" % time.ctime(os.path.getctime(path_to_file)))
    # return os.path.getctime(path_to_file)


def main_one(string_path_to_folder, destination_folder):
    """We give location of folder as input"""
    # .jpg and .JPG are the same
    # photos = glob.glob("C:/Personal/pp2_photo/dataBase/*.JPG") # Examples of location format
    # pho = glob.glob("C:/Personal/pp2_photo/dataBase/*.jpg")
    photos = glob.glob(string_path_to_folder+"/*.JPG")
    print("Number of files: ", len(photos))
    for k in photos:
        print(get_photo_date(k))
        process_all(k, destination_folder)


# path = os.getcwd()
# print("The current working directory is %s" % path)
# main_one("C:/Personal/pp2_photo/dataBase")

"""TESTING PART"""
# for i in photos:
#     process_all(i)
'''
    FOR TESTING PURPOSES
    file = open(i, 'rb')
    Return Exif tags
    tags = exifread.process_file(file, stop_tag="EXIF DateTimeOriginal")
    dateTaken = tags["EXIF DateTimeOriginal"]
    print(dateTaken)
'''

# creation_date_video("C:/Personal/pp2_photo/video/school_collage_4.mp4")
