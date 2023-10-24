from app.admin.base import CustomModelView


class TweetView(CustomModelView):
    form_columns = ["user", "content", "image_name", "image_path"]
