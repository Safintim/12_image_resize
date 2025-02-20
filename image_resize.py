import os
import argparse
from PIL import Image


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.scale and (namespace.width or namespace.height):
        raise ValueError('You cannot scale the image when the dimensions are specified')
    resize_image(
        image=namespace.image,
        height=namespace.height,
        width=namespace.width,
        scale=namespace.scale,
        output=namespace.output
    )


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=is_valid_extension, required=True, help='Path to image')
    parser.add_argument('-wt', '--width', type=int, help='Width image')
    parser.add_argument('-ht', '--height', type=int, help='Height image')
    parser.add_argument('-s', '--scale', type=int, help='Scale')
    parser.add_argument('-o', '--output',  help='Output path')
    return parser


def is_valid_extension(imagepath, extensions=('.jpg', '.jpeg', '.png')):
    _, extension = os.path.splitext(imagepath)
    if extension.lower() in extensions:
        return imagepath
    raise argparse.ArgumentTypeError('not valid extension. Needed {}'.format(extensions))


def resize_image(image, width=None, height=None, scale=None, output=None):
    img = Image.open(image)
    original_width, original_height = img.size

    if original_width // original_height != width // height:
        print('Proportion do not match')

    if scale:
        img = scale_image(img, original_width, original_height, scale)

    if width and height:
        img = img.resize((width, height))
    elif width:
        img.thumbnail((width, original_height), Image.ANTIALIAS)
    elif height:
        img.thumbnail((original_width, height), Image.ANTIALIAS)

    save_image(image, img, output)


def scale_image(img, original_width, original_height, scale):
    if scale > 0:
        return img.resize((original_width * scale, original_height * scale))
    return img.resize((original_width // abs(scale), original_height // abs(scale)))


def save_image(imagepath, img_obj, output):
    if not output:
        image_name, extension = os.path.splitext(imagepath)
        new_image_name = '{}_{}x{}{}'.format(image_name, img_obj.size[0], img_obj.size[1], extension)
        img_obj.save(new_image_name)
    img_obj.save(output)

if __name__ == '__main__':
    main()
