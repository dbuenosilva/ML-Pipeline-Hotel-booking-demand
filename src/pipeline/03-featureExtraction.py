# -*- coding: utf-8 -*-########################################################################### Project: COMP6004 - Machine learning pipeline for data analysis# File: 03-featureExtraction.py# Author: Diego Bueno - d.bueno.da.silva.10@student.scu.edu.au # Date: 20/04/2021# Description: Applying feature extraction to step03 of ML pipeline.############################################################################ Maintenance                            # Author: # Date:  # Description: A###########################################################################>import numpy as npimport pandas as pdfrom functions import openfilefrom functions import savefilefrom functions import convertfrom sklearn.feature_selection import VarianceThresholdfrom sklearn.model_selection import train_test_splitfrom sklearn.linear_model import LinearRegressionfrom sklearn.neighbors import LocalOutlierFactorfrom sklearn.metrics import mean_absolute_error#calling the function to Load data pre-reading on task 1print("\nReading the step02 file\n")db = openfile('data/step02.csv')print("\nChecking the current shape of the data:")rows, columns = db.shapeprint( str(rows) + " rows and " + str(columns) + " columns")print("\nBrief summary of data:\n")print(db.head(5))#####################################################  Starting the process of feature extraction####################################################print("\nConverting all dataframe to numerical categorical values:\n")db = convert(db)print("\nChecking the new shape of the data:")rows, columns = db.shapeprint( str(rows) + " rows and " + str(columns) + " columns")print("\nBrief summary of data:\n")print(db.head(1))#  hotel arrival_date_month meal  ... deposit_type customer_type reservation_statusprint("\nRemoving columns that have a low variance\n")# split data into inputs and outputsdata = db.valuesX = data[:,:-1]y = data[:,-1]print("\nChecking the current shape of X and y:")print(X.shape, y.shape)print("\nDefining thresholds to check low variance")thresholds = np.arange(0.0, 0.55, 0.05)# apply transform with each thresholdresults = list()for t in thresholds:	# define the transform	transform = VarianceThreshold(threshold=t)	# transform the input data	X_sel = transform.fit_transform(X)	# determine the number of input features	n_features = X_sel.shape[1]	print('>Threshold=%.2f, Features=%d' % (t, n_features))	# store the result	results.append(n_features)threshold = tprint("\nUsing threshold", threshold)print("\nDropping columns with low variance:\n")columnsWithLowVariance = db.std()[db.std() < threshold].index.valuesprint(columnsWithLowVariance)db = db.drop(columnsWithLowVariance, axis=1)rows, columns = db.shapeprint("\nThe new shape of the data: " + str(rows) + " rows and " + str(columns) + " columns\n")              print(db.head(1))   print("\nIdentifing and removing outliers based on the interquartile range method:\n")data = db.values # split into inpiut and output elementsX, y = data[:, :-1], data[:, -1] # split into train and test setsX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1) # summarize the shape of the training datasetprint("\nChecking the current shape of X and y:")print(X_train.shape, y_train.shape)# fit the modelmodel = LinearRegression()model.fit(X_train, y_train)# evaluate the modelyhat = model.predict(X_test)# evaluate predictionsmae = mean_absolute_error(y_test, yhat)print('MAE: %.3f' % mae)# identify outliers in the training datasetlof = LocalOutlierFactor()yhat = lof.fit_predict(X_train)# select all rows that are not outliersmask = yhat != -1X_train, y_train = X_train[mask, :], y_train[mask]# summarize the shape of the updated training datasetprint(X_train.shape, y_train.shape)# fit the modelmodel = LinearRegression()model.fit(X_train, y_train)# evaluate the modelyhat = model.predict(X_test)# evaluate predictionsmae = mean_absolute_error(y_test, yhat)print('MAE: %.3f' % mae)print("yhat", yhat)## Saving current DF to CSV to step03#print("\nRecording step03.scv file...")#savefile(db,"data/step03.csv")#print("done! \n\nstep03.csv file is ready for Dimensionality Reduction task\n")