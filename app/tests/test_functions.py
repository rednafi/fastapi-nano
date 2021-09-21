from app.apis.api_a.mainmod import main_func as main_func_a
from app.apis.api_b.mainmod import main_func as main_func_b


def mock_randint(*args, **kwargs):
    """A mock version of 'random.randint' that always returns 42."""
    return 42


def test_func_main_a(monkeypatch) -> None:
    monkeypatch.setattr(
        "app.apis.api_a.submod.random.randint",
        mock_randint,
    )
    seed = 420
    result = main_func_a(seed)
    assert isinstance(result, dict) is True
    assert result.get("seed") == seed
    assert result.get("random_first") == mock_randint()
    assert result.get("random_second") == mock_randint()


def test_func_main_b(monkeypatch) -> None:
    monkeypatch.setattr(
        "app.apis.api_a.submod.random.randint",
        mock_randint,
    )
    seed = 500
    result = main_func_b(seed)
    assert isinstance(result, dict) is True
    assert result.get("seed") == seed
    assert result.get("random_first") == mock_randint()
    assert result.get("random_second") == mock_randint()
