import yaml

def setup_config(app, config_path: str):
    
    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)


    app.config["SQLALCHEMY_DATABASE_URI"] = raw_config.setdefault("SQLALCHEMY_DATABASE_URI")
    app.config["FLASK_ADMIN_SWATCH"] = raw_config.setdefault("FLASK_ADMIN_SWATCH")
    app.config["SECRET_KEY"] = raw_config.setdefault("SECRET_KEY")
    app.config["BABEL_DEFAULT_LOCALE"] = raw_config.setdefault("BABEL_DEFAULT_LOCALE")
