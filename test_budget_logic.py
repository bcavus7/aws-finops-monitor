import pytest
from budget_logic import analyze_budget

def test_no_spending():
    assert analyze_budget(5, 0) == (5, 0, False)

def test_budget_warning():
    assert analyze_budget(5, 4.5) == (0.5, 90, True)

def test_warning_at_threshold():
    assert analyze_budget(5, 4) == (1, 80, True)

def test_invalid_budget():
    with pytest.raises(ValueError):
        analyze_budget(0, 0)
