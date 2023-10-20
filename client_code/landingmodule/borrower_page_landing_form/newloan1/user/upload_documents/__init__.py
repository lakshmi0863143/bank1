from ._anvil_designer import upload_documentsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class upload_documents(upload_documentsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1.user')

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    picture = self.file_loader_1.file

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    govid = self.file_loader_2.file

  def file_loader_3_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    papers = self.file_loader_3.file

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('landingmodule.borrower_page_landing_form.newloan1.user.n_get_provisional_approval')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert('creation completion')
    open_form('landingmodule.borrower_page_landing_form.newloan1.user')




    


