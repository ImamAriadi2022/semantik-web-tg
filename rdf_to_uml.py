from rdflib import Graph, Namespace
from graphviz import Digraph

# Load RDF ke dalam Graph
g = Graph()
g.parse("seleksi.rdf", format="xml")

# Namespace RDF
ns = Namespace("http://www.example.org/university_admission#")

# Membuat diagram UML dengan Graphviz
dot = Digraph(format="png")  # Format output PNG

# Menambahkan node untuk setiap kelas RDF
classes = {
    "Siswa": "Siswa",
    "PerguruanTinggi": "Perguruan Tinggi",
    "JalurPendaftaran": "Jalur Pendaftaran",
    "SNBP": "SNBP",
    "SNBT": "SNBT",
    "Mandiri": "Mandiri",
    "HasilSeleksi": "Hasil Seleksi",
}

for class_id, label in classes.items():
    dot.node(class_id, label, shape="box", style="filled", fillcolor="lightblue")

# Menambahkan relasi dari RDF ke UML
relationships = [
    (ns.Siswa, ns.mendaftarKe, ns.JalurPendaftaran),
    (ns.Siswa, ns.dapatMengikuti, ns.SNBT),
    (ns.JalurPendaftaran, ns.memilikiHasil, ns.HasilSeleksi),
    (ns.Siswa, ns.diterimaDi, ns.PerguruanTinggi),
]

for subj, pred, obj in relationships:
    dot.edge(subj.split("#")[-1], obj.split("#")[-1], label=pred.split("#")[-1])

# Simpan diagram UML
dot.render("rdf_uml_diagram")

print("Diagram UML telah berhasil dibuat sebagai rdf_uml_diagram.png")
