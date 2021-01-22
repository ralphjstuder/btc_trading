class Analysis():
    
    def __init__(self, asset_df, date):
        self.asset_df = asset_df
        self.date = date
        self.twentyfive_days = {}
        self.fifty_days = {}
        self.hundred_days = {}
        
    def get_position(self, date):
        # Get index location of date
        position = -1
        for day in self.asset_df.index:
            position += 1
            if date in str(day):
                break
        return position
            
    def recent_ma_hist(self, days=60):
        # Check the ratio of days the closing price has stayed above each moving average
        total_days = 0
        date_position = self.get_position(self.date)
        ma_status = {'MA': 0, 'MA.1': 0, '10': 0, '50': 0, '200': 0}
        for cal_date in pd.date_range(self.asset_df.index[date_position - days], self.asset_df.index[date_position]):
            total_days += 1                           
            for mov_avg in ['MA', 'MA.1', '10', '50', '200']:
                if self.asset_df.loc[cal_date]['close'] > self.asset_df.loc[cal_date][mov_avg]:
                    ma_status[mov_avg] += 1
        
        for avg in ma_status.keys():
            ma_status[avg] = ma_status[avg] / total_days
            
        return ma_status
        
    def price_trends(self):
        date_position = self.get_position(self.date)
        
        # Previous hundred days data
        hundred = {}
        for date in pd.date_range(self.asset_df.index[date_position - 100], self.asset_df.index[date_position]):
            hundred['low'].append((self.asset_df.loc[str(date).split(' ')[0]]['low']))
            hundred['high'].append((self.asset_df.loc[str(date).split(' ')[0]]['high']))
            hundred['open'].append((self.asset_df.loc[str(date).split(' ')[0]]['open']))
            hundred['close'].append((self.asset_df.loc[str(date).split(' ')[0]]['close']))
            hundred['daily change'].append((self.asset_df.loc[str(date).split(' ')[0]]['close'])
                                         - (self.asset_df.loc[str(date).split(' ')[0]]['open']))
        # Previous fifty days data
        fifty = {}
        for date in pd.date_range(self.asset_df.index[date_position - 50], self.asset_df.index[date_position]):
            fifty['low'].append(self.asset_df.loc[str(date).split(' ')[0]]['low'])
            fifty['high'].append(self.asset_df.loc[str(date).split(' ')[0]]['high'])
            fifty['open'].append(self.asset_df.loc[str(date).split(' ')[0]]['open'])
            fifty['close'].append(self.asset_df.loc[str(date).split(' ')[0]]['close'])
            fifty['daily change'].append((self.asset_df.loc[str(date).split(' ')[0]]['close'])
                                        - (self.asset_df.loc[str(date).split(' ')[0]]['open']))
        # Previous twenty five days data    
        twenty_five = {}
        for date in pd.date_range(self.asset_df.index[date_position - 25], self.asset_df.index[date_position]):
            twenty_five['low'].append(self.asset_df.loc[str(date).split(' ')[0]]['low'])
            twenty_five['high'].append(self.asset_df.loc[str(date).split(' ')[0]]['high'])
            twenty_five['open'].append(self.asset_df.loc[str(date).split(' ')[0]]['open'])
            twenty_five['close'].append(self.asset_df.loc[str(date).split(' ')[0]]['close'])
            twenty_five['daily change'].append((self.asset_df.loc[str(date).split(' ')[0]]['close'])
                                             - (self.asset_df.loc[str(date).split(' ')[0]]['open']))
        
        # Add data to the dictionary for twenty five day analysis
        self.twentyfive_days['avg daily change'] = np.mean(twenty_five['daily change'])
        self.twentyfive_days['std_dev'] = np.std(twenty_five['close'])
        self.twentyfive_days['long term ma'] = self.recent_ma_hist(days=25)['200']
        self.twentyfive_days['med term ma'] = self.recent_ma_hist(days=25)['50']
        self.twentyfive_days['short term ma'] = self.recent_ma_hist(days=25)['MA']
        
        # Add data to the dictionary for fifty day analysis
        self.fifty_days['avg daily change'] = np.mean(fifty['daily change'])
        self.fifty_days['std dev'] = np.std(fifty['close'])
        self.fifty_days['long term ma'] = self.recent_ma_hist(days=50)['200']
        self.fifty_days['med term ma'] = self.recent_ma_hist(days=50)['50']
        self.fifty_days['short term ma'] = self.recent_ma_hist(days=50)['MA']
        
        # Add data to the dictionary for one hundred day analysis
        self.hundred_days['avg daily change'] = np.mean(hundred['daily change'])
        self.hundred_days['std dev'] = np.std(hundred['close'])
        self.hundred_days['long term ma'] = self.recent_ma_hist(days=100)['200']
        self.hundred_days['med term ma'] = self.recent_ma_hist(days=100)['50']
        self.hundred_days['short term ma'] = self.recent_ma_hist(days=100)['MA']
    
        return self
