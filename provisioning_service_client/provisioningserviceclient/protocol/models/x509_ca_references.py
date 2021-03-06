# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class X509CAReferences(Model):
    """Primary and secondary CA references.

    :param primary:
    :type primary: str
    :param secondary:
    :type secondary: str
    """

    _attribute_map = {
        "primary": {"key": "primary", "type": "str"},
        "secondary": {"key": "secondary", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(X509CAReferences, self).__init__(**kwargs)
        self.primary = kwargs.get("primary", None)
        self.secondary = kwargs.get("secondary", None)
