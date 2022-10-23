class EmojiMixin:
    ICON = {'grass': '🌿',
            'fire': '🔥',
            'water': '🌊',
            'electric': '⚡'}

    def __str__(self) -> str:
        text = self.__repr__()
        for cat, emoji in self.ICON.items():
            replaced = text.replace(cat, emoji)
            if replaced != text:
                return replaced
        return text


class Pokemon(EmojiMixin):
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    def __repr__(self) -> str:
        return f"{self.name}/{self.category}"


if __name__ == '__main__':
    pikachu = Pokemon(name='Pikachu', category='electric')
    print(pikachu)
