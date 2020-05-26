import glob, exifread, os
import cv2


def get_photo_date(file_name):
    # Open image file for reading (binary mode)
    file = open(file_name, 'rb')

    # Return Exif tags
    tags = exifread.process_file(file, stop_tag="EXIF DateTimeOriginal")
    # print("Number: ", "\t", tags) #For testing
    time_n_date = tags["EXIF DateTimeOriginal"]
    # time_n_date = tags["DateTimeOriginal"]  # It is IfdTag, need to figure out how to get date from it
    new_time_n_date = str(time_n_date)
    date = new_time_n_date.split(" ")[0]
    new_date = date.split(":")
    return new_date
    # year = new_date[0]
    # month = new_date[1]
    # day = new_date[2]


def get_year(new_list):
    res = new_list[0]
    return res


def get_month(new_list):
    res = new_list[1]
    return res


def get_day(new_list):
    res = new_list[2]
    return res


def create_dirs(year_loc, month_loc):
    path = str("C:/Sorted/" + year_loc + "/" + month_loc)
    try:
        os.makedirs(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


def process_all(file):
    file_name = file.split("\\")[1]
    photo = get_photo_date(file)
    day = get_day(photo)
    month = get_month(photo)
    year = get_year(photo)
    image = cv2.imread(file)
    create_dirs(str(year), str(month))
    name = str('C:/Sorted/' + year + '/' + month + '/' + file_name)
    cv2.imwrite(name, image)
    # print(name)


photos = glob.glob("C:/Personal/pp2_photo_files/dataBase/*.JPG")
pho = glob.glob("C:/Personal/pp2_photo_files/dataBase/*.jpg")
# print("Number of files: ", len(photos))
# print("Files list: ", "\n", photos)

path = os.getcwd()
print("The current working directory is %s" % path)
# create_dirs(str(2011), str(0o5))

for i in photos:
    process_all(i)
    # file = open(i, 'rb')
    # Return Exif tags
    # tags = exifread.process_file(file, stop_tag="EXIF DateTimeOriginal")
    # dateTaken = tags["EXIF DateTimeOriginal"]
    # print(dateTaken)

print("gg")
for k in pho:
    process_all(k)
    # Test line
    # file = open(k, 'rb')
    # Return Exif tags
    # tags = exifread.process_file(file, stop_tag="EXIF DateTimeOriginal")
    # dateTaken = tags["EXIF DateTimeOriginal"]
    # print(dateTaken)

