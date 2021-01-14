class Analysis():
    
    def __init__(self, asset_df, dates):
        self.asset_df = asset_df
        self.dates = dates
        self.mov_avg_status = {}
        self.twenty_five_days = []
        self.fifty_days = []
        self.hundred_days = []
        self.long_term = False
        self.med_term = False
        self.short_term = False
        
    def get_position(self, date):
        position = -1
        for day in self.asset_df.index:
            position += 1
            if date in str(day):
                break
        return position
            
    def moving_avgs(self):
        
        ma_status = []
        
        for date in pd.date_range(self.dates[0], self.dates[1]):
            
            price_above_ma = []
                                          
            for mov_avg in ['MA', 'MA.1', '10', '50', '200']:
                
                price_above_ma.append(self.asset_df.loc[date]['close'] > self.asset_df.loc[date][mov_avg])
            
            ma_status.append(price_above_ma)
        
        df = pd.DataFrame(np.array(price_above_ma))
        
        ma_ratios = []
        
        for i in range(df.shape[1]):
            
            ratio = df[df[i]==True].count()/df.shape[0]
            
            ma_ratios.append(ratio)
        
        
     def trend_analysis(self):
    
        for date in pd.date_range(self.asset_df.index[self.get_position(self.dates[0])-100], 
                                  self.asset_df.index[self.get_position(self.dates[0])]):
            
            self.hundred_days.append(self.asset_df.loc[str(date).split(' ')[0]]['close'])

        for date in pd.date_range(self.asset_df.index[self.get_position(self.dates[0])-50], 
                                  self.asset_df.index[self.get_position(self.dates[0])]):
            
            self.fifty_days.append(self.asset_df.loc[str(date).split(' ')[0]]['close'])

        for date in pd.date_range(self.asset_df.index[self.get_position(self.dates[0])-25], 
                                  self.asset_df.index[self.get_position(self.dates[0])]):
            
            self.twenty_five_days.append(self.asset_df.loc[str(date).split(' ')[0]]['close'])
    
        return self.fifty_days, self.hundred_days, self.twenty_five_days
    
    def trend_strength(self):
