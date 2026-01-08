def read_flex_sensors():
    print("\nEnter finger states (0 = straight, 1 = bent)")
    thumb = int(input("Thumb: "))
    index = int(input("Index: "))
    middle = int(input("Middle: "))
    ring = int(input("Ring: "))
    pinky = int(input("Pinky: "))
    return [thumb, index, middle, ring, pinky]
