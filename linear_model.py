import pandas as pd

test_df = pd.DataFrame(data = {'x_series':[4,5,13,3],'y_series':[12,17,23,8]}) # m, r, r^2 all = 2, b = 0
loldata = pd.read_csv("dirty.csv")

class Model:

	""" There are various methods here that use different algorithms in an attempt to find 
	the best way to fill in the missing data points in dirty.csv 
	"""

	def __init__(self, df, x_string, y_string):
		self.x_string = x_string
		self.y_string = y_string
		self.df = df
		self.x_series = self.df[x_string]
		self.y_series = self.df[y_string]
		""" Can these series be lists as to pass in multiple xs? This way, if I want
		to create some sort of composite value, I can pretty easily"""

	def run_model(self):
		# likely will have to account for NaNs at one point

		# calculate slope of linear regression line
		N = len(self.df)
		self.df["N(x*y)"] = N * (self.df[self.x_string] * self.df[self.y_string]) # take E
		self.df["N(x**2)"] = N * (self.df[self.x_string]**2) # take x squared * # of data values
		self.df = self.df.sum(axis = 0) # each of the rows get a summation
		top_of_m_equation = self.df["N(x*y)"] - (self.df["x_series"] * self.df["y_series"])
		bottom_of_m_equation = self.df["N(x**2)"] - self.df["x_series"]**2
		slope = top_of_m_equation/bottom_of_m_equation

		#calculate the y-int of the linear regression line
		yint = (self.df["y_series"] - slope*self.df["x_series"])/N

		# return a df with the slope and yint
		coef_df = pd.DataFrame(data = {'m:':[round(slope,2)],'b':[round(yint,2)]})
		return coef_df

		# you should probably multiply by 760 and not 800 because there are 40 nans
		# also need to filter out NaNs prior to running model on main data
		# then run it, and fill in the missing values
	def get_r(self):
		return self.x_series.mean()

# FIGURE OUT HOW TO USE A CHILD MODEL TO PRACTICE WITH INHERITANCE!!!!

hmm = Model(test_df,"x_series","y_series")


print(hmm.run_model())


