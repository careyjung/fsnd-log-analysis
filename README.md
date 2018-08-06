# Full Stack Nanodegree Program - Log Analysis Project
## Carey Jung, 2018-08-06

## Overview

The program [trafficreport.py](trafficreport.py) queries the project's "news" database to answer the
following three questions:

1. What are the most popular three articles of all time? Which articles have been accessed the most? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Setup
    1. Download or clone this repo into a directory in the FSND
       vagrant vm in which the news database has been installed
    2. From the command line, create the two SQL views as shown below
    3. Run the program

## Database Views
Note that for the 3rd query, I reference the views 'errorsbydate' and
'trafficbydate', which are defined as follows:

```sql
create view errorsbydate as select time::date as date, count(*) as errors from log where status != '200 OK' group by date;
create view trafficbydate as select time::date as date, count(*) as views from log group by date;
```

## Program Output
Output from the program is in [output.txt](output.txt).
