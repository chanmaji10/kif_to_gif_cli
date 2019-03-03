import cv2
import shogi
import sys
from kif_to_gif import initialize_board
from kif_to_gif import create_board_image
from kif_to_gif import create_hand_pieces_image


def make_images(kif, initialize, start, end):
    # initialize_board
    board, sign_horizontal, sign_vertical, images = initialize_board.initialize_board(initialize, start, end)

    image_file_num = 1
    for num, move in enumerate(kif['moves']):
        # board push is reflect move
        board.push(shogi.Move.from_usi(move))

        # output range
        if start <= num + 1 and end >= num + 1:
            # create board image
            board_img = create_board_image(board, initialize, sign_horizontal, sign_vertical)
            # create hand pieces image
            hand_img_b, hand_img_w = create_hand_pieces_image.create_hand_pieces_image(board.pieces_in_hand)

            # join w, Board, b
            if initialize:
                hand_img_w = cv2.flip(hand_img_w, -1)
                board_img = cv2.hconcat([hand_img_w, board_img, hand_img_b])

            else:
                hand_img_b = cv2.flip(hand_img_b, -1)
                board_img = cv2.hconcat([hand_img_b, board_img, hand_img_w])

            # write
            cv2.imwrite('./tmp_img/' + str(image_file_num) + '.png', board_img)
            print('./tmp_img/' + str(image_file_num) + '.png')
            images.append(board_img)
            image_file_num += 1
    return images
