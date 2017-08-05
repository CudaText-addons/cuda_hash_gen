import hashlib


def get_hashlib_file(filename, method):
    h = method()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def get_hashlib_string(s, method):
    return method(s.encode('ascii')).hexdigest()


def get_hash_universal(kind, data, is_file):
    res = ''

    if kind=='MD5':
        if is_file:
            res = get_hashlib_file(data, hashlib.md5)
        else:
            res = get_hashlib_string(data, hashlib.md5)

    elif kind=='SHA1':
        if is_file:
            res = get_hashlib_file(data, hashlib.sha1)
        else:
            res = get_hashlib_string(data, hashlib.sha1)

    elif kind=='SHA256':
        if is_file:
            res = get_hashlib_file(data, hashlib.sha256)
        else:
            res = get_hashlib_string(data, hashlib.sha256)

    elif kind=='SHA512':
        if is_file:
            res = get_hashlib_file(data, hashlib.sha512)
        else:
            res = get_hashlib_string(data, hashlib.sha512)

    return res
