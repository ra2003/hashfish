# -*- coding: utf-8 -*-


import hashlib


class HashFish(object):

    def __init__(self, file) -> None:
        self.data = file.read().encode('utf-8')

    def _hash(self, callback) -> str:
        return callback(self.data).hexdigest()

    @property
    def md5(self) -> str:
        return self._hash(hashlib.md5)

    @property
    def sha1(self) -> str:
        return self._hash(hashlib.sha1)

    @property
    def sha224(self) -> str:
        return self._hash(hashlib.sha224)

    @property
    def sha256(self) -> str:
        return self._hash(hashlib.sha256)

    @property
    def sha384(self) -> str:
        return self._hash(hashlib.sha384)

    @property
    def sha512(self) -> str:
        return self._hash(hashlib.sha512)

    def __eq__(self, other) -> bool:
        if not isinstance(other, HashFish):
            raise TypeError('Other must be instance of <HashFish>')
        return self.sha1 == other.sha1

    def __str__(self):
        return '{}'.format(self.sha1)
