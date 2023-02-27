# Integer Converter

This is a command-line tool that converts integer strings in a text file to integers. The tool uses a regular expression pattern to match integer strings and then converts them to integers.

## Installation

To install the tool, follow these steps:

## Usage

To use the tool, open a terminal or command prompt and navigate to the directory where the repository was cloned. Then run the following command:

```bash
python integer_converter.py nput_file [-o OUTPUT_FILE] [-r]
```

#### Where

* `input_file`: The name of the input file to convert. This is a required argument.*`-o OUTPUT_FILE`: The name of the output file. If this option is not provided, a default output file with the name "input_file_output.txt" will be created in the same directory as the input file.* `-r`: A flag that specifies whether to replace the contents of the input file with the converted text instead of creating a new output file.### Examples
Convert integers in input.txt and create output.txt:

```bash
python integer_converter.py input.txt -o output.txt

```
## Logging
The tool uses the built-in `logging` module to log information about the conversion process. By default, the logging level is set to `INFO`, but this can be changed by modifying the `level` parameter in the `basicConfig` function call in the script.
The log messages are written to the console and to a log file in the same directory as the input file. The name of the log file is "integer_converter.log".

## Exceptions

The tool uses a try-except block to catch any exceptions that may occur during the conversion process. If an exception occurs, an error message is logged with the details of the error.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions are welcome!

## License

This tool is licensed under the MIT License. See the LICENSE file for details.
