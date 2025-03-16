from rdflib import Graph

# Membuat objek graph RDF
g = Graph()

# Memuat file RDF
g.parse("seleksi.rdf", format="xml")

# Menampilkan semua triple dalam RDF
print("=== Triples dalam RDF ===")
for subj, pred, obj in g:
    print(subj, pred, obj)

print("\nTotal triple RDF:", len(g))
