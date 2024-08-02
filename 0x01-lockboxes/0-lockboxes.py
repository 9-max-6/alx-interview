#!/usr/bin/python3
"""A module that solves a problem about lockboxes.
"""


def canUnlockAll(boxes):
    """Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    """
    n = len(boxes)
    visible_boxes = set([0])
    invisible_boxes = set(boxes[0]).difference(set([0]))
    while len(invisible_boxes) > 0:
        box_index = invisible_boxes.pop()
        if not box_index or box_index >= n or box_index < 0:
            continue
        if box_index not in visible_boxes:
            invisible_boxes = invisible_boxes.union(boxes[box_index])
            visible_boxes.add(box_index)
    return n == len(visible_boxes)
