#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print len(enron_data)

numPOIs = 0
for name in enron_data:
    person = enron_data[name]
    if person['poi']:
        numPOIs += 1

print 'Number of person of interest %d: ' % numPOIs
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['SKILLING JEFFREY K']['total_payments']

numSalary = 0
for name in enron_data:
    person = enron_data[name]
    if person['salary'] != 'NaN':
        numSalary += 1
print 'Number of folks having quantified salary: %d' % numSalary

numHaveEmails = 0
for name in enron_data:
    person = enron_data[name]
    if person['email_address'] != 'NaN':
        numHaveEmails += 1
print 'Number of folks having emails: %d' % numHaveEmails

numNaNPayments = 0
for name in enron_data:
    person = enron_data[name]
    if person['total_payments'] == 'NaN':
        numNaNPayments += 1
print 'Number of people having NaN total payments %d, equi to %f percents' % (numNaNPayments, float(numNaNPayments)/len(enron_data))

numNaNPOIPayments = 0
for name in enron_data:
    person = enron_data[name]
    if person['poi'] and person['total_payments'] == 'NaN':
        numNaNPOIPayments += 1
print 'Percentage of POIs having NaN total payments %f' % (float(numNaNPOIPayments)/numPOIs)
