import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class GraphvizOutputHandler(FileSystemEventHandler):
    def __init__(self, output_folder):
        self.output_folder = output_folder

    def on_created(self, event):
        if event.is_directory and os.path.dirname(event.src_path) == self.output_folder:
            print(f"New folder created: {event.src_path}")
            self.convert_gv_files(event.src_path)

    def convert_gv_files(self, folder_path):
        print(f"Checking files in folder: {folder_path}")
        time.sleep(5)
        print(os.path.isdir(folder_path))
        files = os.listdir(folder_path)
        print(f"Found {len(files)} files.")
        for file in files:
            print(f"Found file: {file}")
            if file.endswith('.gv'):
                input_file = os.path.join(folder_path, file)
                output_file = os.path.splitext(input_file)[0] + '.png'
                print(f"Converting {input_file} to {output_file}")
                subprocess.run(['dot', '-Tpng', input_file, '-o', output_file])
                print("Deleting file")
                os.remove(input_file)


def monitor_directory(output_folder):
    event_handler = GraphvizOutputHandler(output_folder)
    observer = Observer()
    observer.schedule(event_handler, output_folder, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python monitor.py /path/to/GraphViz/Output")
        sys.exit(1)

    output_folder = sys.argv[1]
    monitor_directory(output_folder)
