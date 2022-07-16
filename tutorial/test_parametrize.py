import pytest
import tasks
from tasks import Task


def equivalent(t1, t2):
    """Check two tasks for equivalence."""
    # Compare everything but the id field
    return (
        (t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done)
    )


@pytest.mark.parametrize(
    ("summary", "owner", "done"),
    [
        ("sleep", None, False),
        ("wake", "brian", False),
        ("breathe", "BRIAN", True),
        ("eat eggs", "BrIaN", False),
    ],
)
def test_add_3(summary, owner, done):
    """Demonstrate parametrize with multiple parameters."""
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), "tiny")

    yield  # this is where the testing happens

    # Teardown : stop db
    tasks.stop_tasks_db()
