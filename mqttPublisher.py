from flask import Flask, request
import paho.mqtt.publish as publish

app = Flask(__name__)
mqtt_broker = 'localhost'
mqtt_topic = 'my_topic'

@app.route('/publish', methods=['POST'])
def publish_message():
    text = request.form['text']
    # Add MQTT publishing code here
    return text

if __name__ == '__main__':
    app.run(debug=True)
    


