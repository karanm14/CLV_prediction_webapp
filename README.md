### CLV_Prediction_WebApp v0.1 - Proof of Concept

Machine Learning Web application created using Python Flask for Customer Lifetime Value Prediction

As we all know that how all companies are moving towards data driven marketing. I have made a web application as a small demostration where marketers can look at the predicted customer life time value for individual customers and compare these with marketing costs such as acquisition, retainment strategies. Getting an idea of CLV for future quarter can affectvely help a marketer spend wisely!

In this web application, using customer level KPIs extracted from past data (past quarters) I trained a linear model to predict the CLV of the customer for the next quater. Here I chose quarter as the time window because the dataset represents transactions of an e-commerce company. 

I can divide this as, extracting the KPIs from the data using descriptive analytics. Once I had the data I trained a linear model. Post training I deployed the machine learning model on the web (heroku) using a Python Flask Web-Application. 

You can see the [ML model](https://github.com/karanm14/CLV_prediction_webapp/blob/master/train.py), [Web App](https://github.com/karanm14/CLV_prediction_webapp/blob/master/app.py) 
# The web-app can be reached at https://clvapp2.herokuapp.com

# In the next iteration of the web-app, I will release a dashboard to track KPIs of customers and predict the CLV just with the Customer ID.
