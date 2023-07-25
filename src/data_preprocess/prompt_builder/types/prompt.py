class Prompt:
    """
    Class which models a training sample prompt with the context of the input and the target output.
    """

    instruction: str
    input: str
    output: str

    def __init__(
        self,
        author_to_reply: str,
        input: str,
        input_author: str,
        output: str,
        other_authors,
    ):
        self.instruction = (
            f"Your name is {author_to_reply}."
            " You are in a group chat with {} of your best friends: {}.".format(
                len(other_authors), ", ".join(other_authors)
            )
            + " You talk to each other with no filter, and are encouraged to curse, say amusingly inappropriate things, or be extremely rude."
            " Everything is in good fun, so remember to joke and laugh, and be funny."
            " You will be presented with the most recent messages in the group chat."
            f" Write a response to the conversation as {author_to_reply}."
        )
        self.input = f"{input_author}: {input}"
        self.output = f"{author_to_reply}: {output}"

    def get_dict(self) -> dict:
        return {
            "instruction": self.instruction,
            "input": self.input,
            "output": self.output,
        }
