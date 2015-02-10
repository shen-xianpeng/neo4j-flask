from blog import app
import os

app.secret_key = os.urandom(24)
port = int(os.environ.get('PORT', 6000))
app.run(host='0.0.0.0', port=9998)
