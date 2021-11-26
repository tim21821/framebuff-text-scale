class LengthError(Exception):
    """An Exception for the :class:`Character` class. It is raised when the input isn't of length 1."""

    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if self.message:
            return "LengthError, {}".format(self.message)
        else:
            return "LengthError"


class Character:
    """This is a class representation of a character, that can be displayed on a LCD screen. It's main purpose is to provide a way to scale characters, that is not given by the :class:`framebuf.Framebuffer` class.

    :param char: A string or integer with length 1, that will be represented by :class:`character`
    :type char: Union[str, int]
    :param size: The size of each pixel of the character. 1 means each character pixel will be 1 pixel on the screen, giving an 8x8 character. Defaults to 1
    :type size: int, optional
    :raises LengthError: The length of char isn't 1
    """

    # TODO: get all the offsets
    OFFSETS = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
        "L": [],
        "M": [],
        "N": [],
        "O": [],
        "P": [],
        "Q": [],
        "R": [],
        "S": [],
        "T": [],
        "U": [],
        "V": [],
        "W": [],
        "X": [],
        "Y": [],
        "Z": [],
        "a": [],
        "b": [],
        "c": [],
        "d": [],
        "e": [],
        "f": [],
        "g": [],
        "h": [],
        "i": [],
        "j": [],
        "k": [],
        "l": [],
        "m": [],
        "n": [],
        "o": [],
        "p": [],
        "q": [],
        "r": [],
        "s": [],
        "t": [],
        "u": [],
        "v": [],
        "w": [],
        "x": [],
        "y": [],
        "z": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],
        "0": [],
        ".": [],
        ",": [],
        ":": [],
        "°": [],
    }

    def __init__(self, char, size=1):
        """Constructor method"""
        if len(str(char)) != 1:
            raise LengthError(
                "Characters must have length 1. Your input has length {}".format(
                    len(str(char))
                )
            )
        if size <= 0:
            raise ValueError("size has to be a positive integer.")
        self.char = str(char)
        self.size = size

    def get_pixel_positions(self, x=0, y=0):
        """Returns a list of xy-positions, where pixels on all of the positions form the character with size 1. Can be shifted by x, y.

        :param x: The right shift of all the pixels, defaults to 0
        :type x: int, optional
        :param y: The down shift of all the pixels, defaults to 0
        :type y: int, optional
        :return: A list of xy-positions representing the pixel locations. Each position will be a tuple (x, y)
        :rtype: list
        """
        positions = [
            (position[0] + x, position[1] + y) for position in OFFSETS[self.char]
        ]
        return positions

    def draw(self, screen, x, y, color=0x0000):
        """Draws the character on the screen in its correct size. The top left corner of the character is x, y. The character will be displayed in the given color.

        :param screen: The screen to be drawn on
        :type screen: :class:`framebuff.Framebuffer`
        :param x: The x-position of the top left corner of the character
        :type x: int
        :param y: The y-position of the top left corner of the character
        :type y: int
        :param color: The color the character will be displayed as. Defaults to 0x0000
        :type color: int, optional
        """
        pixel_positions = self.get_pixel_positions()
        for position in pixel_positions:
            screen.fill_rect(
                x + pixel_positions[0] * self.size,
                y + pixel_positions[1] * self.size,
                self.size,
                self.size,
                color,
            )

    def __str__(self):
        return self.char


class Text:
    def __init__(self, text, size=1):
        if size <= 0:
            raise ValueError("size has to be a positive integer.")
        self.text = text
        self.size = size

    def draw(self, screen, x, y, color=0x000):
        # TODO implement text drawing
        pass

    def __str__(self):
        return self.text
