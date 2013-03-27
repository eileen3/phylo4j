from rest_framework import serializers


class ProteinSerializer(serializers.Serializer):
    protein_accession_index = serializers.CharField()
    name = serializers.CharField()
    full_name = serializers.CharField()
    short_name = serializers.CharField()
    accession = serializers.CharField()
    mass = serializers.CharField()
    length = serializers.CharField()
    modified_date = serializers.CharField()
    gene_names = serializers.CharField()
    ensembl_id = serializers.CharField()
    pir_id = serializers.CharField()
    kegg_id = serializers.CharField()
    embl_references = serializers.CharField()
    refseq_references = serializers.CharField()
    array_express_id = serializers.CharField()
    unigene_id = serializers.CharField()
    alternative_accessions = serializers.CharField()
    emsembl_plants_references = serializers.CharField()