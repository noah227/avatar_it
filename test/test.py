if __name__ == '__main__':
    from avatar_it import AvatarIt
    import os

    if not os.path.exists("./out"):
        os.mkdir("./out")
    a = AvatarIt("./sea.jpg", 100, 100)
    for i in range(10):
        a.generate().save(f"./out/sea.100.{i}.jpg")
        pass
    pass
