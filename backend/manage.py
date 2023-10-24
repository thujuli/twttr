import os
from app import create_app

if __name__ == "__main__":
    app = create_app()
    env = os.environ.get("FLASK_ENV", "dev")

    if env == "prod":
        app.run(host="0.0.0.0", port=5000)
    else:
        app.run(host="0.0.0.0", port=5000, debug=True)
