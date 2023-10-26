from ._anvil_designer import loantypeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class loantype(loantypeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan.k12_loan')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan.business_loan')

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    Notification()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('submitted succesfull')
    open_form('landingmodule.borrower_page_landing_form')




