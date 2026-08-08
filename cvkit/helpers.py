

def register_helpers(app):

    @app.template_global()
    def is_visible(item, profile):
        return profile not in item.get("exclude", [])
