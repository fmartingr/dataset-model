dataset_model
=============

Simple model object to work with the dataset framework

```

# Define your model
class Weather(Model):
    _table = 'weather'
    _indexes = ['place', ]
    _fields = [
        ('date', datetime.now()),
        ('temperature', 0),
        ('place', None),
    ]

# Create your object and field values
item = Weather(temperature=32)
item.place = 'Madrid'

# Saves to database
item.save()

# Deletes
item.delete()

```
