# pyeventlib (version: 1.1.1)
#
# Copyright 2023. DuelitDev all rights reserved.
#
# This Library is distributed under the MIT License.


import types
import typing
import asyncio
import inspect
import functools

__all__ = ["EventHandler"]


class EventHandler:
    """
    A class that adds a callback and can be invoked with event data.
    """

    def __init__(self):
        self._functions = []

    def __iadd__(self, callback: types.FunctionType) -> typing.Any:
        """
        Add callback to queue.

        :param callback: function for the event
        :return: EventHandler
        """
        if inspect.isfunction(callback):
            self._functions.append(callback)
            return self
        raise TypeError("parameter 'callback' must be function.")

    def __sub__(self, callback: types.FunctionType) -> typing.Any:
        """
        Remove callback from queue.

        :param callback: function for the event
        :return: EventHandler
        """
        if inspect.isfunction(callback):
            if callback in self._functions:
                self._functions.remove(callback)
            return self
        raise TypeError("parameter 'callback' must be function.")

    async def __call__(self, sender: object, *args, **kwargs) -> tuple:
        """
        Call callbacks in the queue.

        :param sender: The source of the event
        :return: Result of handlers return
        """
        tasks = []
        loop = asyncio.get_running_loop()
        for function in self._functions:
            if inspect.iscoroutinefunction(function):
                tasks.append(function(sender, *args, **kwargs))
                continue
            tasks.append(loop.run_in_executor(
                None, functools.partial(function, sender, *args, **kwargs)
            ))
        return await asyncio.gather(*tasks)

    def register(self, callback: types.FunctionType) -> types.FunctionType:
        """
        Add callback to queue.

        :param callback: function for the event
        :return: function
        """
        self.__iadd__(callback)
        return callback
