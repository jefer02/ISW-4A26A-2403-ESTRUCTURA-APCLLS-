"""
data_structures/waiting_queue.py — Healcia · Peciatech
FIFO queue for the general waiting room (triage levels 4 and 5).
"""

from collections import deque
from typing import Any, Optional


class WaitingQueue:

    def __init__(self):
        self._items: deque = deque()

    def enqueue(self, item: Any) -> None:
        self._items.append(item)

    def dequeue(self) -> Optional[Any]:
        return self._items.popleft() if self._items else None

    def peek(self) -> Optional[Any]:
        return self._items[0] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def to_list(self) -> list:
        return list(self._items)
