import hashlib


def get_hashlib_file(filename, name):
    h = hashlib.new(name)
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def get_hashlib_string(s, name):
    return hashlib.new(name, s.encode('us-ascii')).hexdigest()


def get_hash_universal(kind, data, is_file):

    kind = kind.lower()
    if is_file:
        res = get_hashlib_file(data, kind)
    else:
        res = get_hashlib_string(data, kind)
    return res
