def ok(message: str, data: dict):
    return {"success": True, "message": message, "data": data}


def error(message: str):
    return {"success": False, "message": message, "data": {}}


def pagination(message: str, data: dict, total_pages: int):
    return {
        "success": True,
        "message": message,
        "data": data,
        "total_pages": total_pages,
    }
