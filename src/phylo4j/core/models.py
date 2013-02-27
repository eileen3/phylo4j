import os
os.environ['NEO4J_REST_URL'] = 'http://localhost:7474/db/data/'
from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom


class Enzyme(StructuredNode):

	_index_name = 'enzyme_id_index'
	enzyme_id_index = StringProperty(index=True)

	id = StringProperty()
	official_name = StringProperty()
	alternate_names = StringProperty()
	catalytic_activity = StringProperty()
	cofactors = StringProperty()
	comments = StringProperty()
	prosite_cross_references = StringProperty()

