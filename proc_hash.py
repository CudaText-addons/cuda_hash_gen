import hashlib


def get_file_md5(fname):
    h = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def get_string_md5(s):
    return hashlib.md5(s.encode('ascii')).hexdigest()

