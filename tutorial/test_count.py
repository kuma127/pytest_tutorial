import pytest
import tasks
from tasks import Task


def test_count_zero():
    count = tasks.count()
    assert count == 0


def test_count_single():
    new_task = Task("do something")
    tasks.add(new_task)
    count = tasks.count()
    assert count == 1


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
