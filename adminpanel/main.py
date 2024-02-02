import os
from flask import redirect, url_for
from app.web.app import create_app

app = create_app(
    config_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.yml")
)


@app.route("/")
def main():
    # return redirect("/admin", 302)
    return redirect(url_for("admin.admin_main"))


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True, host="0.0.0.0")
