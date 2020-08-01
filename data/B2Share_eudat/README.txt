1 - Name
========

Hate speech dataset annotated for Portuguese


2 - Description 
===============

Portuguese Hate Speech Twitter Dataset is a dataset of Twitter messages manually annotated for Hate Speech using a hierarchical structure of classes. 5,668 messages were collected on Twitter, from 1,156 distinct users and classified as containing hate speech using a hierarchical structure of classes. A multiclass and multilabel approach was considered. Two different formats of the dataset are provided, plus the hierarchy of classes. The text of the tweets is omitted in this dataset due to the conditions and terms of the Twitter API.


3 - File list 
=============

3.1 - Graph hierarchical classes (graph_hierarchical_classes.csv)
-----------------------------------------------------------------

The classes follow a hierarchical organization. This hierarchy is represented as a Directed Acyclic Graph (DAG) in CSV format with the source (first column, named 'Source') and destiny (second column, named 'Target') nodes. 100 lines.

3.2 - Dataset annotator classes (annotator_classes.csv)
-------------------------------------------------------

CSV file containing the dataset of tweets – represented by Twitter ID (first column, named 'tweet_id'), plus the annotator classification (second column, named 'class'). 5669 lines.

3.3 - Dataset dummy classes (dataset_dummy_classes.csv)
-------------------------------------------------------

CSV file containing the dataset as a matrix with dummy variables for each class. The first column contains the Twitter ID of each tweet (first column, named 'tweet_id'), plus 79 columns representing all classes, as converted to dummy variables. 5669 lines.


4 - Reference 
=============

Fortuna, Paula (2017). Automatic detection of hate speech in text: an overview of the topic and dataset annotation with hierarchical classes (Master Thesis). Faculty of Engineering of the University of Porto, Portugal.


5 - Contact 
===========

Paula Fortuna <paula.fortuna@fe.up.pt>