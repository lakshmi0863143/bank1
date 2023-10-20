from ._anvil_designer import make_paymentTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class make_payment(make_paymentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form')

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""

  def text_area_2_change(self, **event_args):
    """This method is called when the text in this text area is edited"""

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    payment = self.payment.selected_value

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    mobileno = self.text_box_1.text

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    holdername = self.text_box_2.text

  def text_box_3_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    cardno = self.text_box_3.text

  def text_box_4_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    cvv = self.text_box_4.text

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    expairy = self.date_picker_1.date

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('payment method completed')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1.user.make_payment.phonepay')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
   

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
   

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
   

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1.user.check_offer')

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1.user.n_get_provisional_approval')

  def text_box_5_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    cradit_dabit = self.text_box_5.text



    










    



    

    


