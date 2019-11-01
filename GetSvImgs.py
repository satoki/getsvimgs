import json
import os
import random
import requests
from tqdm import tqdm


def make_url(fov, heading, key, location, pitch, size, source):
    return "https://maps.googleapis.com/maps/api/streetview"\
          +"?size="+size\
          +"&fov="+str(fov)\
          +"&heading="+str(heading)\
          +"&key="+key\
          +"&location="+location\
          +"&pitch="+str(pitch)\
          +"&source="+source

def image_exists(url):
    c_url = url.replace("streetview?", "streetview/metadata?")
    g_url = requests.get(c_url)
    status = json.loads(g_url.text)["status"]
    #print(status)
    if status == "OK":
        return True
    elif status == "REQUEST_DENIED":
        message = "Check API_KEY"
        raise Exception("[{}]:{}".format(message, status))
    else:
        return False

def get_image(direname, filename, url):
    g_url = requests.get(url)
    os.makedirs(direname, exist_ok=True)
    with open("{}/{}.jpg".format(direname, filename), mode="wb") as t_file:
        t_file.write(g_url.content)

def set_location(latitude, longitude, range):
    latitude_1km = 0.0090133729745762
    longitude_1km = 0.010966404715491394
    latitude = latitude+(random.uniform(0, range*2)-range)*latitude_1km
    longitude = longitude+(random.uniform(0, range*2)-range)*longitude_1km
    return "{},{}".format(latitude, longitude)

def main():
    _api_key = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" ##API_KEY
    _prefecture, _latitude, _longitude = (
        "Tokyo", 35.6812362, 139.7671248
        #"Nagoya", 35.170915, 136.8815369
        #"Osaka", 34.7024854, 135.4959506
    )
    _fov = "100" ##0~120
    _headings = [0,90,180,270] ##N:0,E:90,S:180,W:270
    _pitch = "40" ##-90~90
    _size = "400x400" ##~640x640
    _source = "outdoor"

    _m_range = 5 ##moving range
    _n_o_images = 500 ##number of images

    try:
        number = 0
        progressbar = tqdm(range(_n_o_images))
        while number < _n_o_images:
            location = set_location(_latitude, _longitude, _m_range)
            for heading in _headings:
                i_url = make_url(_fov, heading, _api_key, location, _pitch, _size, _source)
                #print(i_url)
                if image_exists(i_url):
                    number += 1
                    progressbar.update(1)
                    get_image(_prefecture, "{}_{}_{}".format(number, heading, location), i_url)
                else:
                    break
        progressbar.close()
        print("[{},{}]:OK".format(_prefecture, number))
    except Exception as error:
        progressbar.close()
        print(error)

if __name__ == '__main__':
    main()