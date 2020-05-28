def __iter__(self):
    return self

def __next__(self):
    global index
    if index >= len(App_List):
        raise StopIteration
        index = 0
    index += 1
    return App_List[index]  # Next Value#
