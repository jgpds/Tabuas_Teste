import pandas as pd
import numpy as np

standard = ['x', 'l_x', 'd_x', 'q_x', 'p_x', 'L_x', 'T_x', 'e_x', 'u_x', 'm_x']

class Tables:
    """
    Parameter: w(int) -> The last age of the table, in other words (rows-1)
    Parameter: columns(list) -> List with the columns names in order. By Default this parameter is set to  ['x', 'l_x', 'd_x', 'q_x', 'p_x', 'L_x', 'T_x', 'e_x', 'u_x', 'm_x']
    """
    #standard = ['x', 'l_x', 'd_x', 'q_x', 'p_x', 'L_x', 'T_x', 'e_x', 'u_x', 'm_x']
    def __init__(self, w, columns = standard):
        self.w = w
        self.columns = columns
    def create(self):
        """
        Method that effectively create and returns the data frame.
        """
        self.df = pd.DataFrame(0, index=np.arange(self.w), columns=self.columns)
        self.df['x'] = self.df['x'].apply(lambda x: int(x))
        for row in range(self.w+1):
            self.df.at[row, 'x'] = row
            row += 1
        return self.df