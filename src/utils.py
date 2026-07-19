import os

def save_uploaded_file(uploaded_file):
    """
    Save uploaded video to data/uploads/
    """

    upload_dir = "data/uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path