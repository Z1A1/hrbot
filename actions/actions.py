# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict,List
#
from rasa_sdk import Action, Tracker,FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
#
#
class ActionHelloWorld(FormValidationAction):
#
     def name(self) -> Text:
         return "validate_hr_form"
#
     def validate_valider(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
       if slot_value == "look at payslip":
           
           return{"valider": True}
       elif (slot_value == "Read policies"):
           return{"valider": True}
       elif (slot_value == "Read policies"):
           return{"valider": True }
       else:
           dispatcher.utter_message(text="Please select current year")
           return {"Valider": False} 

#
         #return []
