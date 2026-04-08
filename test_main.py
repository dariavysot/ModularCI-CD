import pytest
from main import Task

@pytest.fixture
def sample_task():
    return Task(1, "Test Task", 3, "2026-04-08 12:00:00")

def test_task_initialization(sample_task):
    assert sample_task.task_id == 1
    assert sample_task.description == "Test Task"
    assert sample_task.priority == 3
    assert sample_task.is_done is False

def test_task_to_line(sample_task):
    expected_line = "1|Test Task|3|2026-04-08 12:00:00|False\n"
    assert sample_task.to_line() == expected_line