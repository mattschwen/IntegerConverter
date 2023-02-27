import argparse
import logging
import re


class IntegerConverter:
    def __init__(self, input_file, output_file, replace_existing):
        """Initializes the IntegerConverter class.

        Args:
            input_file (str): The name of the input file.
            output_file (str): The name of the output file.
            replace_existing (bool): A flag that specifies whether to replace the contents of the input file with the
            converted text instead of creating a new output file.
        """
        self.input_file = input_file
        self.output_file = output_file
        self.replace_existing = replace_existing
        self.pattern = re.compile(r'(\d+)')  # Define a regular expression pattern to match integer strings

    def convert(self):
        """Converts integer strings in a text file to integers.

        Reads the contents of the input file, converts integer strings to integers, and writes the converted text to
        the output file (or the input file if the replace_existing flag is set).
        """
        try:
            with open(self.input_file, 'r') as input_file:
                input_text = input_file.read()

            if self.replace_existing:
                output_text = re.sub(self.pattern, lambda m: str(int(m.group(0))), input_text)
                with open(self.input_file, 'w') as output_file:
                    output_file.write(output_text)
            else:
                output_text = re.sub(self.pattern, lambda m: str(int(m.group(0))), input_text)
                with open(self.output_file, 'w') as output_file:
                    output_file.write(output_text)
            logging.info('Conversion completed successfully.')
        except Exception as e:
            logging.error(f'Error during conversion: {str(e)}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    parser = argparse.ArgumentParser(description='Convert integer strings in a text file to integers')
    parser.add_argument('input_file', help='the name of the input file')
    parser.add_argument('-o', '--output-file', help='the name of the output file', default=None)
    parser.add_argument('-r', '--replace-existing', action='store_true',
                        help='replace the contents of the input file instead of creating a new output file')
    args = parser.parse_args()

    output_file = args.output_file or f"{args.input_file.split('.')[0]}_output.txt"

    converter = IntegerConverter(args.input_file, output_file, args.replace_existing)
    converter.convert()