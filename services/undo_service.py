"""
services/undo_service.py — Healcia · Peciatech
Records and reverts medical actions using ActionStack (LIFO).
"""

from typing import Optional
from models.action import Action
from data_structures.action_stack import ActionStack


class UndoService:

    def __init__(self):
        self._stack = ActionStack()

    def record(self, action: Action) -> None:
        self._stack.push(action)

    def undo(self) -> Optional[Action]:
        return self._stack.pop()

    def peek(self) -> Optional[Action]:
        return self._stack.peek()

    def history(self) -> list[Action]:
        return self._stack.to_list()

    def count(self) -> int:
        return self._stack.size()

    def has_actions(self) -> bool:
        return not self._stack.is_empty()
