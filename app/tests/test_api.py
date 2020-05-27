import pytest

from app.api_a.mainmod import func_main as func_main_a
from app.api_b.mainmod import func_main as func_main_b


def test_func_main_a():
    seed = 420
    result = func_main_a(seed)
    assert isinstance(result, dict) is True
    assert result.get("seed") == seed


def test_func_main_b():
    seed = 500
    result = func_main_b(seed)
    assert isinstance(result, dict) is True
    assert result.get("seed") == seed
