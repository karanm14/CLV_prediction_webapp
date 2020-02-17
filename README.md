# CLV_prediction_webapp
Machine Learning Web application created using Python Flask for Customer Lifetime Value Prediction

As we all know that how all companies are moving towards data driven marketing. I have made a web application as a small demostration where marketers can look at the predicted customer life time value for individual customers and compare these with marketing costs such as acquisition, retatinment strategies. 

In this web application, using customer level KPIs extracted from past data (past quarters) I trained a linear model to predict the CLV of the customer for the next quater. Here I chose quarter as the time window because the dataset represents transactions of an e-commerce company. 

I can divide this as, extracting the KPIs from the data using a descriptive analytics. Once I had the data I trained a linear model and deployed it on the web using a Python Flask Web-Application. 

The web-app can be reached at https://clvapp2.herokuapp.com
