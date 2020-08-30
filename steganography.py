import logging
import time

from decoder import Decoder
from encoder import Encoder

LOGGING_FORMAT = "[%(levelname)s] - %(message)s"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Steganography:

    @staticmethod
    def parse_args(args):
        vars_args = vars(args)
        if vars_args['decode']:
            input_image_file_name = vars_args['input']
            output_image_text_file_name = vars_args['output']

            decoder = Decoder(input_image_file_name, output_image_text_file_name)
            print(decoder.decode())
        else:
            input_image_file_name = vars_args['input']
            input_message_to_encode = vars_args['message']
            output_image_file_name = vars_args['output']

            encoder = Encoder(input_image_file_name, input_message_to_encode, output_image_file_name)

            logger.setLevel(logging.INFO)
            logger.info("Starting to encode.")

            start = time.time()
            encoder.encode()
            end = time.time()

            logger.info("Finished encoding.")
            logger.info("Encoding took: {0} seconds".format(end - start))
