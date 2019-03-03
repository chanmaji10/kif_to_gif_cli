import cv2
import shogi
from kif_to_gif import clip_alpha_image


def create_board_image(board, initialize, sign_horizontal, sign_vertical):
    index = list('ABCDEFGHI')
    col_images = []
    for i in index:
        row_images = []
        for c in range(9, 0, -1):
            # get piece on  this cell
            point = board.piece_at(getattr(shogi, i+str(c)))
            point_img = cv2.imread('./images/' + str(point).upper() + '.png', -1)

            # cell flip
            if str(point).islower():
                point_img = cv2.flip(point_img, -1)

            row_images.append(point_img)

        # join row_images
        raw_img = cv2.hconcat(row_images)
        col_images.append(raw_img)

    # join col_images
    column_img = cv2.vconcat(col_images)

    # add background
    board_img = cv2.imread('./images/bord.png')
    clip_alpha_image(0, 0, board_img, column_img)

    # flip board
    if not initialize:
        board_img = cv2.flip(board_img, -1)

    # add sign images
    board_img = cv2.vconcat([sign_horizontal, board_img])
    board_img = cv2.hconcat([board_img, sign_vertical])
    return board_img



