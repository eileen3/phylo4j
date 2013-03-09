import sys
from py2neo import neo4j
from Bio import Phylo

#read tree
tree = Phylo.read(sys.argv[1], 'newick')
level_order_iterable = tree.find_elements()


def _get_parent(child_clade):
    node_path = tree.get_path(child_clade)
    if len(node_path) <= 1:
        return tree.root
    else:
        return node_path[-2]


#get database connection and get root node + node category index
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
batch_inserter = neo4j.WriteBatch(graph_db)

category_index = graph_db.get_or_create_index(neo4j.Node, 'Category')

#get or create tree nodes
main_tree_category_node = category_index.get_or_create('category', 'Tree', {'category': 'Tree'})
tree_internal_node_category_node = category_index.get_or_create('category', 'TreeInternalNode', {'category': 'TreeInternalNode'})
tree_leaf_node_category_node = category_index.get_or_create('category', 'TreeLeafNode', {'category': 'TreeLeafNode'})

#get property indexes
main_tree_index = graph_db.get_or_create_index(neo4j.Node, 'Tree')
tree_internal_node_index = graph_db.get_or_create_index(neo4j.Node, 'TreeInternalNode')
tree_leaf_node_index = graph_db.get_or_create_index(neo4j.Node, 'TreeLeafNode')

insertion_index = 0
insertion_id_index_dict = {}

#create tree and get rid of tree pointer node in iterable
batch_inserter.create_node({'family_name': 'name'})
batch_inserter.add_indexed_node(main_tree_index, 'family_name', 'name', insertion_index)
batch_inserter.create_relationship(main_tree_category_node, 'TREE', insertion_index)
insertion_index += 2
level_order_iterable.next()

#deal with root node
root_node = level_order_iterable.next()
batch_inserter.create_node({'something': 'name'})
batch_inserter.add_indexed_node(tree_internal_node_index, 'something', 'name', insertion_index + 1)
batch_inserter.create_relationship(insertion_index - 2, 'TREE_ROOT_NODE', insertion_index + 1)
insertion_id_index_dict[hash(root_node)] = insertion_index + 1
insertion_index += 3

for node in level_order_iterable:
    #insert leaf node
    if node.is_terminal():
        batch_inserter.create_node({'taxon': 'something'})
        batch_inserter.add_indexed_node(tree_leaf_node_index, 'taxon', 'something', insertion_index + 1)
        batch_inserter.create_relationship(insertion_id_index_dict[hash(_get_parent(node))], 'TREE_NODE_CONNECTION', insertion_index + 1)
        batch_inserter.create_relationship(tree_leaf_node_category_node, 'TREE_LEAF_NODE', insertion_index + 1)
        insertion_id_index_dict[hash(node)] = insertion_index + 1
        insertion_index += 4
    #insert internal node
    else:
        batch_inserter.create_node({'taxon': 'something'})
        batch_inserter.add_indexed_node(tree_internal_node_index, 'taxon', 'something', insertion_index + 1)
        batch_inserter.create_relationship(insertion_id_index_dict[hash(_get_parent(node))], 'TREE_NODE_CONNECTION', insertion_index + 1)
        batch_inserter.create_relationship(tree_internal_node_category_node, 'TREE_INTERNAL_NODE', insertion_index + 1)
        insertion_id_index_dict[hash(node)] = insertion_index + 1
        insertion_index += 4

insertion_index = 0
insertion_id_index_dict = {}
level_order_iterable = tree.find_elements()
#make batch insertion call

batch_inserter.submit()
