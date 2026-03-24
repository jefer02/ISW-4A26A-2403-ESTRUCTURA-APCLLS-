"""
services/bed_service.py — Healcia · Peciatech
Manages ICU bed assignment and release using BedArray.
"""

from typing import Optional
from models.patient import Patient
from data_structures.bed_array import BedArray


class BedService:

    def __init__(self, capacity: int = 15):
        self._beds = BedArray(capacity)

    def admit_to_bed(self, index: int, patient: Patient) -> bool:
        return self._beds.assign(index, patient)

    def discharge_from_bed(self, index: int) -> Optional[Patient]:
        return self._beds.release(index)

    def get_bed(self, index: int) -> Optional[Patient]:
        return self._beds.get(index)

    def is_free(self, index: int) -> bool:
        return self._beds.is_free(index)

    def all_beds(self) -> list:
        return self._beds.all_beds()

    def first_free_index(self) -> Optional[int]:
        return self._beds.first_free_index()

    def free_count(self) -> int:
        return self._beds.free_count()

    def occupied_count(self) -> int:
        return self._beds.occupied_count()

    def capacity(self) -> int:
        return self._beds.capacity
