#Gestión de hábitats en peligro: Crea un diccionario que asocie especies animales en peligro de extinción con información sobre sus hábitats amenazados, lo que permite priorizar la protección de áreas críticas para la supervivencia de estas especies
# Diccionario de hábitats en peligro
habitats_en_peligro = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}

# Añadir 2 hábitats más con 2 especies cada uno
habitats_en_peligro.update({
    "sahara": {
        "especies": {"camello", "fennec"}
    },
    "australia": {
        "especies": {"canguro", "koala"}
    }
})

# ¿Existe el hábitat 'amazonas'?
existe_amazonas = 'amazonas' in habitats_en_peligro
print("¿Existe 'amazonas'?:", existe_amazonas)

# Añadir la especie 'anaconda' al amazonas
habitats_en_peligro['amazonas']['especies'].add("anaconda")