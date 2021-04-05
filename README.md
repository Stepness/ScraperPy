ScraperPy

Scraper made for an interview.  
Takes 2 numbers as inputs, one tells what page you are looking for (url starts with http://quote.cfi.cn/ and you concat the number to that.).  
The other tells which year you want from the last datatable and extract the first row of that datatable (Total equity) at 31-12 of given year and multiply it by 10^8.  

Example:  
Method(600006, 2019)  
Looks for http://quote.cfi.cn/600006  
Extract the cell in the first row of 2019-12-31 column in the last datatable and multiply it by 10^8.
