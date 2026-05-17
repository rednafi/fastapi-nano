from unittest.mock import MagicMock, patch

import pytest

from svc.apis.api_a import mainmod as mainmod_a
from svc.apis.api_b import mainmod as mainmod_b
from svc.apis.schemas import RandomNumbers


@pytest.fixture(scope="module")
def mock_randint() -> MagicMock:
    """Mock random.randint function."""

    with patch("random.randint", return_value=42, auto=True) as m:
        yield m


@pytest.mark.parametrize(
    ("seed", "output"),
    [
        pytest.param(1, 42, id="seed-1"),
        pytest.param(100, 42, id="seed-100"),
        pytest.param(589, 42, id="seed-589"),
        pytest.param(444, 42, id="seed-444"),
    ],
)
def test_func_main_a(mock_randint: MagicMock, seed: int, output: int) -> None:
    # Act.
    result = mainmod_a.main_func(seed)

    # Assert.
    assert isinstance(result, RandomNumbers)
    assert result.seed == seed
    assert result.random_first == output
    assert result.random_second == output

    mock_randint.assert_called_with(0, seed)


@pytest.mark.parametrize(
    ("seed", "output"),
    [
        pytest.param(1, 42, id="seed-1"),
        pytest.param(100, 42, id="seed-100"),
        pytest.param(589, 42, id="seed-589"),
        pytest.param(444, 42, id="seed-444"),
    ],
)
def test_func_main_b(mock_randint: MagicMock, seed: int, output: int) -> None:
    # Act.
    result = mainmod_b.main_func(seed)

    # Assert.
    assert isinstance(result, RandomNumbers)
    assert result.seed == seed
    assert result.random_first == output
    assert result.random_second == output

    mock_randint.assert_called_with(0, seed)
