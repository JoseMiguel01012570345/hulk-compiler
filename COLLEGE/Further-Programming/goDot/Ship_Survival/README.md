# Ship Survival

## Problema escogido

## Simulación Interactiva de Conquista de Banderas

En nuestro proyecto, hemos desarrollado una simulación interactiva en la que dos comandantes de naves espaciales compiten por conquistar la bandera enemiga. Permíteme describir los detalles clave:

### Comandantes y Naves

- Hay dos comandantes: uno representando a las fuerzas aliadas y otro a las fuerzas enemigas.
Cada comandante tiene un conjunto de naves a su disposición. Estas naves son autónomas y siguen las órdenes de su comandante.

- Las naves están equipadas con inteligencia artificial que les permite tomar decisiones estratégicas en tiempo real.

#### Objetivo: Conquistar la Bandera Rival

- El objetivo principal es capturar la bandera enemiga ubicada en una base neutral.
- Al capturar la bandera rival, se derrota al enemigo y se asegura la victoria.

#### Estrategias y Desafíos

- Los comandantes deben planificar sus movimientos cuidadosamente. ¿Atacarán directamente la base enemiga o intentarán flanquearla?

- Las naves enemigas también están en movimiento y pueden interceptar a las naves aliadas.

- La inteligencia artificial de las naves evalúa situaciones como la cantidad de enemigos, la distancia a la bandera y la salud de las naves antes de tomar decisiones.

#### Derrotando al Comandante Enemigo

- Además de capturar la bandera, los comandantes pueden derrotar al enemigo eliminando su nave insignia o capturándolo.

- La derrota del comandante enemigo también garantiza la victoria.

## Explicacion del proyecto

### Tecnologías Utilizadas

#### Motor de Juegos Godot

- Utilizamos Godot como nuestro motor de juegos para renderizar los gráficos y crear la interfaz de usuario.
- Godot nos proporcionó una plataforma versátil para diseñar el entorno espacial, las naves y la bandera.

#### Implementación de Lógica en Python

- La lógica del juego, incluidos los algoritmos de inteligencia artificial, se implementó en Python.
- Python nos permitió crear una simulación dinámica y tomar decisiones estratégicas en tiempo real.

#### Conexión a Través de un Servidor

- Para conectar Godot y Python, establecimos un servidor central que gestionaba la comunicación entre ambos.
- El servidor transmitía datos como posiciones de las naves, órdenes de los comandantes y eventos del juego.

#### Inteligencia Artificial y Naves

- Algoritmo A (Astar)*
Utilizamos el algoritmo A* para determinar la secuencia de avance de las naves.
- A* calcula la ruta más corta hacia la bandera enemiga, evitando obstáculos y considerando la distancia y los costos asociados.

El uso del algoritmo A* (Astar) es una excelente elección para la simulación de batalla espacial.

- Garantiza la Ruta Más Corta:
El algoritmo A* está diseñado para encontrar la ruta más corta entre dos puntos en un grafo o mapa.
En la simulación, esto significa que las naves podrán encontrar la ruta óptima para conquistar la bandera enemiga de manera eficiente.
- Optimización de Velocidad y Uso de Memoria:
A* puede ser ajustado para equilibrar velocidad y uso de memoria.
Esto es crucial para mantener una experiencia de juego fluida y evitar retrasos en el cálculo de rutas.
- Manejo de Obstáculos y Terrenos Diferentes:
A* puede lidiar con obstáculos en el camino, como asteroides o naves enemigas.
Además, puede adaptarse a diferentes tipos de terreno espacial.
Aplicación en 2D:
A* es versátil y puede utilizarse tanto para pathfinding en un plano 2D.
Esto es importante para una simulación espacial realista y dinámica.
- En resumen, el algoritmo A* es una herramienta poderosa para la navegación de las naves en la simulación.

#### Máquina de Estados para las Naves No Comandantes

- Las naves no comandantes (agentes) utilizan una máquina de estados para tomar decisiones.
- La máquina de estados evalúa la heurística actual (por ejemplo, salud, distancia al enemigo, etc.) y decide si avanzar, disparar o rotar.

- Facilita la Implementación:
La máquina de estados es una técnica de programación que organiza el comportamiento de un sistema en diferentes estados y transiciones entre ellos.
Al utilizar una máquina de estados, podemos definir claramente los posibles estados en los que se encuentra nuestro sistema.
Esto simplifica la implementación, ya que cada estado tiene un conjunto específico de acciones asociadas, y podemos concentrarnos en programar esas acciones de manera modular.
- Heurística para Decisiones Óptimas:
En el contexto de las naves no comandantes, la máquina de estados utiliza heurísticas para evaluar el entorno y determinar la acción más eficiente.
Por ejemplo, si una nave está cerca de la bandera enemiga, la heurística podría indicar que avanzar hacia ella es la acción óptima. Si está bajo ataque, podría priorizar la defensa o el esquive.
- Adaptabilidad y Flexibilidad:
La máquina de estados permite cambiar de un estado a otro según las condiciones cambiantes.
Si una nave detecta un enemigo cercano, puede cambiar al estado de “combate” y ajustar su comportamiento en consecuencia.
Esto proporciona adaptabilidad y flexibilidad en la toma de decisiones, lo que es crucial en una simulación dinámica.

#### Aprendizaje del Ambiente

- Las naves aprenden del entorno a medida que interactúan con él.
- Observan las posiciones de las naves enemigas, la ubicación de la bandera y las acciones de su comandante.
- Basándose en esta información, ajustan su comportamiento para maximizar la eficiencia.

#### Órdenes del Comandante

- Además de su autonomía, las naves también siguen las órdenes de su comandante.
- Las órdenes pueden ser atacar, defender, flanquear o capturar la bandera.

### Generacion del mapa

## Conclusiones

En base a nuestra simulación interactiva de conquista de banderas, hemos llegado a las siguientes conclusiones:

### Efectividad de la Inteligencia Artificial (IA)

- La IA de las naves demostró ser crucial para la toma de decisiones estratégicas en tiempo real.
- Las naves pudieron adaptarse a situaciones cambiantes y optimizar sus movimientos para alcanzar el objetivo.

### Importancia de la Coordinación

- La comunicación y coordinación entre las naves y los comandantes fueron esenciales.
- Los equipos que trabajaron juntos de manera efectiva lograron una mayor tasa de éxito en la conquista de banderas.

### Equilibrio entre Ataque y Defensa

- Los comandantes debieron equilibrar sus estrategias ofensivas y defensivas.
- A veces, priorizar la defensa de la propia bandera fue más efectivo que un ataque agresivo.

### Recomendaciones de Trabajo Futuro

Para futuras iteraciones de la simulación, sugerimos considerar lo siguiente:

### Mejora de la IA

- Investigar y desarrollar algoritmos de IA más avanzados para que las naves tomen decisiones aún más inteligentes.
- Explorar técnicas de aprendizaje profundo para mejorar la adaptabilidad y la capacidad de predicción de las naves.

### Referencias Bibliográficas

Aunque nuestra simulación es principalmente un proyecto original, nos basamos en los siguientes recursos académicos y técnicos:

 - Temas de Simulacion de Luciano Garcías
 - Stuart Russell Peter Norvig artificial intelligence 2020
