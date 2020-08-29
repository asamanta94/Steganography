import logging
import sys

from os import path

'''
Decoder class to decode a given encoded image.
'''
class Decoder:
    def __init__(self, input_image_file_name, output_message_file_name):
        self.input_image_file_name = input_image_file_name
        self.output_message_file = output_message_file

    def decode(self):
        if not path.exists(self.input_image_file_name):
            logging.error("Input image file does not exist.")
            sys.exit()

        image = Image.open(self.input_image_file_name)

    def decode_image(self):
        pass

    def save_image(self):
        if output_message_file_name is None:
            logging.info("Success!")
