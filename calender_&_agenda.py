


import datetime

class Event:
    def __init__(self, date, description):
        self.date = date
        self.description = description

class Calendar:
    def __init__(self):
        self.events = {}

    def add_event(self, event):
        if event.date in self.events:
            self.events[event.date].append(event.description)
        else:
            self.events[event.date] = [event.description]

    def view_events(self, date):
        if date in self.events:
            print(f"Events for {date}:")
            for event in self.events[date]:
                print(f"  - {event}")
        else:
            print(f"No events for {date}")

    def delete_event(self, date, description):
        if date in self.events:
            if description in self.events[date]:
                self.events[date].remove(description)
                print("Event deleted.")
            else:
                print("Event not found.")
        else:
            print("No events for the specified date.")

def get_date():
    while True:
        try:
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return date
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

if __name__ == "__main__":
    calendar = Calendar()

    while True:
        print("\nCalendar/Agenda")
        print("1. Add Event")
        print("2. View Events")
        print("3. Delete Event")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            date = get_date()
            description = input("Enter event description: ")
            event = Event(date, description)
            calendar.add_event(event)
        elif choice == '2':
            date = get_date()
            calendar.view_events(date)
        elif choice == '3':
            date = get_date()
            description = input("Enter event description to delete: ")
            calendar.delete_event(date, description)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


