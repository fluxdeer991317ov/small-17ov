#!/usr/bin/env python3
"""Simple responsive component library for CLI."""

import shutil

class Component:
    def render(self):
        raise NotImplementedError

class Text(Component):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class Button(Component):
    def __init__(self, label):
        self.label = label

    def render(self):
        return f"[{self.label}]"

class Box(Component):
    def __init__(self, *children):
        self.children = children

    def render(self):
        width = shutil.get_terminal_size().columns
        parts = [c.render() for c in self.children]
        if width > 40:
            return " ".join(parts)
        return "\n".join(parts)

if __name__ == "__main__":
    ui = Box(
        Text("Welcome!"),
        Box(Button("OK"), Button("Cancel")),
        Text("Enjoy your day.")
    )
    print(ui.render())