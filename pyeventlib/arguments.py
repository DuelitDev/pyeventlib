# pyeventlib (version: 1.1.1)
#
# Copyright 2023. DuelitDev all rights reserved.
#
# This Library is distributed under the MIT License.


import typing

__all__ = ["EventArgs"]


def _strict_setattr_(self, key: str, value: typing.Any):
    if key not in dir(self):
        raise AttributeError(f"Attribute '{key}' does not exist.")
    if not isinstance(value, type(getattr(self, key))):
        raise TypeError(f"Only type '{type(getattr(self, key)).__name__}' "
                        f"can be assigned to attribute '{key}'.")
    object.__setattr__(self, key, value)


class EventArgs:
    """
    A class that contains event data to send to the callback.
    """

    @staticmethod
    def create(name: str, kwargs: typing.Dict[str, typing.Any],
               strict: bool = True) -> type:
        mcs = type(name, (EventArgs,), kwargs)
        if strict:
            mcs.__setattr__ = _strict_setattr_
        return mcs
