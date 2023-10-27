from ._anvil_designer import business_loanTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class business_loan(business_loanTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    onetime_payment = self.drop_down_1.selected_value

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('submitted successfully')
    open_form('landingmodule.borrower_page_landing_form.newloan.loantype')

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    emi = self.text_box_1.text

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    memi = self.text_box_2.text

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan.loantype')





