import pytest
import tasks
from tasks.api import UninitializedDatabase


def test_count_raises():
    with pytest.raises(UninitializedDatabase):
        tasks.count()


def test_unique_id_raises():
    with pytest.raises(UninitializedDatabase):
        tasks.unique_id()
