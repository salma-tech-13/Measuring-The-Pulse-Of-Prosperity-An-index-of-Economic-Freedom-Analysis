from flask import Flask, render_template, jsonify, request
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
app = Flask(__name__)
# Basic Page Routes
@app.route('/')
def index():
return render_template('index.html')
@app.route('/analytics')
def analytics():
return render_template('analytics.html')
@app.route('/methodology')
def methodology():
return render_template('methodology.html')
# Actual ML Logic Implementation
@app.route('/api/predict', methods=['POST'])
def predict():
try:
# Expecting JSON data with country metrics
input_data = request.json
df = pd.DataFrame(input_data)
features = ['Trade Freedom', 'Financial Freedom', 'Monetary Freedom']
target = 'GDP_Growth'
# Simple Model training
model = RandomForestRegressor(n_estimators=100)
model.fit(df[features], df[target])
importance = dict(zip(features, model.feature_importances_.tolist()))
return jsonify({
"status": "success",
"feature_importance": importance
})
except Exception as e:
return jsonify({"status": "error", "message": str(e)})
if __name__ == '__main__':
app.run(debug=True, port=5000)
