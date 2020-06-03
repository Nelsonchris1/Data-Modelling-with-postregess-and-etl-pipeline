# Data Modelling with postregess and ETL pipeline
_____________________________________________________________

# Udacity Data Engineering Nanodegree Project 1
_____________________________________________________________

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Project Goal
Sparkify would like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis.

In this project implemented the start Schema for creating the database with Fact and Dimension table
1. Fact table : songplays
2 Dimension table: users, artists, song, time

<img src="star_schema_photo.jpg" alt="drawing" width="400"/>

### Project structure
1. test.ipynb displays the first few rows of each table to let you check your database.
2. create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL      scripts.
3. etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook    contains detailed instructions on the ETL process for each of the tables.
4. etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based    on your work in the ETL notebook.
5. sql_queries.py contains all your sql queries, and is imported into the last three files above.
6. README.md provides discussion on your project.
