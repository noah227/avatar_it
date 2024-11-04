# avatar_it

> Crop random part from image with given size.

## Usage

```python
if __name__ == "__main__": 
    from avatar_it import AvatarIt

    a = AvatarIt("./sea.jpg", 100, 100)
    a.generate().save(f"./sea.100x100.jpg")
    pass
```