import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import burnout_types
from burnout_types import BurnoutCollection


@pytest.fixture(autouse=True)
def use_temp_data_file(tmp_path, monkeypatch):
    """Use a temporary data file for each test."""
    temp_file = tmp_path / "data.json"
    temp_file.write_text("[]", encoding="utf-8")
    monkeypatch.setattr(burnout_types, "DATA_FILE", str(temp_file))


def test_add_burnout_type():
    collection = BurnoutCollection()
    initial_count = len(collection.burnout_types)

    collection.add_burnout_type(
        "Emotional Burnout",
        "Feeling emotionally depleted after prolonged stress.",
        ["Emotional numbness", "Feeling detached"],
        "Focus on nervous system regulation.",
    )

    assert len(collection.burnout_types) == initial_count + 1
    burnout_type = collection.find_burnout_type_by_title("Emotional Burnout")
    assert burnout_type is not None
    assert burnout_type.reviewed is False


def test_mark_burnout_type_as_reviewed():
    collection = BurnoutCollection()
    collection.add_burnout_type(
        "Mental Burnout",
        "Feeling mentally overloaded.",
        ["Brain fog"],
        "Use brain retraining strategies.",
    )

    result = collection.mark_as_reviewed("Mental Burnout")

    assert result is True
    burnout_type = collection.find_burnout_type_by_title("Mental Burnout")
    assert burnout_type.reviewed is True


def test_mark_burnout_type_as_reviewed_invalid():
    collection = BurnoutCollection()

    result = collection.mark_as_reviewed("Missing Burnout Type")

    assert result is False


def test_remove_burnout_type():
    collection = BurnoutCollection()
    collection.add_burnout_type(
        "Social Burnout",
        "Feeling drained by social obligations.",
        ["Avoiding gatherings"],
        "Set clear boundaries.",
    )

    result = collection.remove_burnout_type("Social Burnout")

    assert result is True
    burnout_type = collection.find_burnout_type_by_title("Social Burnout")
    assert burnout_type is None


def test_remove_burnout_type_invalid():
    collection = BurnoutCollection()

    result = collection.remove_burnout_type("Missing Burnout Type")

    assert result is False


def test_find_by_healing_keyword():
    collection = BurnoutCollection()
    collection.add_burnout_type(
        "Purpose-Driven Burnout",
        "Feeling stuck even though the work matters to you.",
        ["Hopelessness", "Dissatisfaction"],
        "Reconnect with your purpose and reduce stress around your goals.",
    )

    matches = collection.find_by_healing_keyword("purpose")

    assert len(matches) == 1
    assert matches[0].title == "Purpose-Driven Burnout"