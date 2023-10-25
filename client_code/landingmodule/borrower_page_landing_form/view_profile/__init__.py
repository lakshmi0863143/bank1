from ._anvil_designer import view_profileTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_profile(view_profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
    self.user_id = []
    self.name = []
    self.password = []
    self.mobile_no = []
    self.mail_id = []
    self.pincode = []
    

    data = tables.app_tables.users.search()
    for row in data:
      self.user_id.append(row['user_id'])
      self.name.append(row['name'])
      self.password.append(row['passward'])
      self.mobile_no.append(row['mobile_no'])
      self.mail_id.append(row['mail_id'])
      self.pincode.append(row['pincode'])
      
    
    self.label_3.text = self.user_id[-1]
    self.label_5.text = self.name[-1]
    self.label_7.text = self.password[-1]
    self.label_9.text = self.mobile_no[-1]
    self.label_11.text = self.mail_id[-1]
    self.label_13.text = self.pincode[-1]
    print(self.pincode)


  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('landingmodule.borrower_page_landing_form')

    