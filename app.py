from flask import Flask
from documented_endpoints import blueprint as documented_endpoint
from basic_endpoints import blueprint as basic_endpoint


app =Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(basic_endpoint)
app.register_blueprint(documented_endpoint)



if __name__ == "__main__":
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=5000, debug=True)