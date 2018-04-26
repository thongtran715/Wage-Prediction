

						Predicting and Recommending Wage User Manual Instructions


- You will need to set up an environment such as Anaconda and Python 3.6. ( We use mainly Sklearn and other Machine Learning Library in Anaconda) and pip installation 
You can download Anaconda in this link: https://anaconda.org/
You can download Python 3.6 in this link: https://www.python.org/downloads/
You can install pip by this link: https://pip.pypa.io/en/stable/installing/
You might need to install brew as well: https://brew.sh/

- In order to use our Association Rule python file you will also might to integrate Apyori Library from https://github.com/ymoch/apyori
- If you want to try out SVM prediction model, please download SVM library from this link:
https://www.csie.ntu.edu.tw/~cjlin/libsvm/. Then you can compile format-data.py to proceed to format-data.txt that has the formatted data follow with this library and you can run it by using this command svm-run format-data.py 


In order to best use our source code, please open your Anaconda program and open Spyder
When you open Spyder, you can navigate to the different folder inside our project and simply click Green button to run the program

***************. If you choose not to download Anaconda, you will need to install some of the machine learning libraries in Sklearn ***************
You can download Sklearn by http://scikit-learn.org/stable/install.html
However, you will need to have Python, Num-py and Scipy ready before installing Sklearn and Run all our scripts in your favorite IDES or in the terminal. 


							Instructions for Our Software 
						(we will assume that you will download Anaconda)
			(If you choose not to use Anaconda, you will have to run our scripts on your own, which is more complicated)

Please Notice that: We also use XGBoosting which is not supported by Sklearn. As a result, we will ask you to install XgBoost by pip install xgboost (assume you use Mac)

** To Format Data follow SVM library please compile python format-data.py. The script “format-data.py” converted raw data from the UCI website and formatted to numeric svm and outputs to file named formatted-data.txt. Then we can use this file to run svm lib. Simply, type sim-run format-data.txt inside your terminal

** In Algorithms folder, if you want to get hands on first experiment of Classification model, we provide Naive-Bayes script just to let you have the idea of how we can use this basic model to perform our prediction task. This will give you the accuracy of using Naive-Bayes algorithm. 

** To Run other Prediction Models please go to Algorithms Folder and compile with algorithm.py. This file will give you the stimulation results of different Prediction Model tasks

** To Have more Understand about the data, please go to association-rule/understand-data folder to check out some of the scripts that we have built in order to enhance our understanding about the data. We also have chart folders to show different Chart Diagram 

** In order to show the correlation between different variables, please go to algorithms/ feature_selection.py. This script will draw the diagram of the heat correlation table. 

** To see how we use our code for data- preprocessing, please check out filling-data folder where it contains all different code for different way of filling missing values data

** To Try out Association Rules Data, please go to Association Rule folder and run script association-rule.py

** In our folder, good-data.txt contains a set of data that is being processed and used for association rule data task

** Pics Folder contain all different kind of pictures that are being used for Research Paper
