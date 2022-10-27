__version__ = "0.0.1"

#!/usr/bin/env python

from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer, Input

from typing import Any


class PrincetonApp(App[Any]):
    """Displays the Princeton colors."""

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Input(placeholder="Name")
        for color in ["black", "orange"] * 2:
            stripe = Static()
            stripe.styles.height = "1fr"
            stripe.styles.background = color
            yield stripe
        yield Footer()


def main() -> None:
    PrincetonApp().run()


if __name__ == "__main__":
    main()
