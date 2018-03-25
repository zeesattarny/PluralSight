def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii
    return wrap


def norhtern_city():
    return 'Tromso'