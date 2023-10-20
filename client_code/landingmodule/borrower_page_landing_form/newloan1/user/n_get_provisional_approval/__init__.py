from ._anvil_designer import n_get_provisional_approvalTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class n_get_provisional_approval(n_get_provisional_approvalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form')

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1.user.upload_documents')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1.user.make_payment')


    

    


