Notes on kmeans:

* Optimal value of k:
	* We use a distance function to evaluate how well our clustering is doing
	* Calculate distance from any point to its centroid
	* Increasing K will *always* improve our score, where the extreme case is
	  k = number of data points and score is zero

	* The Elbow Method: graph the score per number of clusters, when the improvement
	  to the score, bends towards the horizontal like an elbow, that is the number of
	  clusters we pick

	* Cross validation: Use our traditional cross validation method to determine the
	  number of clusters by partitioning data into v sets, train on v-1 and test the
	  resulting model on the remaining set; pick the value of k with the smallest squared
	  distance average across all cross validation tests
