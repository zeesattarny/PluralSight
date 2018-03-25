"""Module for demonstrating generator execution."""

def take(count, iterable):
    """Take items from front of an Iterable

    Args:
        count: The maximum number of items to retrieve
        iterable: the source yield

    Yields:
        At most counts items for iterable."""
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    """Return unique items by eliminating duplicates

    Iterable: The source series

    Yields: Unique elements in order from Iterable"""
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_take():
    items = [2, 4, 6, 8]
    for item in take(3, items):
        print(item)

def run_distinct():
    items = [5, 5, 7, 7, 7, 6, 6]
    for item in distinct(items):
        print(item)

def run_pipeline():
    items = [3, 6, 6, 2,]

if __name__ == '__main__':
    #run_take()
     run_distinct()