from PIL import Image


def create_gif(images, file_name, duration):
    ims = []
    for i in images:
        im = Image.fromarray(i[:, :, ::-1])
        ims.append(im)

    ims[0].save('{}.gif'.format(file_name),
                save_all=True,
                append_images=ims[1:],
                optimize=False,
                duration=duration,
                loop=0)
