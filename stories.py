"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, ident, title, words, text):
        """Create story with words and template text."""
        self.ident = ident
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


basic = Story(
    "basic",
    "Basic Story",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

action = Story(
    "action",
    "Action Story",
    ["place","verb","adjective","name"],
    """A long time ago in {place}, there lived a person named {name}.
    It was here that {name} was a secret spy.  They were trained to {verb} in a very
    {adjective} manner."""
)

silly = Story(
        "silly",
        "Silly Story",
        ["name", "adjective", "food", "noun","verb"],
        """{name} was a silly person.  They liked to eat {adjective} {food}.  Their favorite
        place to eat was on top of {noun}.  They would eat it while {verb}!  How silly.""")

stories = {s.ident: s for s in [basic, action, silly]}