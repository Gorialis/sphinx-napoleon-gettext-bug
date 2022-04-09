# -*- coding: utf-8 -*-

def documented_function(small: bool = False):
    """
    Use this when you want to look at a picture of a duck.

    Parameters
    -----------
    small: :class:`bool`
        Whether the duck should be small or not.

        .. warning::
            This duck is very small.

    Returns
    --------
    str
        A nice `picture of a duck`__.

        .. _picture_of_a_duck: https://upload.wikimedia.org/wikipedia/commons/5/51/Mandarin.duck.arp.jpg
        __ picture_of_a_duck_

    """

    if small:
        return "https://c.pxhere.com/photos/5c/45/animal_bird_cute_duck_duckling_feathers_little_small-991952.jpg!d"

    return "https://upload.wikimedia.org/wikipedia/commons/5/51/Mandarin.duck.arp.jpg"
