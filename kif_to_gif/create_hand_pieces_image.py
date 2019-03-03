import shogi
import cv2
from kif_to_gif import clip_alpha_image


def create_hand_pieces_image(hand):
    # change shape
    hand_pieces = [[], []]
    for i, player in enumerate([shogi.BLACK, shogi.WHITE]):
        for p in hand[player].keys():
            hand_pieces[i].append([shogi.Piece(p, player).symbol(), hand[player][p]])

    # create pieces
    hand_piece_images = [[], []]
    for i, player in enumerate(hand_pieces):
        for koma_num, piece_cnt in enumerate(player):
            if piece_cnt[1] == 0:
                komasuu = str(piece_cnt[1]+1)
            else:
                komasuu = str(piece_cnt[1])
                piece = cv2.hconcat([cv2.imread('./images/' + str(piece_cnt[0]) + '.png', -1),
                                     cv2.imread('./images/koma_num/x' + komasuu + '.png', -1)])
                hand_piece_images[i].append(piece)

        hand_piece_images[i] = cv2.vconcat(hand_piece_images[i])

    komadai_img_b, komadai_img_w = hand_piece_images[0], hand_piece_images[1]

    # join background
    for i, (h_p, h_p_images) in enumerate(zip(hand_pieces, hand_piece_images)):
        if h_p:
            hand_piece_images[i] = clip_alpha_image(0, 0, cv2.imread('./images/komadai.png'), h_p_images)
        else:
            hand_piece_images[i] = cv2.imread('./images/komadai.png')
    return hand_piece_images[0], hand_piece_images[1]
