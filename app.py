import traceback
from flask import Flask
from common import common_responsor
from init import app
from modules.intent import intent_routes
from modules.serviceOrder  import service_routes

app = Flask(__name__)
app.register_blueprint(intent_routes.intent)
app.register_blueprint(service_routes.service)


@app.errorhandler(500)
def handle_500(ex):
    traceback.print_exc()
    return common_responsor.get_message('Something went wrong. Please contact server administrator.'), 500




if __name__ == "__main__":
    app.run(port=1971)