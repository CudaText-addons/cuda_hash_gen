import hashlib
import binascii
from .md4 import MD4


def get_hashlib_file(filename, method):
    h = method()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def get_hashlib_string(s, method):
    return method(s.encode('us-ascii')).hexdigest()


def _digest_str(d):
    return binascii.hexlify(d).decode('us-ascii')

def get_hash_md4_string(s):
    m = MD4()
    m.update(s.encode('us-ascii'))
    return _digest_str(m.digest())

def get_hash_md4_file(filename):
    h = MD4()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return _digest_str(h.digest())


def get_hash_ripemd160_string(s):
    return hashlib.new('ripemd160', s).hexdigest()


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

    elif kind=='SHA224':
        if is_file:
            res = get_hashlib_file(data, hashlib.sha224)
        else:
            res = get_hashlib_string(data, hashlib.sha224)

    elif kind=='SHA256':
        if is_file:
            res = get_hashlib_file(data, hashlib.sha256)
        else:
            res = get_hashlib_string(data, hashlib.sha256)

    elif kind=='SHA384':
        if is_file:
            res = get_hashlib_file(data, hashlib.sha384)
        else:
            res = get_hashlib_string(data, hashlib.sha384)

    elif kind=='SHA512':
        if is_file:
            res = get_hashlib_file(data, hashlib.sha512)
        else:
            res = get_hashlib_string(data, hashlib.sha512)

    elif kind=='MD4':
        if is_file:
            res = get_hash_md4_file(data)
        else:
            res = get_hash_md4_string(data)

    return res
