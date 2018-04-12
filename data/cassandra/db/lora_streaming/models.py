from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Store00(Model):
	uid = columns.UUID(primary_key=True)
	eui = columns.Text(required=True)
	tms = columns.DateTime(primary_key=True)
	typ = columns.Text(required=True)
	msg = columns.Text(required=False)
