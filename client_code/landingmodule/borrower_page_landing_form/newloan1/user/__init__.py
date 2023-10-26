from ._anvil_designer import userTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class user(userTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1.user.new_loan')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1.user.nexisting_loan')

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    ri = self.radio_button_1.selected

  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    nri = self.radio_button_2.selected

  def radio_button_3_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    oci = self.radio_button_3.selected

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    firstname = self.text_box_1.text

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    middlename = self.text_box_2.text

  def text_box_3_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    lastname = self.text_box_3.text

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    birthdate = self.date_picker_1.date

  def text_box_4_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    mobileno = self.text_box_4.text

  def text_box_5_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    clocation = self.text_box_5.text

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1.user.check_offer')










   






 
