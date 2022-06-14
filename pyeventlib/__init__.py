# pyeventlib (version: 1.0.0)
#
# Copyright 2022. Kim Jae-yun all rights reserved.
#
# This Library is distributed under the MIT License.
# -----------------------------------------------------------------------------
# MIT License
#
# Copyright (c) 2022 DuelitDev
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import types
import typing
import asyncio
import inspect

__all__ = ["EventHandler"]


class EventHandler:
    """
    Represents the method that will handle an event that has no event data.
    """

    def __init__(self) -> None:
        """
        Represents the method that will handle an event that has no event data.
        """
        self._functions = []

    def __add__(self, function: types.FunctionType) -> typing.Any:
        """
        Add function to queue.

        :param function: function for the event.
        :return: EventHandler
        """
        if inspect.isfunction(function):
            self._functions.append(function)
            return self
        raise TypeError("parameter 'function' must be function.")

    def __sub__(self, function: types.FunctionType):
        """
        Remove function from queue.

        :param function: function for the event.
        :return: EventHandler
        """
        if inspect.isfunction(function):
            if function in self._functions:
                self._functions.remove(function)
            return self
        raise TypeError("parameter 'function' must be function.")

    def register(self, function: types.FunctionType) -> types.FunctionType:
        """
        Add function to queue.

        :param function: function for the event.
        :return: function
        """
        self.__add__(function)
        return function

    def __call__(self, sender: object, *args, **kwargs) -> asyncio.Future:
        """
        Call functions in the queue.

        :param sender: The source of the event.
        :return: Future
        """
        tasks = []
        for function in self._functions:
            if inspect.iscoroutinefunction(function):
                tasks.append(function(sender, *args, **kwargs))
                continue
            function(sender, *args, **kwargs)
        return asyncio.gather(*tasks)
