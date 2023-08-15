# Databricks notebook source
#fetch parameters from Azure Data Factory
table_schema=dbutils.widgets.get("table_schema")
table_name=dbutils.widgets.get("table_name")
filePath=dbutils.widgets.get("filePath")

#create database
spark.sql(f'create database if not exists {table_schema}')

#create new external table using latest datetime location
ddl_query = """CREATE TABLE """+table_schema+"""."""+table_name+""" 
                   USING PARQUET
                   LOCATION '/mnt/bronze/"""+filePath+"""/"""+table_schema+"""."""+table_name+""".parquet'
                   """

#execute query
spark.sql(ddl_query) 
