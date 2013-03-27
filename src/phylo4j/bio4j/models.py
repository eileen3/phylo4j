import os

from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom

#phylofacts tree classes

class Tree(StructuredNode):
    family_name = StringProperty(index=True)
    root = RelationshipTo('_TreeNode', 'TREE_ROOT_NODE')


class _TreeNode(StructuredNode):
    parent = RelationshipFrom('_TreeNode', 'TREE_NODE_CONNECTION')
    children = RelationshipTo('_TreeNode', 'TREE_NODE_CONNECTION')

    def mrca(self, *args):
        if len(args) == 1:
            result = self.cypher('START x=node(9),y=node(10) \
                                  MATCH p=shortestPath(y-[:TREE_NODE_CONNECTION*]-x) \
                                  RETURN FILTER ( n in nodes(p) : y<-[*]-(n)-[*]->x);')
            return TreeInternalNode.inflate(result[0][0][0][0])


class TreeInternalNode(_TreeNode):
    something = StringProperty(index=True)


class TreeLeafNode(_TreeNode):
    taxon = StringProperty(index=True)


# imported models from bio4j: https://github.com/bio4j/Bio4j/tree/master/src/main/java/com/era7/bioinfo/bio4j/model/nodes

class AlternativeProduct(StructuredNode):
    _index_name = 'alternative_product_name_index'
    alternative_product_name_index = StringProperty(index=True)

    name = StringProperty()


class City(StructuredNode):
    _index_name = 'city_name_index';
    city_name_index = StringProperty(index=True)
    
    name = StringProperty()


class CommentType(StructuredNode):
    _index_name = 'comment_type_name_index';
    comment_type_name_index = StringProperty(index=True)
    
    name = StringProperty()


class Consortium(StructuredNode):
    _index_name = 'consortium_name_index'
    consortium_name_index = StringProperty(index=True)
    
    name = StringProperty()


class Country(StructuredNode):
    _index_name = 'country_name_index'
    country_name_index = StringProperty(index=True)
    
    name = StringProperty()


class Dataset(StructuredNode):
    _index_name = 'dataset_name_index'
    dataset_name_index = StringProperty(index=True)
    
    name = StringProperty()


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


class FeatureType(StructuredNode):
    _index_name = 'feature_type_name_index'
    feature_type_name_index = StringProperty(index=True)
    name = StringProperty()


class GoTerm(StructuredNode):
    _index_name = 'go_term_id_index'
    go_term_id_index = StringProperty(index=True)
    
    id = StringProperty()
    name = StringProperty()
    definition = StringProperty()
    namespace = StringProperty()
    obsolete = StringProperty()
    comment = StringProperty()
    alternative_ids = StringProperty()
    biological_process = StringProperty()
    molecular_function = StringProperty()
    cellular_component = StringProperty()


class Institute(StructuredNode):
    _index_name = 'institute_name_index'
    institute_name_index = StringProperty(index=True)
    
    name = StringProperty()


class Interpro(StructuredNode):
    _index_name = 'interpro_id_index'
    interpro_id_index = StringProperty(index=True)
    
    id = StringProperty()
    name = StringProperty()


class Isoform(StructuredNode):
    _index_name = 'isoform_id_index'
    isoform_id_index = StringProperty(index=True)
    
    id = StringProperty()
    name = StringProperty()
    note = StringProperty()
    sequence = StringProperty()


class Keyword(StructuredNode):
    _index_name = 'keyword_id_index'
    keyword_id_index = StringProperty(index=True)
    
    id = StringProperty()
    name = StringProperty()


class Organism(StructuredNode):
    _index_name = 'organism_scientific_name_index'
    organism_scientific_name_index = StringProperty(index=True)
    #second index: 'organism_ncbi_taxonomy_id_index' included in OrganismNode.java
    
    scientific_name = StringProperty()
    common_name = StringProperty()
    synonym_name = StringProperty()
    ncbi_taxonomy_id  = StringProperty()


class Person(StructuredNode):
    _index_name = 'person_name_full_text_index'
    person_name_full_text_index = StringProperty(index=True)
    
    name = StringProperty()


class Pfam(StructuredNode):
    _index_name = 'pfam_id_index'
    pfam_id_index = StringProperty(index=True)
    
    id = StringProperty()
    name = StringProperty()


class Protein(StructuredNode):
    _index_name = 'protein_accession_index'
    protein_accession_index = StringProperty(index=True)
    #three additional indexes included: 
    #   protein_full_name_full_text_index, 
    #   protein_gene_names_full_text_index, 
    #   protein_ensembl_plants_index
    
    name = StringProperty()
    full_name = StringProperty()
    short_name = StringProperty()
    accession = StringProperty()
    mass = StringProperty()
    length = StringProperty()
    modified_date = StringProperty()
    gene_names = StringProperty()
    ensembl_id = StringProperty()
    pir_id = StringProperty()
    kegg_id = StringProperty()
    embl_references = StringProperty()
    refseq_references = StringProperty()
    array_express_id = StringProperty()
    unigene_id = StringProperty()
    alternative_accessions = StringProperty()
    emsembl_plants_references = StringProperty()


class SequenceCaution(StructuredNode):
    _index_name = 'sequence_caution_name_index'
    sequence_caution_name_index = StringProperty(index=True)
    
    name = StringProperty()


class SubcellularLocation(StructuredNode):
    _index_name = 'subcellular_location_name_index'
    subcellular_location_name_index = StringProperty(index=True)
    
    name = StringProperty()


class Taxon(StructuredNode):
    _index_name = 'taxon_name_index'
    taxon_name_index = StringProperty(index=True)
    
    name = StringProperty()
