
# Put here your models or extend User model from bp_includes/models.py
from google.appengine.ext import ndb
from google.appengine.ext import db

# def nextValidator(prop, value):
#  return isdigit(value)
# , validator=nextValidator

def is_number(prop, value):
    if not value.isdigit():
        raise db.BadValueError("and the value is: "+value)
    return None

class Counter(ndb.Model):
   """Model for containing a count."""
   count = ndb.StringProperty(default='1000', validator=is_number) 

def update_counter():
    """Increment the named counter by 1."""
    def _update_counter():
        counter = Counter.get_by_id('KEY')
        if counter is None:
            counter = Counter(id='KEY')
        else:
            counter.count = str(int(counter.count) + 1 )
        counter.put()
        return counter.count
    # Update counter in a transaction.
    return db.run_in_transaction(_update_counter)        