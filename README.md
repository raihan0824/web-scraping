# kickoffai web scraping

URL: https://kickoff.ai/matches

Below is the desired page to be scraped:
![alt text](https://github.com/raihan0824/kickoffai_scraping/blob/main/past%20result.png)

Data to be saved:

- Date
- Home name
- Away name
- Home goal
- Away goal
- Home win%
- Draw win%
- Away win%
- Home kick score
- Away kick score

Example of the desired data:
![alt text](https://github.com/raihan0824/kickoffai_scraping/blob/main/football%20score.png)

# Note:
Because the page is not showing the full data, I used selenium to automatically clicked the "show more" button. After the data is fully showed, I used beautifulsoup to parse the html of the page.
