Python Database Log Analyzer
-----------------------------------------------------------------

USAGE
--------------------------------------------------------------------------------
 1. Move log_analyzer.py into your linux machine with the corresponding news Database
 2. Change directory to the location of log_analyzer
 3. Run python log_analyzer.py in your terminal
 <!-- 4. Run cat (output file) to view the output of the program -->


DESCRIPTION
--------------------------------------------------------------------------------
The plain text document produced will contain the following data:

a. The three most poplar articles based on number of times it was accessed

<!-- Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views -->

b. The most popular authors by total page views

<!-- Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views -->

c. The days that have greater than 1% of requests leading to errors

<!-- (based on HTTP status code)

Example:

July 29, 2016 — 2.5% errors -->
