import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def add_user(name, mobile, mail, pincode, userid, passcode):
  app_tables.users.add_row(name=name,Date_of_signup=datetime.now(),mobile_no=mobile,mail_id=mail,pincode=pincode, user_id=userid, passward=passcode)



#ProductId,ProductName,MemebershipType,ProcessingFee,ExtensionFee,DefaulterFee,InterestType,MaxAmount,MinAmount,Tenure,ExtensionsAllowed,PartPayments,ForeClosure
@anvil.server.callable
def add_product(productid, productname, membershiptype, processingfee, extensionfee, defaulterfee, interesttype, maxamount, minamount, tenure, extensionsallowed, partpayments, foreclosure):
   app_tables.product.add_row(product_id=productid, product_name=productname, membership_type=membershiptype, processing_fee=processingfee, extension_fee=extensionfee, defaulter_fee=defaulterfee, interest_type=interesttype, max_amount=maxamount, min_amount=minamount, tenure=tenure, extensions_allowed=extensionsallowed, part_payments=partpayments, foreclosure=foreclosure)

@anvil.server.callable
def add_membership(membershiptype,tenure):
  app_tables.membership.add_row(membershiptype=membershiptype,tenure=tenure)
@anvil.server.callable
def get_product():
  return app_tables.product.search()


@anvil.server.callable
def search_product(query):
  result = app_tables.product.search()
  if query:
    result = [
      x for x in result
      if query in x['product_id']
      or query in x['product_name']
      or query in x['membership_type']
    ]
  return result