import base64
import logging
import sys
import xml.etree.ElementTree as ET

from PIL import Image

from io import BytesIO
from os import path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LENGTH_TAG = "length"
MESSAGE_TAG = "message"

'''
Encoder class that
'''
class Encoder:
    def __init__(self, input_image_file_name, input_message_to_encode, output_image_file_name=None):
        self.input_image_file_name = input_image_file_name
        self.input_message_to_encode = input_message_to_encode
        self.output_image_file_name = output_image_file_name

    '''
    Convert the input message to a Base64 encoded xml object and return it.
    '''
    def __convert_message_to_base64(self):
        if self.input_message_to_encode is None:
            logger.error("Can't convert message.")
            sys.exit()

        return base64.b64encode(bytearray(self.input_message_to_encode, 'utf-8'))

    '''
    Embed message into the image
    '''
    def __embed_message_in_xml(self, message):
        if message is None:
            logger.error("Can't convert message.")
            sys.exit()

        body = ET.Element('body')
        body.set(LENGTH_TAG, str(len(str(message))))
        body.set(MESSAGE_TAG, str(message))
        et = ET.ElementTree(body)

        f = BytesIO()
        et.write(f, encoding='utf-8', xml_declaration=True)
        return f.getvalue()

    '''
    Embed message in an Image
    '''
    def __embed_xml_image(self, message):
        if message is None or type(message) is not str:
            logger.error("Can't embed message")
            sys.exit()

    def __convert_string_to_bin(self, string):
        """
        Convert a String to a byte representation of the same.

        :param string: String to be converted to bytes.
        """

        # Take the bytearray of the string and convert each byte into binary format.
        return ''.join([bin(byte)[2:] for byte in bytearray(string)])

    def __encode_bin_in_pixels(self, binary_str, pixels):
        """
        Encode binary string message in pixels.

        :param binary_str:
        :param pixels:
        :return:
        """

        str_iter = 0

        # Introduce padding
        rem = len(binary_str) % 3
        if rem != 0:
            binary_str = binary_str + ("0" * rem)

        def _embed_val(p_val, val):
            p_val_str = format(p_val, "08b")
            return p_val_str[:7] + val

        for pixel in pixels:
            r, g, b = pixel

            _embed_val(r, binary_str[str_iter])
            _embed_val(g, binary_str[str_iter + 1])
            _embed_val(b, binary_str[str_iter + 2])

            str_iter += 3
            if str_iter >= len(binary_str):
                break


    '''
    Embed input message (encoded) into the image and save it.
    '''
    def encode(self):
        if not path.exists(self.input_image_file_name):
            logger.error("Input image file does not exist.")
            sys.exit()

        image = Image.open(self.input_image_file_name)
        base64_encoded_message = self.__convert_message_to_base64()
        xml_string = self.__embed_message_in_xml(message=base64_encoded_message.decode('utf-8'))
        xml_string_bin = self.__convert_string_to_bin(xml_string)

        # Get pixels from image.
        pixels = list(image.getdata())

        # Encode
        self.__encode_bin_in_pixels(xml_string_bin, pixels)

        image.close()
