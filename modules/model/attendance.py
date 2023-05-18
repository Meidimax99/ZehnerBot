from dataclasses import dataclass, field, asdict
from datetime import date
from user import User
import json

class AttendanceList:
    """This holds the information for the attendance of all users for all days."""
    def __init__(self):
        self.attList: list = []
        self.FILE_PATH = './data/attendance.json'

    def pushDate(self):
        today = date.today().strftime("%B-%d-%Y")
        if self.containsDay(today):
            return
        dayList = []
        for user in userList:
            userDict = {user.name : UserAttendance(present = False, excused = False, proof = "no proof").dict()}
            dayList.append(userDict)
        self.attList.append({today : dayList})

        self.sort_by_date()
    
    def deleteDate(self, date: str, user: User):
        pass
    
    def newEntry(self, day: date, user:User, present: bool, excused:bool, proof: str):
        if day > date.today():
            print("The date is in the future and cannot be changed")
            return
        formatted_date = day.strftime("%b-%d-%Y")
        new_attendee = {user.name: {'present': str(present), 'excused': str(excused), 'proof': proof}}
        new_entry = {formatted_date: [new_attendee]}
        self.attList.append(new_entry)
        self.sort_by_date()
    
    def changeAttendance(self, day: date, user: User, present: bool, excused:bool, proof: str):
        if day > date.today():
            print("The date is in the future and cannot be changed")
            return
        formatted_date = day.strftime("%b-%d-%Y")
        if not self.containsDay(formatted_date):
            # If the date or name is not found, create a new entry
            self.newEntry(day=day, user=user, present=present,excused=excused, proof=proof)
            print("No entry found at this day created a new entry")
            return
        for item in self.attList:
            if formatted_date in item:
                attendees = item[formatted_date]
                for attendee in attendees:
                    if user.name in attendee:
                        attendee[user.name]['present'] = str(present)
                        attendee[user.name]['excused'] = str(excused)
                        attendee[user.name]['proof'] = proof
                        self.sort_by_date()
                        return
                    attendees.append({user.name: {'present': str(present), 'excused': str(excused), 'proof': proof}})
                
        
    def saveAttlist(self):
        with open(self.FILE_PATH, 'w') as f:
            json.dump(self.attList, f, indent=4)

    def loadAttlist(self):
        try:
            with open(self.FILE_PATH, 'r') as f:
                self.attList = json.load(f)
        except FileNotFoundError:
            print(f"LoadingError: The Attendancelist was not found at '{self.FILE_PATH}'")

    def containsDay(self, day: str) -> bool:
        for item in self.attList:
            if day in item:
                return True
        return False

    def lastNEntriesOfUsers(self, users: list[User], n: int) -> list[dict[str, any]]:
        user_entries = []
        user_counts = {user.name: 0 for user in users}
        for item in self.attList[::-1]:
            for date, entries in item.items():
                for entry in entries:
                    for user in users:
                        if user.name in entry and user_counts[user.name] < n:
                            entry_with_date = {
                                'date': date,
                                'entry': entry
                            }
                            user_entries.append(entry_with_date)
                            user_counts[user.name] += 1
        return user_entries
    
    def noProofOrExcuse(self, day: date):
        names = []
        for item in self.attList:
            for date_key, entries in item.items():
                if date_key == day.strftime("%b-%d-%Y"):
                    for entry in entries:
                        for name, attendance in entry.items():
                            if attendance['proof'] == 'no proof' and attendance['excused'] == 'False':
                                names.append(name)
        
        return names
    def sort_by_date(self):
        self.attList = sorted(self.attList, key=lambda x: list(x.keys())[0], reverse=True)
    
    def prettyPrint(self):
        print(json.dumps(self.attList, indent=4))
            

@dataclass(kw_only=True)
class UserAttendance:
    """This holds the information for the attendance of a one User on one day."""
    present: bool = False
    excused: bool = False
    proof: str = "no proof"
    
    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}
