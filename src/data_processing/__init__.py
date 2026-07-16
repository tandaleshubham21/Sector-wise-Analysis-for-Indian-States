"""ETL Pipeline for metrics processing"""
from datetime import datetime
from typing import List
import logging

logger = logging.getLogger(__name__)

class ETLPipeline:
    """Extract, Transform, Load pipeline"""

    @staticmethod
    def transform_metrics(raw_metrics: dict) -> List:
        """Transform raw metrics into database format"""
        timestamp = raw_metrics.get('timestamp', datetime.now())
        cpu = raw_metrics.get('cpu', {})
        mem = raw_metrics.get('memory', {})
        disk = raw_metrics.get('disk', {})
        
        return [(
            timestamp,
            cpu.get('cpu_percent', 0),
            mem.get('percent', 0),
            disk.get('percent', 0),
            'active'
        )]

class AnomalyDetector:
    """Detect anomalies using statistical methods"""
    
    def __init__(self, threshold_sigma: float = 2.0):
        self.threshold_sigma = threshold_sigma
    
    def detect_anomalies(self, metrics_list: List[float]) -> List[bool]:
        """Detect anomalies using z-score"""
        if len(metrics_list) < 2:
            return [False] * len(metrics_list)
        
        import statistics
        mean = statistics.mean(metrics_list)
        stdev = statistics.stdev(metrics_list) if len(metrics_list) > 1 else 0
        
        return [abs((m - mean) / stdev) > self.threshold_sigma for m in metrics_list] if stdev > 0 else [False] * len(metrics_list)
