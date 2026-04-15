import json
from dataclasses import asdict, dataclass
from typing import List, Optional

DATA_FILE = "data.json"


@dataclass
class BurnoutType:
    title: str
    what_it_looks_like: str
    signs: List[str]
    healing_steps: str
    reviewed: bool = False


class BurnoutCollection:
    def __init__(self):
        self.burnout_types: List[BurnoutType] = []
        self.load_burnout_types()

    def load_burnout_types(self):
        """Load burnout types from the JSON file if it exists."""
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.burnout_types = [BurnoutType(**item) for item in data]
        except FileNotFoundError:
            self.burnout_types = []
        except json.JSONDecodeError:
            print("Warning: data.json is corrupted. Starting with an empty guide.")
            self.burnout_types = []

    def save_burnout_types(self):
        """Save the current burnout guide to JSON."""
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([asdict(item) for item in self.burnout_types], file, indent=2)

    def add_burnout_type(
        self,
        title: str,
        what_it_looks_like: str,
        signs: List[str],
        healing_steps: str,
    ) -> BurnoutType:
        if not title:
            raise ValueError("Title is required.")
        if not what_it_looks_like:
            raise ValueError("A description is required.")
        if not signs:
            raise ValueError("At least one sign is required.")
        if not healing_steps:
            raise ValueError("Healing steps are required.")

        burnout_type = BurnoutType(
            title=title,
            what_it_looks_like=what_it_looks_like,
            signs=signs,
            healing_steps=healing_steps,
        )
        self.burnout_types.append(burnout_type)
        self.save_burnout_types()
        return burnout_type

    def list_burnout_types(self) -> List[BurnoutType]:
        return self.burnout_types

    def find_burnout_type_by_title(self, title: str) -> Optional[BurnoutType]:
        for burnout_type in self.burnout_types:
            if burnout_type.title.lower() == title.lower():
                return burnout_type
        return None

    def mark_as_reviewed(self, title: str) -> bool:
        burnout_type = self.find_burnout_type_by_title(title)
        if burnout_type:
            burnout_type.reviewed = True
            self.save_burnout_types()
            return True
        return False

    def remove_burnout_type(self, title: str) -> bool:
        burnout_type = self.find_burnout_type_by_title(title)
        if burnout_type:
            self.burnout_types.remove(burnout_type)
            self.save_burnout_types()
            return True
        return False

    def find_by_healing_keyword(self, keyword: str) -> List[BurnoutType]:
        normalized_keyword = keyword.lower().strip()
        return [
            burnout_type
            for burnout_type in self.burnout_types
            if normalized_keyword in burnout_type.healing_steps.lower()
        ]