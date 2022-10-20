import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    previous_cases = {}

    # Iterate through reader variable, creating dict where key is state and value is a list of most recent 7 days of new cases
    for row in reader:
        if row["state"] in new_cases:
            seven_day_list = new_cases[row["state"]]
            new_cases[row["state"]].append(
                int(row["cases"]) - previous_cases[row["state"]]
            )
            if len(new_cases[row["state"]]) > 14:
                new_cases[row["state"]] = new_cases[row["state"]][1:]
        else:
            new_cases[row["state"]] = []
            new_cases[row["state"]].append(int(row["cases"]))
        previous_cases[row["state"]] = int(row["cases"])

    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):

    for state in sorted(states):
        last_week_avg = int(sum(new_cases[state][:7]) / 7)
        this_week_avg = int(sum(new_cases[state][7:]) / 7)

        print(f"{state} had a 7-day average of {this_week_avg} ", end="")

        # Only calculate if totals are greater than zer0
        try:
            if this_week_avg > last_week_avg:
                percent = (this_week_avg - last_week_avg) / last_week_avg * 100
                print(f"and an increase of {round(percent)}%.")
            else:
                percent = (last_week_avg - this_week_avg) / last_week_avg * 100
                print(f"and a decrease of {round(percent)}%.")
        except ZeroDivisionError:
            print()
    print()


main()
