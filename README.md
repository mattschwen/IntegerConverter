# Integer Converter

This is a command-line tool that converts integer strings in a text file to integers. The tool uses a regular expression pattern to match integer strings and then converts them to integers.

## Installation

To install the tool, follow these steps:

## Usage

To use the tool, open a terminal or command prompt and navigate to the directory where the repository was cloned. Then run the following command:
<pre><span class="">css</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button><code class="!whitespace-pre hljs language-css">python integer_converter<span class="hljs-selector-class">.py</span> input_file <span class="hljs-selector-attr">[-o OUTPUT_FILE]</span> <span class="hljs-selector-attr">[-r]</span>
</code></pre>where:

* `input_file`: The name of the input file to convert. This is a required argument.*`-o OUTPUT_FILE`: The name of the output file. If this option is not provided, a default output file with the name "input_file_output.txt" will be created in the same directory as the input file.* `-r`: A flag that specifies whether to replace the contents of the input file with the converted text instead of creating a new output file.### Examples
Convert integers in input.txt and create output.txt:

<pre><span class="">lua</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button><code class="!whitespace-pre hljs language-lua">python integer_converter.py <span class="hljs-built_in">input</span>.txt -o <span class="hljs-built_in">output</span>.txt
</code></pre>Convert integers in input.txt and replace the contents of the input file:
<pre><span class="">python</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button><code class="!whitespace-pre hljs language-python">python integer_converter.py <span class="hljs-built_in">input</span>.txt -r
</code></pre>

## Logging
The tool uses the built-in `logging` module to log information about the conversion process. By default, the logging level is set to `INFO`, but this can be changed by modifying the `level` parameter in the `basicConfig` function call in the script.
The log messages are written to the console and to a log file in the same directory as the input file. The name of the log file is "integer_converter.log".

## Exceptions

The tool uses a try-except block to catch any exceptions that may occur during the conversion process. If an exception occurs, an error message is logged with the details of the error.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions are welcome!

## License

This tool is licensed under the MIT License. See the LICENSE file for details.
