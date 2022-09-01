# Linkedin sales navigator data scraping

Scrape a large volume of Sales Navigator profile URLs. The profile url are in the csv file.

The output is in JSON format and contain:
- Profile details
- Full career history
- Company ID for each experience
- LinkedIn Profile URL for each provided Sales Navigator Profile URL

I used selenium with option's argument added to my chrome instance so that when the webdriver open the url, it's logged in to my sales navigator account. Then I used beautifulsoup to parse the html and extract the information needed.
