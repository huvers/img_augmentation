__author__ = 'Sean Huver'
__email__ = 'huvers@gmail.com'

import sys
import os
import numpy as np

from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import Image
import random


def load_np_image(infilename) :
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="int32" )
    return data


def save_image(npdata, outfilename):
    img = Image.fromarray(np.asarray(np.clip(npdata, 0, 255), dtype="uint8"))
    img.save(outfilename)


def make_blur_img(file_name, path_dir):
    file_path = path_dir + '/' + file_name
    img = Image.open('%s' % file_path)
    img.filter(ImageFilter.BLUR).save(path_dir + '/' + '%02s_blur'
                                      % file_name.translate(None, '.png') + '.png', "PNG")
    return


def make_bright_img(file_name, path_dir):
    file_path = path_dir + '/' + file_name
    img = Image.open('%s' % file_path)
    ImageEnhance.Brightness(img).enhance(1.5).save(path_dir + '/' + '%02s_dim'
                                                    % file_name.translate(None, '.png') + '.png', "PNG")
    return


def make_clr_chg(file_name, path_dir):
    file_path = path_dir + '/' + file_name
    img = Image.open('%s' % file_path)
    ImageEnhance.Color(img).enhance(0.8).save(path_dir + '/' + '%02s_clr'
                                              % file_name.translate(None, '.png') + '.png', "PNG")
    return


def make_contrast_chg(file_name, path_dir):
    file_path = path_dir + '/' + file_name
    img = Image.open('%s' % file_path)
    ImageEnhance.Contrast(img).enhance(0.8).save(path_dir + '/' + '%02s_ctrt'
                                                 % file_name.translate(None, '.png') + '.png', "PNG")
    return


def make_rot_img(file_name, path_dir):
    file_path = path_dir + '/' + file_name
    img = Image.open('%s' % file_path)
    img.rotate(180).save(path_dir + '/' + '%02s_rot1' % file_name.translate(None, '.png') + '.png', "PNG")
    img.rotate( 90).save(path_dir + '/' + '%02s_rot2' % file_name.translate(None, '.png') + '.png', "PNG")
    img.rotate(-90).save(path_dir + '/' + '%02s_rot3' % file_name.translate(None, '.png') + '.png', "PNG")
    img.rotate(-180).save(path_dir + '/' + '%02s_rot4' % file_name.translate(None, '.png') + '.png', "PNG")


def make_noise_img(file_name, path_dir):
    file_path = path_dir + '/' + file_name
    img = load_np_image('%s' % file_path)
    array_shape = img.shape
    noise = np.random.randint(1, 100, size=array_shape)
    img += noise
    rand_name = str(np.random.randint(1,1000))
    file_name = path_dir + '/' + rand_name + '%02s_nz' % file_name.translate(None, '.png') +'.png'
    save_image(img, file_name)


def main():

    if len(sys.argv) < 2:
        print "No folder given for synthetic data creation."
        print "Usage: python create_synthetic_data.py [folder]"
        sys.exit()

    target_path_dir = sys.argv[1]

    num_noise_imgs = 200

    for sub_dir in os.walk(target_path_dir).next()[1]:
        for image in os.listdir(target_path_dir + '/' + sub_dir):
            make_rot_img(image, target_path_dir + '/' + sub_dir)
            for image in os.listdir(target_path_dir + '/' + sub_dir):
                make_bright_img(image, target_path_dir + '/' + sub_dir)
                make_clr_chg(image, target_path_dir + '/' + sub_dir)
                make_contrast_chg(image, target_path_dir + '/' + sub_dir)
                for i in range(num_noise_imgs):
                    make_noise_img(image, target_path_dir + '/' + sub_dir)

if __name__ == "__main__":
    main()
