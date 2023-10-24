def ok(message: str, data: dict):
    return {"success": True, "message": message, "data": data}


def error(message: str):
    return {"success": False, "message": message, "data": {}}
