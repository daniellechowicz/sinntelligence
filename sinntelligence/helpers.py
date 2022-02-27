from typing import Set


def allowed_file(filename: str) -> bool:
    allowed_extensions: Set[str] = {"png", "jpg", "jpeg", "tif", "tiff"}
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions
