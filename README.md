laptop price predictor (feb 2024)

A customer need to enter certain details like company name, type of laptop, RAM size, weight of laptop,touchscreen or not,ips display or not, screen size, screen resolution, CPU brand name, HDD size, SSD size, GPU brand name, operating system etc and model will predict the price of the laptop


1. It is a machine learning regression project.
2. i create a website and machine learning model works in the backgroud in a such a way that if a user tell desired configuration of laptop then model will predict the price of laptop according to the configuration.
3. please note that, i train my model on three years old dataset.

stages of project :
1. data cleaning
2. EDA (#data analysis)
3. feature engineering
4. modelling (#machine learning models, #model evaluation)
5. website
6. deployment


observation :
i predicted price for apple macbook air m1 (chip)
a) price predicted by model : 77410.16
b) actual product price in market :-
    flipkart and amazon = 83990
    croma and reliance digital = 80990
    jio mart = 78490
    unicorn = 79920
    apple store = 99900                      
note : all prices are exclusive of bank credit cards offer

result : 1)i guess model is giving fair result
         2)we need to improve our model by providing fresh and larget dataset
         3)obviously we need to do some more feature engineering with time 


challenges/issues/limitations : 
1. sometimes predicted price may vary in a large amount according to offer/discount given by brand/seller.
2. this dataset is 3 years old. we need to train our model with the recent time dataset to get results/price close to actual price.
3. model is trained on 1303 rows only. this is a very small dataset.

