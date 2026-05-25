class TextProcessor:
    # Implement method overloading for format_text method
    def __init__(self) -> None:
        pass

    def format_text(self, s: str, n = None) -> str:
        if n is None:
            return s.upper()
        else:
            return s+n




# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
