import matplotlib.pyplot as plt
import numpy as np
plt.ion()  # Ponemos el modo interactivo
visitas = [43.97, 9.70, 7.42, 6.68, 3.91, 3.85, 3.62, 3.43, 3.16, 3.04] # Definimos un vector con el % de visitas del top ten de países
visitas = np.append(visitas, 100. - np.sum(visitas)) # Introducimos un último elemento que recoge el % de visitas de otros países fuera del top ten
paises = [u'España', u'México', 'Chile', 'Argentina', 'Colombia', 'Ecuador', u'Perú', 'USA', 'Islandia', 'Venezuela', 'Otros']  # Etiquetas para los quesitos
explode = [0, 0, 0, 0, 0, 0, 0, 0.2, 0.2, 0, 0]  # Esto nos ayudará a destacar algunos quesitos
plt.pie(visitas, labels = paises, explode = explode)  # Dibuja un gráfico de quesitos
plt.title(u'Porcentaje de visitas por país')