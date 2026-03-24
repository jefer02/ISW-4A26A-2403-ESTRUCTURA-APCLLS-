"""
services/patient_history_service.py — Healcia · Peciatech
Keeps each patient's intervention history using InterventionHistory (singly linked list).
"""

from data_structures.intervention_history import InterventionHistory


class PatientHistoryService:

    def __init__(self):
        self._histories: dict[str, InterventionHistory] = {}

    def add_intervention(self, patient_id: str, procedure: str) -> None:
        if patient_id not in self._histories:
            self._histories[patient_id] = InterventionHistory()
        self._histories[patient_id].append(procedure)

    def get_history(self, patient_id: str) -> list[str]:
        history = self._histories.get(patient_id)
        return history.to_list() if history else []

    def clear_history(self, patient_id: str) -> None:
        self._histories.pop(patient_id, None)

    def all_patient_ids(self) -> list[str]:
        return list(self._histories.keys())
