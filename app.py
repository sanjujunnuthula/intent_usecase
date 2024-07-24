import traceback
from flask import request
from init import app
from responsors import common_responsor


@app.errorhandler(500)
def handle_500(ex):
    traceback.print_exc()
    return common_responsor.get_message('Something went wrong. Please contact server administrator.'), 500

#
# @app.route("/intent/sample-request", methods=['get'])
# def fetch_sample_data():
#     return {"message": "inside sample request"}
#
#
#
# if __name__ == "__main__":
#     app.run(port=6000)