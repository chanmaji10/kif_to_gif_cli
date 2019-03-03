import kif_to_gif as ktg


def kiftogif(kif_file_path, file_name, game_range=[0, 999], duration=1500, initialize=1, start=0, end=999):
    kif = ktg.get_kif(ktg.format_file(kif_file_path))
    print(kif)
    images = ktg.make_images(kif, initialize, game_range[0], game_range[1])
    print(len(images))
    ktg.create_gif(images, file_name, duration)


kiftogif("./fujii_imai.kif", 'hoge')
print('kif_to_gif_cli!')

