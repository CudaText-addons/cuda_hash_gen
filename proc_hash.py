import hashlib


def get_file_md5(fname):
    h = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def get_file_sha1(fname):
    h = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def get_string_md5(s):
    return hashlib.md5(s.encode('ascii')).hexdigest()

def get_string_sha1(s):
    return hashlib.sha1(s.encode('ascii')).hexdigest()


def get_hash_universal(kind, data, is_file):
    res = ''

    if kind=='MD5':
        if is_file:
            res = get_file_md5(data)
        else:
            res = get_string_md5(data)

    elif kind=='SHA1':
        if is_file:
            res = get_file_sha1(data)
        else:
            res = get_string_sha1(data)

    return res
