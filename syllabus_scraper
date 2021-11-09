from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd

# These options make it easier to see the resulting dataframe, when testing
pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)


# Takes a url containing a syllabus and returns a dataframe object
# with tasks, dates, and times.
def scrape_canvas(url):
    session = HTMLSession()
    r = session.get(url)
    r.html.render()

    soup = BeautifulSoup(r.html.raw_html, "html.parser")
    table = soup.find(id="syllabus")
    rows = table.find_all('tr')

    last_date = None
    dates = []
    tasks = []
    times = []

    for row in rows:
        # for each row, designated by "tr", we find each data field, designated by "td"
        fields = row.find_all('td')

        # handles instances where multiple assignments are due on the same day
        if len(fields) == 3:
            td_count = 1
        elif len(fields) == 2:
            td_count = 2
            dates.append(last_date)

        for field in fields:
            cur_text = field.text.strip().replace('\n', '')
            # The first td will be the due date of the assignment
            if td_count == 1:
                dates.append(cur_text)
                last_date = cur_text
            # The second td is the task (assignment details)
            elif td_count == 2:
                # The following code strips unnecessary info from this field
                cur_text = cur_text.split("Assignment", 1)[-1].strip()
                cur_text = cur_text.replace("Calendar Event", "").strip()  # remove icon
                cur_text = cur_text.replace("(3 students)", "").strip()  # remove extraneous trailing info
                tasks.append(cur_text)
            # The third td is the time the assignment is due
            elif td_count == 3:
                times.append(cur_text)
            td_count += 1

    # Puts the data into a dictionary for formatting
    syllabus_data = {"Tasks": tasks, "Dates": dates, "Times": times}
    # Makes a pandas dataframe using the syllabus_data dictionary
    syllabus_df = pd.DataFrame(syllabus_data)

    return syllabus_df
