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

inicio = input('Inserta el nombre de la estacion desde la cual vas a partir \n')
destino = input('Inserta el nombre de la estacion a la cual quieres llegar \n')

lista_bfs = [inicio]
recorrido = {inicio: None}
ruta = []

for estacion in lista_bfs:
  adyacencias = [s[1] for s in list(nx.edges(G, estacion))]
  for adyacencia in adyacencias:
    if adyacencia not in recorrido:
      lista_bfs.append(adyacencia)
      recorrido[adyacencia] = estacion

actual = destino
while(actual != inicio):
  ruta.append(actual)
  actual = recorrido[actual]
ruta.append(inicio)
print(ruta[::-1])
