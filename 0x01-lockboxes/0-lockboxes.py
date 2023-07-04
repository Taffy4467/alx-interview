def canUnlockAll(boxes):
    if not boxes:
        return False

    # Set to keep track of opened boxes
    opened_boxes = set()
    opened_boxes.add(0)  # Start with the first box (boxes[0])

    stack = [0]  # Stack to perform DFS

    while stack:
        current_box = stack.pop()

        # Check all the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and it has not been opened yet
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)

    # If all boxes have been opened
    return len(opened_boxes) == len(boxes)

