from contextlib import contextmanager
from urllib.parse import urlparse
import pysftp


@contextmanager
def open_sftp(url, mode="r"):
    # Parse url into username, password, host, port, path
    # using the proper ftp URL syntax of
    # sftp://username:password@host:port/path/to/file.txt
    try:
        # Parsing url
        split_url = urlparse(url)
        if not split_url.scheme == "sftp":
            raise ValueError("Invalid URL: Invalid scheme '{}'".format(split_url.scheme))
        if not split_url.hostname:
            raise ValueError("Invalid URL: No hostname")
        if not split_url.path:
            raise ValueError("Invalid URL: No file path")
        path_split = split_url.path.split("/")
        path_split.pop(0)
        if len(path_split) < 1:
            raise ValueError("Invalid URL: Invalid path '{}'".format(split_url.path))
        file_name = path_split.pop()
        file_path = path_split
        if not file_name:
            raise ValueError("Invalid URL: No file name")
        cinfo = {
            "host": split_url.hostname,
            "username": split_url.username,
            "password": split_url.password,
        }
        if split_url.port:
            cinfo["port"] = split_url.port
        else:
            cinfo["port"] = 22

        # Connect to host. Sometimes it takes a couple tries... =(
        sftp = pysftp.Connection(**cinfo)
        if not sftp:
            raise TimeoutError()

        # Get file object
        for directory in file_path:
            # Skip blanks (e.g. caused by '//')
            if not directory:
                sftp.cwd("/")
            try:
                sftp.chdir(directory)
            except IOError as exc:
                raise IOError(
                    "Could not navigate to path '{}': {}".format("/".join(file_path), exc)
                )

        try:
            file_obj = sftp.open(file_name, mode=mode)
        except IOError as exc:
            raise IOError(
                "Could not open file '{}' in path '{}': {}".format(file_name, file_path, exc)
            )
        yield file_obj
    finally:
        sftp.close()
