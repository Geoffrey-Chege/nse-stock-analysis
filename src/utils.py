import glob
import os

def get_latest_file(directory, extension="csv"):
    """
    Return the path to the most recently modified file in the specified directory
    with the given extension.
    """
    pattern = os.path.join(directory, f"*.{extension}")
    files = glob.glob(pattern)
    if not files:
        raise FileNotFoundError(f"No .{extension} files found in {directory}")
    latest_file = max(files, key=os.path.getmtime)
    return latest_file