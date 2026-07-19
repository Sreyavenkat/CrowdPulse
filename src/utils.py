import os

def save_uploaded_file(uploaded_file):
    upload_dir = "data/uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, uploaded_file.name)

    # If the file already exists, don't save it again.
    if os.path.exists(file_path):
        return file_path

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path