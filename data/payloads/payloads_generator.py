import uuid


def new_task_payload() -> dict:
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"

    return {
        'content': content,
        'user_id': user_id,
        'is_done': False
    }


def update_task_payload(task_id) -> dict:
    content = f"updated_content_{uuid.uuid4().hex}"
    is_done = True

    return {
        'task_id': task_id,
        'content': content,
        'is_done': is_done
    }
