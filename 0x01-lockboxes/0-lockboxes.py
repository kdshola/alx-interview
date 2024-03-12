#!/usr/bin/python3
""" module for canUnlockAll function """


def canUnlockAll(boxes):
    """ Determines if a given list of boxes can be unlocked """
    length = len(boxes)
    unlocked = [0]
    position = 0
    for box in boxes:
        boxlength = len(box)
        if boxlength != 0:
            for key in box:
                if key not in unlocked and key < length and key != position:
                    unlocked.append(key)
        position += 1
    return len(unlocked) == length
