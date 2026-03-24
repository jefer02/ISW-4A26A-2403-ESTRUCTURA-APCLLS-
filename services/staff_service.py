"""
services/staff_service.py — Healcia · Peciatech
Manages the on-duty medical staff directory using a native Python list.
"""

from models.doctor import Doctor


class StaffService:

    def __init__(self):
        self._staff: list[Doctor] = []

    def add_doctor(self, doctor: Doctor) -> bool:
        if any(d.doctor_id == doctor.doctor_id for d in self._staff):
            return False
        self._staff.append(doctor)
        return True

    def remove_doctor(self, doctor_id: str) -> bool:
        for i, d in enumerate(self._staff):
            if d.doctor_id == doctor_id:
                self._staff.pop(i)
                return True
        return False

    def find_doctor(self, query: str) -> list[Doctor]:
        q = query.lower()
        return [d for d in self._staff if q in d.name.lower() or q in d.specialty.lower()]

    def all_doctors(self) -> list[Doctor]:
        return list(self._staff)

    def count(self) -> int:
        return len(self._staff)
