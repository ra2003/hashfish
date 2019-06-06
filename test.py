import hashfish

with open('archive.txt') as f:
    archive = hashfish.HashFish(f)

    print(archive == archive)