from ._anvil_designer import product1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class product1(product1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    productid=self.text_box_product_id.text
    productname=self.text_box_2.text
    membershiptype=self.text_box_3.text
    processingfee=self.text_box_4.text
    extensionfee=self.text_box_5.text
    defaulterfee=self.text_box_6.text
    extensionsallowed=self.d
    partpayments=
    foreclosure=self.text_box_13.text
    Notification("submitted successfully").show()


    anvil.server.call('add_product', productid, productname, membershiptype, processingfee, extensionfee, defaulterfee, interesttype, maxamount, minamount, tenure, extensionsallowed, partpayments, foreclosure)

  def link_1_click(self, **event_args):
    open_form('landingmodule.Home_direct')

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    
  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.data_grid_product.rows_per_page = anvil.server.call('get_product')

    open_form('productmodule.product1.search.RowTemplate1')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_button_3_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def text_box_3_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def drop_down_3_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def drop_down_4_change(self, **event_args):
    """This method is called when an item is selected"""
    pass









    



 

 

  


  


  


  

 

