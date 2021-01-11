class Analysis():
    
    def __init__(self, asset_df, dates):
        self.asset_df = asset_df
        self.dates = dates
        self.mov_avg_status = {}
        self.long_term = False
        self.med_term = False
        self.short_term = False
        
    def get_position(date):
        pos=-1
        for i in self.asset_df.index:
            count+=1
            if dates[0] in str(i):
                break
        return pos
            
    def moving_avgs(self):
        
        ma_list = []
        
        for date in pd.date_range(self.dates[0], self.dates[1]):
            
            b_list = []
                                          
            for mov_avg in ['MA', 'MA.1', '10', '50', '200']:
                
                b_list.append(self.asset_df.loc[date]['close'] > self.asset_df.loc[date][mov_avg])
            
            ma_list.append(b_list)
        
        df = pd.DataFrame(np.array(ma_list))
        
        ma_rat = []
        
        for i in range(df.shape[1]):
            
            ratio = df[df[i]==True].count()/df.shape[0]
            
            ma_rat.append(ratio)
        
        print(ma_rat)
        
    def trend_analysis(self):
        try: 
            for date in pd.date_range(coinbase_btc.index[get_position(dt)-50], coinbase_btc.index[get_position(dt)]):
                
            
        except:
            IndexError
            pass
        
        try
    
    def trend_strength(self):
