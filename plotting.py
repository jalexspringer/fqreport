import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from gauge import gauge

class AnalysisResults:
    def __init__(self, client, data, traffic_type=None):
        self.total_percent =


    def metrics(self, data):
        df = pd.read_csv(data)
        details = {
            'totals': {
                'highRisk': df.highRisk.sum(),
                'suspect': df.suspect.sum(),
                'nonSuspect': df.nonSuspect.sum(),
                'total': df.total.sum(),
            },
            'sources': {},
            'subsources': {},
            'campaigns': {},
            'domains': {}
        }
        parameters = ['source', 'campaign', 'domain', 'subsource']
        risks = ['highRisk', 'suspect', 'nonSuspect', 'total']
        for p in parameters:
            grouped = df.groupby(p).sum()
            for r in risks:
                grouped.apply(lambda row: details[p][row.name].update(row[r]))


