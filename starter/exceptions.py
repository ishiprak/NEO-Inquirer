class UnsupportedFeature(Exception):
    """
    Custom exception for an unimplemented feature
    """

    # All exceptions and bugs have been resolved internally and through internal implementations leaving the scope of this file empty.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
