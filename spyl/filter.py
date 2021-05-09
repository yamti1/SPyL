from dataclasses import dataclass
from typing import Callable, Union


@dataclass
class Filter:
    arg: Union[dict, Callable]

    def __call__(self, event: dict):
        if callable(self.arg):
            return self.arg(event)

        elif isinstance(self.arg, dict):
            for field, value in self.arg:
                if event.get(field) != value:
                    return False
            return True

        else:
            raise ValueError("`Match` expects a dict or a callable")

