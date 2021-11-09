import syllabus_scraper

CS361_URL = 'https://oregonstate.instructure.com/courses/1877222/assignments/syllabus'
CS372_URL = 'https://oregonstate.instructure.com/courses/1830291/assignments/syllabus'


dataframe = syllabus_scraper.scrape_canvas(CS361_URL)
print(dataframe)
