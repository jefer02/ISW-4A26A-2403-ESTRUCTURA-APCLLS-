"""
services/waiting_room_service.py — Healcia · Peciatech
Manages the general waiting queue for triage levels 4 and 5 using WaitingQueue.
"""

from typing import Optional
from models.patient import Patient
from data_structures.waiting_queue import WaitingQueue


class WaitingRoomService:

    def __init__(self):
        self._queue = WaitingQueue()

    def add_patient(self, patient: Patient) -> None:
        self._queue.enqueue(patient)

    def call_next_patient(self) -> Optional[Patient]:
        return self._queue.dequeue()

    def peek_next(self) -> Optional[Patient]:
        return self._queue.peek()

    def queue_list(self) -> list[Patient]:
        return self._queue.to_list()

    def count(self) -> int:
        return self._queue.size()

    def is_empty(self) -> bool:
        return self._queue.is_empty()
