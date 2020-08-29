import argparse

from steganography import Steganography


def main():
    parser = argparse.ArgumentParser(description='Do some steganography.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--encode', action="store_true",
                    help='for encoding an image')
    group.add_argument('--decode', action="store_true",
                    help='for decoding an image')
    parser.add_argument('--input', type=str, required=True,
                    help='input image file name for encoding/decoding message')
    parser.add_argument('--message', type=str,
                    help='input message file for encoding the message in to the input image')
    parser.add_argument('--output', type=str,
                    help='output image file for the encoded image/decoded message')

    args = parser.parse_args()
    Steganography.parse_args(args=args)


if __name__ == "__main__":
    main()
