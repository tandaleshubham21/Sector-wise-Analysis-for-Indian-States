"""REST API for IT Infrastructure Monitoring"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    }), 200

@app.route('/api/metrics/current', methods=['GET'])
def get_current_metrics():
    """Get current system metrics"""
    return jsonify({
        'success': True,
        'data': {
            'cpu_usage': 45.2,
            'memory_usage': 62.8,
            'disk_usage': 78.5,
            'network_in': 125.5,
            'network_out': 89.3
        },
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    """Get active alerts"""
    return jsonify({
        'success': True,
        'alerts': [
            {'id': 'alert_001', 'severity': 'warning', 'type': 'high_cpu', 'message': 'CPU usage above 80%'},
            {'id': 'alert_002', 'severity': 'info', 'type': 'high_memory', 'message': 'Memory above 70%'}
        ],
        'total': 2
    }), 200

@app.route('/api/sla', methods=['GET'])
def get_sla_compliance():
    """Get SLA compliance metrics"""
    return jsonify({
        'success': True,
        'data': {
            'compliance_percentage': 99.5,
            'uptime_hours': 720,
            'downtime_minutes': 36
        }
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
