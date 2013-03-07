import os
os.environ['NEO4J_REST_URL'] = 'http://localhost:7474/db/data/'
from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom

# imported models from bio4j: https://github.com/bio4j/Bio4j/tree/master/src/main/java/com/era7/bioinfo/bio4j/model/nodes

class AlternativeProductNode(StructuredNode):
	_index_name = 'alternative_product_name_index'
	alternative_product_name_index = StringProperty(index=True)
	
	name = StringProperty()

class CityNode(StructuredNode):
    _index_name = 'city_name_index';
    city_name_index = StringProperty(index=True)
    
    name = StringProperty()
    
class CommentTypeNode(StructuredNode):
    _index_name = 'comment_type_name_index';
    comment_type_name_index = StringProperty(index=True)
    
    name = StringProperty()
    
class ConsortiumNode(StructuredNode):
    _index_name = 'consortium_name_index'
    consortium_name_index = StringProperty(index=True)
    
    name = StringProperty()
    
class CountryNode(StructuredNode):
    _index_name = 'country_name_index'
    country_name_index = StringProperty(index=True)
    
    name = StringProperty()

class DatasetNode(StructuredNode):
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
    
class FeatureTypeNode(StructuredNode):
    _index_name = 'feature_type_name_index'
    feature_type_name_index = StringProperty(index=True)

    name = StringProperty()
    
class GoTermNode(StructuredNode):
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
    
class InstituteNode(StructuredNode):
    _index_name = 'institute_name_index'
    institute_name_index = StringProperty(index=True)
    
    name = StringProperty()
    
class InterproNode(StructuredNode):
    _index_name = 'interpro_id_index'
    interpro_id_index = StringProperty(index=True)
    
    id = StringProperty()
    name = StringProperty()
    
class IsoformNode(StructuredNode):
    _index_name = 'isoform_id_index'
    isoform_id_index = StringProperty(index=True)
    
    id = StringProperty()
    name = StringProperty()
    note = StringProperty()
    sequence = StringProperty()
    
class KeywordNode(StructuredNode):
    _index_name = 'keyword_id_index'
    keyword_id_index = StringProperty(index=True)
    
    id = StringProperty()
    name = StringProperty()
    
class OrganismNode(StructuredNode):
    _index_name = 'organism_scientific_name_index'
    organism_scientific_name_index = StringProperty(index=True)
    #second index: 'organism_ncbi_taxonomy_id_index' included in OrganismNode.java
    
    scientific_name = StringProperty()
    common_name = StringProperty()
    synonym_name = StringProperty()
    ncbi_taxonomy_id  = StringProperty()
    
class PersonNode(StructuredNode):
    _index_name = 'person_name_full_text_index'
    person_name_full_text_index = StringProperty(index=True)
    
    name = StringProperty()
    
class PfamNode(StructuredNode):
    _index_name = 'pfam_id_index'
    pfam_id_index = StringProperty(index=True)
    
    id = StringProperty()
    name = StringProperty()
    
class ProteinNode(StructuredNode):
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
    
class SequenceCautionNode(StructuredNode):
    _index_name = 'sequence_caution_name_index'
    sequence_caution_name_index = StringProperty(index=True)
    
    name = StringProperty()
    
class SubcellularLocationNode(StructuredNode):
    _index_name = 'subcellular_location_name_index'
    subcellular_location_name_index = StringProperty(index=True)
    
    name = StringProperty()
    
class TaxonNode(StructuredNode):
    _index_name = 'taxon_name_index'
    taxon_name_index = StringProperty(index=True)
    
    name = StringProperty()
    