import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def plot_correlation_network(corrMatrix):
	indexes = corrMatrix.index.values
	G=nx.Graph()
	G.add_nodes_from(indexes)

	#loop over indexes and for each pair, find its correlation value from corrMatrix and add as weight.
	for row in indexes:
		for col in indexes:
			wt = corrMatrix.get_value(row,col)
			G.add_edge(row, col, weight=wt )
	nx.draw(G)
	#plt.show()

if __name__ == '__main__':
	df = pd.read_hdf('../data/anes_timeseries_thermometer.h5')
	
	print('This is info about the survey data in the file.')
	df.info()
	
	# split table into separate tables for each year
	yearList = np.unique(df['VCF0004'])
	numYears = yearList.size
	dataByYear = []
	for yr in yearList:
		dataByYear.append(df[df['VCF0004'] == yr])
		print('%d survey has %d entries' % (yr, dataByYear[-1].size))
		
		
	print('Just keep in mind that many of the entries will have empty data for certain survey quesitons.')
	
	#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.corr.html
	corrMats = []
	for i in range(numYears):
		corrMats.append(dataByYear[i].corr(method='pearson'))
		print('For %d:' % (yearList[i]))
		print(corrMats[-1])
		#call function to plot correlation network
		plot_correlation_network(corrMats[-1])
		
	print('NaN values indicate nobody filled out both the questions that year.')


