import cv2
import shogi

def initialize_board(initiative, start, end):
    board = shogi.Board()
    if initiative:
        sign_horizontal = cv2.imread('./images/sign_horizontal.png')
        sign_vertical = cv2.imread('./images/sign_vertical.png')
    else:
        sign_horizontal = cv2.imread('./images/sign_horizontal2.png')
        sign_vertical = cv2.imread('./images/sign_vertical2.png')

    # 1st image
    if start == 0:
        board0 = cv2.hconcat([cv2.imread('./images/komadai.png'),
                              cv2.vconcat([sign_horizontal, cv2.imread('./images/0.png')]),
                              sign_vertical, cv2.imread('./images/komadai.png')])
        cv2.imwrite('./img/' + '/' + '0.png', board0)
        images = [board0]
    else:
        images = []

    return board, sign_horizontal, sign_vertical, images

