import logging
import sys

from os import path
from PIL import Image


class Decoder:
    """
    Decoder class to decode a given encoded image.
    """
    def __init__(self, input_image_file_name, output_message_file_name):
        self.input_image_file_name = input_image_file_name
        self.output_message_file = output_message_file_name

    def decode(self):
        if not path.exists(self.input_image_file_name):
            logging.error("Input image file {} does not exist.".format(self.input_image_file_name))
            sys.exit()

        image = Image.open(self.input_image_file_name).convert("RGB")

        pixels = image.load()

        width, height = image.size

        str_concat = ""
        xml_str = ""
        k = 0

        for i in range(0, width):
            for j in range(0, height):
                r, g, b = pixels[i, j]

                r_bin_str = format(r, "08b")
                g_bin_str = format(g, "08b")
                b_bin_str = format(b, "08b")

                str_concat += r_bin_str[7]
                k += 1
                if k == 8:
                    k = 0
                    x = int(str_concat, 2).to_bytes(8, "big").decode("utf-8")
                    xml_str += x
                    if x == '>':
                        return xml_str
                    str_concat = ""

                str_concat += g_bin_str[7]
                k += 1
                if k == 8:
                    k = 0
                    x = int(str_concat, 2).to_bytes(4, "big").decode("utf-8")
                    xml_str += x
                    if x == '>':
                        return xml_str
                    str_concat = ""

                str_concat += b_bin_str[7]
                k += 1
                if k == 8:
                    k = 0
                    x = int(str_concat, 2).to_bytes(4, "big").decode("utf-8")
                    xml_str += x
                    if x == '>':
                        return xml_str
                    str_concat = ""

                # k += 1
                #
                # if k == 168:
                #     return str_concat

    def decode_image(self):
        pass

    def save_image(self):
        if self.output_message_file_name is None:
            logging.info("Success!")
