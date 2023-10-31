def ok(message: str, data: dict):
    return {"success": True, "message": message, "data": data}


def error(message: str):
    return {"success": False, "message": message, "data": {}}


def pagination(
    message: str,
    data: dict,
    current_page: int,
    total_pages: int,
    total_items: int,
):
    return {
        "success": True,
        "message": message,
        "data": data,
        "current_page": current_page,
        "total_pages": total_pages,
        "total_items": total_items,
    }
