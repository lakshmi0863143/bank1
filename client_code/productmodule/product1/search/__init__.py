from ._anvil_designer import searchTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class search(searchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.data_grid_employees.rows_per_page = int(self.text_box_1.text) + 2
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    def search(self, **event_args):
      self.data_grid_product.items=anvil.server.call(
      'search_product',
      self.text_box_search.text)