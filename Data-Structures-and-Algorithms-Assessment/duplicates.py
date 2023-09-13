def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result