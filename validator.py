"""Student scaffold. Implement rules from Lab 2; never print secret values."""
import sys

def validate(values):

    errors = []

    # TODO: APP_PORT must be an integer in 1024..65535.
    port = values.get("APP_PORT")
    if not (port.isascii() and port.isdigit()):
        errors.append("APP_PORT value must be a number.")
    elif not (1024 <= int(port) <= 65535):
        errors.append("APP_PORT value must be between 1024 and 65535.")

    # TODO: DEBUG must be false, DB_HOST and DB_PASSWORD must be nonempty.
    # Return useful errors naming keys, not secret values.
    debug = values.get("DEBUG")
    if not (debug == "false"):
        errors.append("DEBUG value must be false.")

    # raise NotImplementedError("Complete the configuration contract")

def load(path):
    values = {}
    for line in open(path, encoding="utf8"):
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    return values

if __name__ == "__main__":
    issues = validate(load(sys.argv[1]))
    print("\n".join(issues) if issues else "Configuration accepted")
    sys.exit(bool(issues))
