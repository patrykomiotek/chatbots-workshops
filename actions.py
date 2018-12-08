from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import json
import datetime

class ActionCheckOpeningHours(Action):
   def name(self):
      # type: () -> Text
      return "check_opening_hours"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
      week_day = datetime.datetime.today().strftime('%A')
      with open('opening_hours.json') as json_file:
          data = json.load(json_file)
          days = data['items']
          try:
              open_hour = days[week_day]['open']
              close_hour = days[week_day]['close']
              dispatcher.utter_message(f'On {week_day} we are open from {open_hour} till {close_hour}')
              return [SlotSet("matches", [f'We are open from {open_hour} till {close_hour}'])]
          except KeyError:
              print('No match for open hours')
      return [SlotSet("matches", [])]
