"""RUN APP FROM HERE"""
from gpbapp import app

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
