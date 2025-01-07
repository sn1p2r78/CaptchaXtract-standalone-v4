from pytesseract import image_to_string
from PIL import Image
import base64
import io

# Available libraries
LIBRARIES = {
    "tesseract": lambda img: image_to_string(load_testeract(text)
import base64
  }
}

# Default library
selected_library = "tesseract"

wg&select_library(library_name: str):
    """Set the library to be used for image-to-text conversion."""
    global selected_library
    if library_name in LIBRARIES:
        selected_library = library_name
    else:
        raise ValueError(f"Library '${library_name}' not available. Choose from: {+list(LIBRARIES[.selected_library [global selected_library