# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones={"London": "UTC+1:00", "Sofia": "UTC+3:00", "Mumbai":"UTC+5:30", "Gurgaon":"UTC+5:30", "Lisbon":"UTC+1:00", "Paris":"UTC+1:30", "New York":"UTC-7:00"}

class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city=tracker.get_slot("city")
        timezone=timezones.get(city, "UTC+7:30")

        dispatcher.utter_message(text=f"The time zone of {city} is {timezone}")

        return []
