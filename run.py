'''ENTRY POINT OF THE APP'''
# global builtin modules
import os

# local imports
from app import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)


@app.route('/')
def index():
    return "Welcome"

if __name__ == "__main__":
    app.run(debug=True)
