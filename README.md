# pyeventlib
pyeventlib library is used to handle event in a simple way.  
## Install
`pip install pyeventlib`  
## Documentation
[pyeventlib wiki](https://github.com/DuelitDev/pyeventlib/wiki)  
## Example
```python
import asyncio
from pyeventlib import *


event = EventHandler()


async def main():
    await event(__name__)
    

@event.register
def event_a(sender, e):
    print("Event A")


@event.register
async def event_b(sender, e):
    print("Event B")


def event_c(sender, e):
    print("Event C")
event += event_c


asyncio.run(main())
```   
## Copyright
Copyright 2022. Kim Jae-yun all rights reserved.  
## License
[MIT License](https://github.com/DuelitDev/pyeventlib/blob/main/LICENSE) 