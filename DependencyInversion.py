from abc import ABC, abstractmethod
class Notification(ABC):
 @abstractmethod
 def send_notification(self, message):
  pass

class SMSNotification(Notification):
  def send_notification(self, message):
     # Code to send an SMS notification

class NotificationService:
 def _init_(self, notification):
    self.notification = notification

 def send_notification(self, message):
      self.notification.send_notification(message)

###############################
class SMSNotification:
  def send_sms(self, message):
     # Code to send an SMS notification

class NotificationService:
 def init_(self):
        self.sms_notification = SMSNotification()
 def send_notification(self, message):
    self.sms_notification.send_sms(message)
######################################################
from abc import ABC, abstractmethod
# Define an interface for printable objects
class Printable(ABC):
 @abstractmethod
 def format(self) -> str:
  pass
# Define a class that implements the Printable interface
class Book(Printable):
 def __init__(self, title: str, author: str, content: str):
       self.title = title
       self.author = author
       self.content = content
 # Implement the format method to return the book's content
 def format(self) -> str:
     return f"{self.title} by {self.author}\n{self.content}"

 # Define a high-level module that depends on the Printable interface
class Printer:
     def print(self, printable: Printable):
     # Use the format method of the printable object
      formatted_content = printable.format()
      print(formatted_content)
# Create a book object
book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Don't Panic.")
# Create a printer object
printer = Printer()
# Print the book using the printer
printer.print(book)

'''Output: 
“The Hitchhiker's Guide to the Galaxy by Douglas Adams Don't Panic”.
This way, the Printer class does not depend on the Book class, but on the Printable interface. If you want to print other 
types of objects, such as articles, magazines, or reports, you just need to implement the Printable interface for them, and 
the Printer class will work without any changes'''

