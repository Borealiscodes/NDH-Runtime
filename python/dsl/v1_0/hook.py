class Hook:
    """
    NDH Hook semantic wrapper.
    Represents registration state for runtime hooks.
    """

    def __init__(self, registered: bool = False):
        self.registered = registered

    def reversible_register(self) -> None:
        self.registered = True
