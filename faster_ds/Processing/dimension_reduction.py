import pandas as pd
import matplotlib.pylab as plt

class DimensionReductionInterface:
    def method1(self, path: str, file_name: str) -> str:
         """method description"""
        pass

    def method2(self, full_file_name: str) -> dict:
        """method description"""
        pass




#Computing Linear Discriminant Analysis projection
#     lda = LinearDiscriminantAnalysis(n_components=7)
#     X_trainl = lda.fit(X_train, y_train).transform(X_train)
#     X_testl = lda.transform(X_test)    
#     classifierl = KNeighborsClassifier(n_neighbors =5, metric = 'minkowski', p = 2)
#     classifierl.fit(X_trainl, y_train)
#     l_pred = classifierl.predict(X_testl)
#     #Accuracy of LDA
#     acc2 = accuracy_score(y_test, l_pred)






class PCA:
	@staticmethod
	def pca2df(df, target_name,n_components=2):
		
		from sklearn.preprocessing import StandardScaler
		
		x = df[df.columns.difference([target_name])]
		
		y = df[target_name]
		# Standardizing the features
		x = StandardScaler().fit_transform(x)
		
		from sklearn.decomposition import PCA
		pca = PCA(n_components=n_components)
		principalComponents = pca.fit_transform(x)
		principalDf = pd.DataFrame(data = principalComponents
			     , columns = ['principal component 1', 'principal component 2'])


		finalDf = pd.concat([principalDf, df[[target_name]]], axis = 1) # pca and target
		return finalDf
	
	@staticmethod
	def pca(df,target_name, n_components=2):
		from sklearn.preprocessing import StandardScaler
		x = df[df.columns.difference([target_name])]
		
		y = df[target_name]
		# Standardizing the features
		x = StandardScaler().fit_transform(x)
		
		from sklearn.decomposition import PCA
		pca = PCA(n_components=n_components)
		
		return pca
		
		
	
	
	@staticmethod
	def pca_info(pca):
		return pca.explained_variance_ratio_
	
	@staticmethod
	def plot_explained_variance(pca):
		
		plt.figure(1, figsize=(14, 13))
		plt.clf()
		plt.axes([.2, .2, .7, .7])
		plt.plot(pca.explained_variance_ratio_, linewidth=2)
		plt.axis('tight')
		plt.xlabel('n_components')
		plt.ylabel('explained_variance_ratio_')
		plt.show()
		
	@staticmethod
	def visualize(pca):
		
		
		fig = plt.figure(figsize = (8,8))
		ax = fig.add_subplot(1,1,1) 
		ax.set_xlabel('Principal Component 1', fontsize = 15)
		ax.set_ylabel('Principal Component 2', fontsize = 15)
		ax.set_title('2 component PCA', fontsize = 20)
		
	
	
	class LDA:
		raise NotImplementedError

		
	class ICA:
		raise NotImplementedError

		
