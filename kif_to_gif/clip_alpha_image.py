import cv2
import numpy as np


def clip_alpha_image(x, y, background, foreground):
    f_h, f_w, _ = foreground.shape
    alpha_mask = np.ones((f_h, f_w)) - np.clip(cv2.split(foreground)[3], 0, 1)
    target_background = background[y:y+f_h,x:x+f_w]
    new_background = cv2.merge(list(map(lambda x:x * alpha_mask, cv2.split(target_background))))
    background[y:y + f_h, x:x + f_w] = cv2.merge(cv2.split(foreground)[:3]) + new_background
    return background
