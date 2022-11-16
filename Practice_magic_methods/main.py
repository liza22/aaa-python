class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        rgb = (r, g, b)
        if not all(0 <= c <= 255 for c in rgb):
            raise ValueError('Incorrect input')

        self.rgb = rgb

    def __repr__(self) -> str:
        return (
            f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}'
            f'●'
            f'{self.END}{self.MOD}'
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False

        return self.rgb == other.rgb

    def __hash__(self):
        return hash(self.rgb)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('other must be the Color object')

        return Color(*map(lambda x: min(sum(x), 255), zip(self.rgb, other.rgb)))

    def __rmul__(self, other: float):
        return self.__mul__(other)

    def __mul__(self, other: float):
        if not isinstance(other, float) or not 0 <= other <= 1:
            raise ValueError('other must be the number from [0, 1]')

        cl = -256 * (1 - other)
        coef = 259 * (cl + 255) / 255 / (259 - cl)

        return Color(*map(lambda x: int(coef * (x - 128) + 128), self.rgb))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    red1 = Color(255, 0, 0)
    green = Color(0, 255, 0)
    green1 = Color(0, 255, 0)

    s = {red, red1, green, green1}
    print(s)

    print(red == red1)
    print(red == green)
    print(red + green)
    print(red + red1)

    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)

    color_list = [orange1, red, green, orange2]
    print(set(color_list))

    print(red * 0.5)
    print(0.5 * red)
