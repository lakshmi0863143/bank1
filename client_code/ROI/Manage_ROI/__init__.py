from ._anvil_designer import Manage_ROITemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Manage_ROI(Manage_ROITemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
   open_form('landingmodule.Home_direct')

  def button_1_click(self, **event_args):
   open_form('ROI.Form1')



  
