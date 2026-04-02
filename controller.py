from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from model import TipModel

Builder.load_file('view.kv')

class TipCalculator(BoxLayout):
    bill_input = StringProperty()
    tip_output = StringProperty()
    
    num_people_input=StringProperty()
    split_output=StringProperty()
    
    __model: TipModel

    def __init__(self, model):
        super().__init__()    
        self.__model = model

    def btn_click_calc_tip(self, tip_percent):
        try:
            self.__model.bill_amount = float(self.bill_input)
            self.__model.tip_percent = float(tip_percent)
            # Get tip amount from model
            tip_amount = self.__model.tip_amount
            self.tip_output = f"Tip Amount: ${self.__model.tip_amount:.2f}"
            try:
                people = int(self.num_people_input)
                if people <= 0:
                    people = 1
            except ValueError:
                people = 1

        # Update outputs
            
            self.split_output = f"Each Person Pays: ${(self.__model.bill_amount + tip_amount)/people:.2f}"
        except ValueError as ex:
            print("error")
        
