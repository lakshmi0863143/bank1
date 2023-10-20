from ._anvil_designer import ProductsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Products(ProductsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_copy_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('openform')

  def link_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

  def link_1_copy_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('productmodule.manageproducts')

  def link_1_copy_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def link_1_copy_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def link_1_copy_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass





  
