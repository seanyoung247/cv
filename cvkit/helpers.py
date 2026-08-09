
import re


MISSING = object()
TOKEN_PATTERN = re.compile(r"\{([^{}]+)\}")


def resolve_value(path, *sources):
    keys = path.split(".")

    for source in sources:
        value = source

        for key in keys:
            if not isinstance(value, dict) or key not in value:
                value = MISSING
                break

            value = value[key]

        if value is not MISSING:
            return value

    return None


def register_helpers(app):


    @app.template_global()
    def is_visible(item, profile):
        return profile not in item.get("exclude", [])


    @app.template_global()
    def parse_text(value, *sources):
        if not isinstance(value, str):
            return value

        def replace(match):
            path = match.group(1)
            resolved = resolve_value(path, *sources)

            return "" if resolved is None else str(resolved)

        return TOKEN_PATTERN.sub(replace, value)

