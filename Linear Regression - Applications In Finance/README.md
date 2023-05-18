# INTRO 

In this notebook, my aim is to consolidate my learning of linear regression models. 

I chose an application from finance: using the CAPM theory to price the General Electric (GE) stock. 


I will do that in the following steps: 
* Use a simple regression to estimate the relationship GE's excess return and the market portfolio's excess return (SP500 will be used as proxy for market portfolio)
* Run a regresion diagnostic and revisit the assumptions if necessary 
* Plot GE's actuall excess return on the revisted regression line. If it is above, then AAPL is underpriced. If it is below, then AAPL is overpriced. 

During my learning i used the following sources:
* Case study: https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/mit18_s096f13_casestudy1/
* Thoertical background for regression analysis: https://online.stat.psu.edu/stat462/node/87/
* Diagnostic analysis: https://robert-alvarez.github.io/2018-06-04-diagnostic_plots/

