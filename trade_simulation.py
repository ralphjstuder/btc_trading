import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

class Trades():
    
    def __init__(self, asset, dollar_amount, direction, trade_date, pos_price, take_prof=None, stop_loss=None, leverage=1, trade_active=False):
        self.asset = asset 
        self.trade_date = trade_date
        self.direction = direction
        self.pos_price = pos_price
        self.take_prof = take_prof
        self.stop_loss = stop_loss
        self.trade_active = trade_active
        self.trade_value = (dollar_amount/33000) * leverage
        self.returns = {}
    
    def past_trade_analysis(self):
        
        new_df = self.asset.loc[self.trade_date:]
        
        if self.direction == 'buy':
            
            if new_df[new_df['low'] <= self.stop_loss].shape[0] == 0 and new_df[new_df['high'] >= self.take_prof].shape[0] == 0:
                
                self.trade_active = True
                
            elif new_df[new_df['low'] <= self.stop_loss].shape[0] > 0 and new_df[new_df['high'] >= self.take_prof].shape[0] == 0:
                
                self.returns['loss'] = int((self.pos_price - self.stop_loss) * self.trade_value)
                
                return self.returns
                
            elif new_df[new_df['low'] <= self.stop_loss].shape[0] == 0 and new_df[new_df['high'] >= self.take_prof].shape[0] > 0:
                
                self.returns['profit']= int((self.take_prof - self.pos_price) * self.trade_value)
                
                return self.returns
                
            else:
                sell_trigger_date = new_df[new_df['low'] <= self.stop_loss].index[0]
                buy_trigger_date = new_df[new_df['high'] >= self.take_prof].index[0]
            
                if sell_trigger_date < buy_trigger_date:
                    
                    self.returns['loss'] = int((self.pos_price - self.stop_loss) * self.trade_value)
                    
                    return self.returns
            
                elif buy_trigger_date < sell_trigger_date:
                    
                    self.returns['profit']= int((self.take_prof - self.pos_price) * self.trade_value)
                    
                    return self.returns
                    
                elif sell_trigger_date == buy_trigger_date:
                    
                    print(sell_trigger_date)
                    
                    print('Smaller price data timeframe required!')
                
                
                  
        if self.direction == 'sell':
            
            if new_df[new_df['high'] >= self.stop_loss].shape[0] == 0 and new_df[new_df['low'] <= self.take_prof].shape[0] == 0:
                
                self.trade_active = True
                
            elif new_df[new_df['high'] >= self.stop_loss].shape[0] > 0 and new_df[new_df['low'] <= self.take_prof].shape[0] == 0:
                
                self.returns['loss'] = int((self.pos_price - self.stop_loss) * self.trade_value)
                
                return self.returns
                
            elif new_df[new_df['high'] >= self.stop_loss].shape[0] == 0 and new_df[new_df['low'] <= self.take_prof].shape[0] > 0:
                
                self.returns['profit']= int((self.take_prof - self.pos_price) * self.trade_value)
                
                return self.returns
                
            else:
                sell_trigger_date = new_df[new_df['High'] >= self.stop_loss].index[0]
                buy_trigger_date = new_df[new_df['Low'] <= self.take_prof].index[0]
            
                if sell_trigger_date < buy_trigger_date:
                    
                    self.returns['loss'] = int((self.pos_price - self.stop_loss) * self.trade_value)
                    
                    return self.returns
            
                elif buy_trigger_date < sell_trigger_date:
                    
                    self.returns['profit']= int((self.pos_price - self.take_prof) * self.trade_value)
                    
                    return self.returns
                    
                elif sell_trigger_date == buy_trigger_date:
                    
                    print('Smaller price data timeframe required!')
