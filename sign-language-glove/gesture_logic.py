def recognize_gesture(flex_data):
    if flex_data == [0, 0, 0, 0, 0]:
        return "HELLO"
    elif flex_data == [1, 0, 0, 0, 0]:
        return "YES"
    elif flex_data == [1, 1, 1, 1, 1]:
        return "NO"
    else:
        return "UNKNOWN"
