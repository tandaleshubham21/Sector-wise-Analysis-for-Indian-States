"""Server Metrics Collection Module"""
import psutil
import os
from datetime import datetime
from typing import Dict

class ServerMetricsCollector:
    """Collects system metrics from local or remote servers"""

    def collect_cpu_metrics(self) -> Dict:
        """Collect CPU usage metrics"""
        return {
            'timestamp': datetime.now(),
            'cpu_percent': psutil.cpu_percent(interval=1),
            'cpu_count_logical': psutil.cpu_count(logical=True),
            'load_average': os.getloadavg() if hasattr(os, 'getloadavg') else [0, 0, 0]
        }

    def collect_memory_metrics(self) -> Dict:
        """Collect Memory usage metrics"""
        vm = psutil.virtual_memory()
        return {
            'timestamp': datetime.now(),
            'total': vm.total,
            'used': vm.used,
            'percent': vm.percent
        }

    def collect_disk_metrics(self) -> Dict:
        """Collect Disk usage metrics"""
        usage = psutil.disk_usage('/')
        return {
            'timestamp': datetime.now(),
            'total': usage.total,
            'used': usage.used,
            'percent': usage.percent
        }

    def collect_all_metrics(self) -> Dict:
        """Collect all system metrics"""
        return {
            'cpu': self.collect_cpu_metrics(),
            'memory': self.collect_memory_metrics(),
            'disk': self.collect_disk_metrics(),
            'timestamp': datetime.now()
        }

if __name__ == '__main__':
    collector = ServerMetricsCollector()
    metrics = collector.collect_all_metrics()
    print(f"✅ CPU: {metrics['cpu']['cpu_percent']}%, Memory: {metrics['memory']['percent']}%")
