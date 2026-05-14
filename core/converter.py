from PIL import Image


def convert_to_ico(input_path, output_path, sizes):
    """
    Convert an image to ICO format with specified sizes.
    Returns True on success, False on failure.
    """
    try:
        img = Image.open(input_path)
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        img.save(output_path, format="ICO", sizes=sizes)
        return True
    except Exception as e:
        # The main window will show the error; we re-raise or return False
        raise e