import pytest
from main import Task, TaskManager

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


@pytest.fixture
def temp_manager(tmp_path):
    db_file = tmp_path / "test_tasks.txt"
    return TaskManager(str(db_file))

def test_save_and_load_tasks(temp_manager):
    task = Task(1, "Buy milk", 2)
    temp_manager.save_to_file(task)
    
    tasks = temp_manager.load_tasks()
    assert len(tasks) == 1
    assert tasks[0].description == "Buy milk"

def test_sorting_by_priority(temp_manager):
    task1 = Task(1, "Low priority", 5)
    task2 = Task(2, "High priority", 1)
    temp_manager.save_to_file(task1)
    temp_manager.save_to_file(task2)
    
    sorted_tasks = temp_manager.list_tasks_sorted(sort_by="priority")
    assert sorted_tasks[0].priority == 1
    assert sorted_tasks[1].priority == 5

def test_remove_task(temp_manager):
    task = Task(1, "To be deleted", 3)
    temp_manager.save_to_file(task)
    
    temp_manager.remove_task(1)
    tasks = temp_manager.load_tasks()
    assert len(tasks) == 0

def test_complete_task(temp_manager):
    task = Task(10, "Task to complete", 2)
    temp_manager.save_to_file(task)
    
    temp_manager.complete_task(10)
    tasks = temp_manager.load_tasks()
    assert len(tasks) == 0