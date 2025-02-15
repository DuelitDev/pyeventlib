# ⚠️ Deprecated Notice

The `pyeventlib` library is now deprecated and no longer maintained.  

---

**Alternatives**:
- [pyee](https://pypi.org/project/pyee/)
- [blinker](https://pypi.org/project/blinker/)
- [PyDispatcher](https://pypi.org/project/PyDispatcher/)


# pyeventlib
pyeventlib library is used to handle event in a simple way.  
## Install
`pip install pyeventlib`  
## Examples
```python
import asyncio
from pyeventlib import *


class CloseEventArgs(EventArgs):
    def __init__(self):
        self.accept = False
# other option
# CloseEventArgs = EventArgs.create(
#     "CloseEventArgs", 
#     {"accept": False})


event1 = EventHandler()
event2 = EventHandler()


async def main():
    await event1(__name__)
    args = CloseEventArgs()
    await event2(__name__, args)
    print(args.accept)  # True
    

@event1.register
def event_a(sender):
    print("Event A Sender: " + sender)


async def event_b(sender):
    print("Event C Sender: " + sender)
event1 += event_b


@event2.register
def close_event(sender, e):
    e.accept = True


asyncio.run(main())
```   
## Copyright
Copyright 2023. DuelitDev all rights reserved.  
## License
[MIT License](https://github.com/DuelitDev/pyeventlib/blob/main/LICENSE) 
