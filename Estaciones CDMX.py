import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
metro_cdmx = {
    "Línea 1": [
        "Pantitlán", "Zaragoza", "Gómez Farías", "Boulevard Puerto Aéreo",
        "Balbuena", "Moctezuma", "San Lázaro", "Candelaria", "Merced",
        "Pino Suárez", "Isabel la Católica", "Salto del Agua", "Balderas",
        "Cuauhtémoc", "Insurgentes", "Sevilla", "Chapultepec", "Juanacatlán",
        "Tacubaya", "Observatorio"
    ],
    "Línea 2": [
        "Cuatro Caminos", "Panteones", "Tacuba", "Cuitláhuac", "Popotla",
        "Colegio Militar", "Normal", "San Cosme", "Revolución", "Hidalgo",
        "Bellas Artes", "Allende", "Zócalo/Tenochtitlan", "Pino Suárez",
        "San Antonio Abad", "Chabacano", "Viaducto", "Xola", "Villa de Cortés",
        "Nativitas", "Portales", "Ermita", "General Anaya", "Tasqueña"
    ],
    "Línea 3": [
        "Indios Verdes", "Deportivo 18 de Marzo", "Potrero", "La Raza",
        "Tlatelolco", "Guerrero", "Hidalgo", "Juárez", "Balderas",
        "Niños Héroes", "Hospital General", "Centro Médico",
        "Etiopía/Plaza de la Transparencia", "Eugenia", "División del Norte",
        "Zapata", "Coyoacán", "Viveros/Derechos Humanos",
        "Miguel Ángel de Quevedo", "Copilco", "Universidad"
    ],
    "Línea 4": [
        "Martín Carrera", "Talismán", "Bondojito", "Consulado",
        "Canal del Norte", "Morelos", "Candelaria", "Fray Servando",
        "Jamaica", "Santa Anita"
    ],
    "Línea 5": [
        "Pantitlán", "Hangares", "Terminal Aérea", "Oceanía", "Aragón",
        "Eduardo Molina", "Consulado", "Valle Gómez", "Misterios", "La Raza",
        "Autobuses del Norte", "Instituto del Petróleo", "Politécnico"
    ],
    "Línea 6": [
        "El Rosario", "Tezozómoc", "UAM-Azcapotzalco",
        "Ferrería/Arena Ciudad de México", "Norte 45", "Vallejo",
        "Instituto del Petróleo", "Lindavista", "Deportivo 18 de Marzo",
        "La Villa-Basílica", "Martín Carrera"
    ],
    "Línea 7": [
        "El Rosario", "Aquiles Serdán", "Camarones", "Refinería", "Tacuba",
        "San Joaquín", "Polanco", "Auditorio", "Constituyentes", "Tacubaya",
        "San Pedro de los Pinos", "San Antonio", "Mixcoac",
        "Barranca del Muerto"
    ],
    "Línea 8": [
        "Garibaldi/Lagunilla", "Bellas Artes", "San Juan de Letrán",
        "Salto del Agua", "Doctores", "Obrera", "Chabacano", "La Viga",
        "Santa Anita", "Coyuya", "Iztacalco", "Apatlaco", "Aculco",
        "Escuadrón 201", "Atlalilco", "Iztapalapa", "Cerro de la Estrella",
        "UAM-I", "Constitución de 1917"
    ],
    "Línea 9": [
        "Tacubaya", "Patriotismo", "Chilpancingo", "Centro Médico",
        "Lázaro Cárdenas", "Chabacano", "Jamaica", "Mixiuhca", "Velódromo",
        "Ciudad Deportiva", "Puebla", "Pantitlán"
    ],
    "Línea A": [
        "Pantitlán", "Agrícola Oriental", "Canal de San Juan", "Tepalcates",
        "Guelatao", "Peñón Viejo", "Acatitla", "Santa Marta", "Los Reyes",
        "La Paz"
    ],
    "Línea B": [
        "Buenavista", "Guerrero", "Garibaldi/Lagunilla", "Lagunilla", "Tepito",
        "Morelos", "San Lázaro", "Ricardo Flores Magón", "Romero Rubio",
        "Oceanía", "Deportivo Oceanía", "Bosque de Aragón", "Villa de Aragón",
        "Nezahualcóyotl", "Impulsora", "Río de los Remedios", "Múzquiz",
        "Ecatepec", "Olímpica", "Plaza Aragón", "Ciudad Azteca"
    ],
    "Línea 12": [
        "Mixcoac", "Insurgentes Sur", "Hospital 20 de Noviembre", "Zapata",
        "Parque de los Venados", "Eje Central", "Ermita", "Mexicaltzingo",
        "Atlalilco", "Culhuacán", "San Andrés Tomatlán", "Lomas Estrella",
        "Calle 11", "Periférico Oriente", "Tezonco", "Olivos", "Nopalera",
        "Zapotitlán", "Tlaltenco", "Tláhuac"
    ]
}

for linea, estaciones in metro_cdmx.items():
    nx.add_path(G, estaciones, linea=linea)

# 1. Configurar un lienzo grande para que no se encimen los nombres
plt.figure(figsize=(24, 20))

# 2. Usar el algoritmo Kamada-Kawai (distribuye mejor redes de transporte)
pos = nx.kamada_kawai_layout(G)

# 3. Colores oficiales de cada línea del Metro CDMX
colores_metro = {
    "Línea 1": "#F04E98",  # Rosa
    "Línea 2": "#005EB8",  # Azul
    "Línea 3": "#AF9800",  # Verde olivo
    "Línea 4": "#6BBBAE",  # Cian
    "Línea 5": "#FFD100",  # Amarillo
    "Línea 6": "#DA291C",  # Rojo
    "Línea 7": "#E87722",  # Naranja
    "Línea 8": "#009A44",  # Verde
    "Línea 9": "#512F2E",  # Café
    "Línea A": "#981D97",  # Morado
    "Línea B": "#B1B3B3",  # Gris/Verde
    "Línea 12": "#C99700"  # Dorado
}

# Obtener el color de cada conexión (si creaste el grafo con la Opción A)
colores_aristas = [
    colores_metro.get(G[u][v].get("linea"), "gray") for u, v in G.edges()
]

# 4. Dibujar el grafo con with_labels=True
nx.draw(
    G,
    pos,
    with_labels=True,        # <--- Activa los nombres de las estaciones
    node_size=120,           # Nodos más pequeños para dejar espacio al texto
    node_color="#1f78b4",
    edge_color=colores_aristas,
    width=2.5,
    font_size=7,             # Letra pequeña para evitar que se amontonen
    font_weight="bold",
    bbox=dict(facecolor="white", edgecolor="none", alpha=0.7, pad=0.5) # Fondo blanco tras el texto
)

plt.title("Red del Metro CDMX", fontsize=20)
plt.show()
