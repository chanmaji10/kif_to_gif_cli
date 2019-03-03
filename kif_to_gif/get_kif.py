import shogi
import shogi.KIF
# import shogi.CSA


def get_kif(kif_file_path):
    kif = shogi.KIF.Parser.parse_file(kif_file_path)[0]
    return kif
