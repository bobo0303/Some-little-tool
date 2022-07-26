def concat_zoom_and_original_img(original_box_img, zoom_img_set, config_):
    direction_lsit = ['top', 'below', 'left', 'right']
    #if direction == None:   raise Exception(f'\nPlease choose direction {direction_lsit}')
    direction = 3

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
            zoom_img = np.hstack([zoom_img, zoom_img_set[n]])
        zoom_img_shape = zoom_img.shape[0:2]
        original_box_img_shape = original_box_img.shape[0:2]
        zoom_img = cv2.resize(zoom_img, (zoom_img_shape[1], original_box_img_shape[0]))
        if config_['CROP']['POSITION'] == 'R':
            final_img = np.hstack([zoom_img, original_box_img])
        elif config_['CROP']['POSITION'] == 'L':
            final_img = np.hstack([zoom_img, original_box_img])
    else:
        raise Exception(f'\nPlease choose direction {direction_lsit}')

    return final_img
