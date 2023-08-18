# Graphviz Workaround Utility for Linux

## Description:
This is a Linux workaround utility for those who use the Trace Java tool and encounter the issue where `dot` isn't recognized even when installed. It aids in converting GraphViz outputs into images, specifically PNG format, when new `.gv` files are detected in a specified output directory.

## Why I Made This:
I developed this utility due to an existing issue on Linux that prevented the Trace Java utility from utilizing the `dot` command, even when it was properly installed. This tool serves as a bridge to overcome this limitation and ensure seamless image conversion.

## Requirements:
- Python 3.x
- watchdog (`pip install watchdog`)
- GraphViz (`dot` command should be available)

## Usage:
\```bash
python monitor.py /path/to/GraphViz/Output
\```

## How it Works:

### `GraphvizOutputHandler` class:

- This class is responsible for monitoring any new directories created in the specified `output_folder`.
- When a new directory is detected, it checks the directory for `.gv` files.
- For each `.gv` file found, it:
  1. Converts the `.gv` file into a `.png` image using the `dot` command.
  2. Deletes the `.gv` file after conversion.

### `monitor_directory` function:

- Initiates monitoring on the specified `output_folder` using the `GraphvizOutputHandler` event handler.
- Keeps running indefinitely unless interrupted by the user.

## Important Notes:

- Ensure you have the `dot` command available in your PATH. This utility relies on it for conversion.
- Make sure you provide the correct path to the `GraphViz` output folder when executing the script. 

## Limitations:
- Any `.gv` file added to a newly created directory inside the specified `output_folder` will be deleted after being converted to `.png`. Ensure you have backup copies if necessary.
