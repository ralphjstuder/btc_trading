class AssetData():
    """ Uses data from Tradingview """
    
    def __init__(self, filename):
        self.filename = filename
        self.data_frame = pd.read_csv(filename)
        
    def clean(self):
        self.data_frame.fillna(method='backfill', inplace=True)
        self.data_frame['date'] = pd.to_datetime(self.data_frame['time'].values, unit='s')
        self.data_frame.set_index('date', inplace=True)
        self.data_frame.drop('time', axis=1, inplace=True)
        
        return self
        
