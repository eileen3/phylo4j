import sys
from py2neo import neo4j
from Bio import Phylo

#read tree
tree = Phylo.read(sys.argv[1], 'newick')
level_order_iterable = tree.find_elements()
#get rid of tree pointer node
level_order_iterable.next()


def _get_parent(child_clade):
    node_path = tree.get_path(child_clade)
    if len(node_path) <= 1:
        return tree.root
    else:
        return node_path[-2]


#get database connection and get root node + node category index
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
category_index = graph_db.get_index(neo4j.Node, 'Category')

tree_root_node_category_node = category_index.get('category', 'TreeRootNode')[0]
tree_internal_node_category_node = category_index.get('category', 'TreeInternalNode')[0]
tree_leaf_node_category_node = category_index.get('category', 'TreeLeafNode')[0]

tuple_index = 0
insertion_tuple = ()
insertion_id_index_dict = {}

for node in level_order_iterable:
    if node == tree.root:
        #assuming single root per family
        insertion_tuple += {'tree_node': 'name'}, (tree_root_node_category_node, 'TREE_ROOT_NODE', tuple_index)
        insertion_id_index_dict[hash(node)] = tuple_index
        tuple_index += 1
    elif node.is_terminal():
        insertion_tuple += {'taxon': node.name}, \
            (insertion_id_index_dict[hash(_get_parent(node))], "TREE_NODE_CONNECTION", tuple_index + 1), \
            (tree_leaf_node_category_node, 'TREE_LEAF_NODE', tuple_index + 1)
        insertion_id_index_dict[hash(node)] = tuple_index + 1
        tuple_index += 3
    else:
        insertion_tuple += {'something': 'something'}, \
            (insertion_id_index_dict[hash(_get_parent(node))], "TREE_NODE_CONNECTION", tuple_index + 1), \
            (tree_internal_node_category_node, 'TREE_INTERNAL_NODE', tuple_index + 1)
        insertion_id_index_dict[hash(node)] = tuple_index + 1
        tuple_index += 3

graph_db.create(*insertion_tuple)
