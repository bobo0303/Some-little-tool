import glob
from PIL import Image
import math
import yaml
import os
import numpy as np
from natsort import natsorted
import cv2
from glob import glob
from tqdm import tqdm


def save_img(filepath, img):
    cv2.imwrite(filepath, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))


def get_color(c, x, max_val):
    colors = np.array([[1, 0, 1], [0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0], [1, 0, 0]], dtype=np.float32)
    ratio = float(x) / max_val * 5
    i = int(math.floor(ratio))
    j = int(math.ceil(ratio))
    ratio = ratio - i
    r = (1 - ratio) * colors[i][c] + ratio * colors[j][c]
    return int(r * 255)


def concat_zoom_and_original_img(original_box_img, zoom_img_set, config_):
    direction_lsit = ['top', 'below', 'left', 'right']
    zoom_img_set_shape = np.shape(zoom_img_set)
    zoom_img = zoom_img_set[0]
    if config_['CROP']['POSITION'] in ['T', 'B']:
        for n in range(1,zoom_img_set_shape[0]):
            zoom_img = np.hstack([zoom_img, zoom_img_set[n]])
        zoom_img_shape = zoom_img.shape[0:2]
        original_box_img_shape = original_box_img.shape[0:2]
        zoom_img = cv2.resize(zoom_img, (original_box_img_shape[1], zoom_img_shape[0]))
        if config_['CROP']['POSITION'] == 'T':
            final_img = np.vstack([zoom_img, original_box_img])
        elif config_['CROP']['POSITION'] == 'B':
            final_img = np.vstack([original_box_img, zoom_img])

    elif config_['CROP']['POSITION'] in ['L', 'R']:
        for n in range(1, zoom_img_set_shape[0]):
            zoom_img = np.vstack([zoom_img, zoom_img_set[n]])
        zoom_img_shape = zoom_img.shape[0:2]
        original_box_img_shape = original_box_img.shape[0:2]
        zoom_img = cv2.resize(zoom_img, (zoom_img_shape[1], original_box_img_shape[0]))
        if config_['CROP']['POSITION'] == 'R':
            final_img = np.hstack([original_box_img, zoom_img])
        elif config_['CROP']['POSITION'] == 'L':
            final_img = np.hstack([zoom_img, original_box_img])
    else:
        raise Exception(f'\nPlease choose direction {direction_lsit}')
    return final_img



def color_pad(zoom_patch, color, thickness):
    padding_img = []
    for channel in range(zoom_patch.shape[-1]):
        padding_img.append(np.pad(zoom_patch[:, :, channel], ((thickness, thickness), (thickness, thickness)), 'constant', constant_values=color[channel]))
    padding_img = np.array(padding_img, dtype=np.uint8)
    padding_img = padding_img.transpose(1, 2, 0)

    return padding_img

def crop_zoom_patch(original_img, config_):
    thickness = config_['CROP']['BOX_THICK']
    cropping_size = config_['CROP']['BOX_SIZES']
    color = (0, 255, 0)
    zoom_img_set = []
    h, w = original_img.shape[0], original_img.shape[1]
    original_box_img = original_img
    for i in range(config_['CROP']['NUMBER']):
        if config_['CROP']['POSITION'] not in ['R', 'L', 'T', 'B']: raise Exception(f'\nThe position only support "L", "R", "T", "B"')
        if config_['CROP']['POSITION'] in ['R', 'L']: size_patch = h // config_['CROP']['NUMBER']
        else: size_patch = w // config_['CROP']['NUMBER']

        if config_['CROP']['RANDOM']:  # random choose the location
            row = random.randint(0, w - cropping_size - thickness)
            col = random.randint(0, h - cropping_size - thickness)
            top_left_location = [row, col]

        else:  # user choose the location
            if len(config_['CROP']['BOX_LOCAT']) != config_['CROP']['NUMBER']: raise Exception(f'\nThe number of "BOX_LOCAT" and "NUMBER" have be the same!')

            top_left_location = config_['CROP']['BOX_LOCAT'][i]
            if top_left_location[0] + cropping_size + thickness > w or top_left_location[1] + cropping_size + thickness > h:
                raise Exception(f'\n The pixel location range is [0~{w - cropping_size - thickness}, 0~{h - cropping_size - thickness}]!')

        bottom_right_location = [cropping_size + val for val in top_left_location]
        zoom_img = original_img[top_left_location[1]:top_left_location[1] + cropping_size, top_left_location[0]:top_left_location[0] + cropping_size, :]
        zoom_img = color_pad(zoom_img, color, thickness)
        # cv2.imshow("cropped", zoom_img)
        # cv2.waitKey(0)
        zoom_img = cv2.resize(zoom_img, (size_patch, size_patch), interpolation=cv2.INTER_CUBIC)
        zoom_img_set.append(zoom_img)
        original_box_img = cv2.rectangle(original_box_img, tuple(top_left_location), tuple(bottom_right_location), color=color, thickness=thickness)
    # cv2.imshow("cropped", original_box_img)
    # cv2.waitKey(0)
    final_img = concat_zoom_and_original_img(original_box_img, zoom_img_set, config_)

    return final_img


if __name__ == "__main__":
    ## Load yaml configuration file
    with open('config.yaml', 'r') as config:
        opt = yaml.safe_load(config)

    img_type = opt['IMG']['TYPE']
    img_input = opt['PATH']['INPUT_DIR']

    os.makedirs(opt['PATH']['SAVE_DIR'], exist_ok=True)

    files_img = natsorted(glob(os.path.join(img_input, f'*.{img_type}')))

    if len(files_img) == 0: raise Exception(f'\nNo {img_type} files found at {img_input}')

    for img_path in files_img:
        img_name = os.path.splitext(os.path.split(img_path)[-1])[0]
        img_degraded = cv2.imread(img_path)

        # img_degraded = Image.open(name_degraded).convert('RGB')
        # img_restored = Image.open(name_restored).convert('RGB')

        img_result = crop_zoom_patch(img_degraded, opt)

        save_img((os.path.join(opt['PATH']['SAVE_DIR'], img_name + '.png')), img_result)