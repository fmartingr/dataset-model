dataset_model
=============

Simple model object to work with the dataset framework

It's available on PyPi:

```
pip install dataset-model
```

Basic usage:

```
from dataset_model.models import Model
import dataset

# Define your model
class Weather(Model):
    _table = 'weather'
    _indexes = ['place', ]
    _fields = [
        ('date', datetime.now()),
        ('temperature', 0),
        ('place', None),
    ]

# Create the engine
engine = dataset.connect('sqlite:///:memory:')

# Create your object and field values
item = Weather(_engine=engine, temperature=32)
item.place = 'Madrid'

# Saves to database
item.save()

# Deletes
item.delete()

```
