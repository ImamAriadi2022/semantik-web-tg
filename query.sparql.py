from rdflib import Graph, Namespace

# Load data RDF
g = Graph()
g.parse("seleksi_masuk.ttl", format="turtle")

# Definisi namespace
ex = Namespace("http://example.com/seleksi#")

# Query SPARQL
query = """
PREFIX ex: <http://example.com/seleksi#>
SELECT ?siswa WHERE {
    ?siswa ex:mengikuti ex:SNBT_2025 .
}
"""

# Eksekusi Query
result = g.query(query)

# Tampilkan Hasil Query
for row in result:
    print(row.siswa)
