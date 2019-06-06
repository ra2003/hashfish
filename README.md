# hashfish


This library allows you to compare files.

### Installation

```
~ pipenv install hashfish
```


### Basic usage

```python

import hashfish


with open('file.zip') as f:
    file = hashfish.HashFish(f)

>>> archive.md5
db79bedb48340fe39d025a81080f40c4

>>> archive.sha1
aa00572321e92840e11daf9cdcad1725c53ed15c

>>> archive.sha224
69e660ff245a33be40a215bc4aaf6027df056875c925d8f7bcc5ff00

>>> archive.sha256
13feaac02381e66ec367c9b1ab61576fccd637807cba1c56c16ef6a7c1344053

>>> archive.sha384
405e6d56cea9b189488b0b3a647a2503d79fafad3fd7c1db0bcbe50f03aa77a799f8c29efc098212a964b537e83b3867

>>> archive.sha512
e766940daced1eb1bb07377d5fbb2ee0df7eb6294cbdeb5a25494c0d095cdd22ccb9977f11a4901549d8ed847ef10bb225f68e03214357a458c565500b17a671
```

You can also compare files:

```python
>>> arcive == archive
True

>>> arcive != archive
False
```