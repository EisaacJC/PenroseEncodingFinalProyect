# PenroseEncodingFinalProyect
Penrose Encoding with Python, Graph-States implemented in Mathematica.
## Cómo ejecutar?
Abrir la libreta de Wofram y evaluar cuaderno, asegurarse de que se ejecuta una máquina de Turing que tenga paro, de otra manera se ejecutará hasta desbordar la mamoria del ordenador.
## Introducción
Las Máquinas de Turing fueron propuestas por el matemático Alan Turing en 1936, son dispositivos computacionales abstractos capaces de simular la lógica de cualquier algoritmo, lo cual las convierte en una poderosa herramienta matemática para ayudar a investigar el alcance y las limitaciones de lo que se puede calcular. Desde su propuesta, las Maquinas de Turing han marcado su importancia como el modelo de computación más utilizado en las ciencias de la computación y la teoría de la complejidad.

En términos generales, las Maquinas de Turing están conformadas por cintas infinitas con representaciones binarias y un diagrama de estados o lista de instrucciones que determinaran el comportamiento de la máquina, en cada paso el estado actual y el símbolo leído en la cinta determinaran el siguiente estado, el símbolo que se emitirá en la cinta y la dirección a la cual se moverá el cabezal (derecha o izquierda).

La limitante principal de las Maquinas de Turing es que precisamente, como se mencionó previamente, simulan un cálculo especifico, por lo que para cada nuevo cálculo que se quiera simular es necesario construir una maquina diferente, sin embargo, es posible codificar la lista de instrucciones de cualquier máquina de Turing en una cadena y construir una máquina de Turing que espere en su cinta una cadena que describa una lista de instrucciones, seguida de una cadena que describa la cinta de entrada, y compute la cinta que la Máquina de Turing codificada habría computado, esta Máquina de Turing capaz de emular el comportamiento de cualquier otra Máquina de Turing es conocida como la Maquina de Turing Universal.

Si bien la cinta infinita que usan las Maquinas de Turing ya tiene una representación binaria, es necesaria una codificación que permita a la maquina distinguir entre espacios, instrucciones, números, etc. Distintos autores han propuesto sus codificaciones para lidiar con este problema, uno de ellos es Roger Penrose que propone una serie de equivalencias para lograr una codificación simple y eficiente.

En este proyecto se presenta la codificación de Penrose aplicada a un número m con notación decimal que representará las instrucciones de la m-ésima Máquina de Turing, para posteriormente construir el diagrama de estados de dicha Máquina y el comportamiento que tendrá dado un número n de entrada.

## Marco teórico

En 1936 y de manera independiente fueron publicados tres artículos; "Finite Combinatory Processes—Formulation 1" por Emil Post y que da origen a la máquina de POST, "An Unsolvable Problem of Elementary Number Theory" por Alonzo Church el cual formula el cálculo $\lambda$  y "On computable numbers, with an application to the Entscheidungsproblem" por Alan Turing que da origen a las máquinas de Turing.

En _esencia_ la máquina de Post publicada por Emil Post y la máquina de Turing son equivalentes, de igual manera la máquina de Turing y el cálculo $\lambda$  de Church son equivalentes. 

La propuesta hecha por Turing es similar a los autómatas finitos pero con una memoria ilimitada y sin restricciones. En este sentido la máquina de Turing es un modelo de cómputo general, las máquinas de Turing pueden llevar a cabo las mismas operaciones que una computadora real, sin embargo, esto no implica que todos los problemas puedan ser resueltos por una máquina de Turing.


Cinco años antes de que la propuesta de Turing fuese publicada, K. Göedel (1931) probó su teorema de incompletitud, el cual se puede entender como la no existencia de una teoría matemática que pueda ser enteramente demostrable, es decir, que sea demostrable a partir de algo que no fuesen supuestos. 
Formalmente esto se dice según Göedel como:

> "Para toda fórmula A de la lógica cuantificacional de primer orden, si A es lógicamente verdadera, entonces A es deducible". Dicho formalmente: "Si ╞ A, entonces ├ A"[cita]

Esto está intrínsecamente relacionado con lo propuesto por Church/Turing, pues en sus trabajos ellos proponen que las máquinas de Turing solo son capaces de computar funciones recursivamente numerables.

Una máquina de Turing consiste de un control finito que puede estar en cualquier estado de un conjunto finito de estados. El modelo propuesto por Turing usa una cinta infinita como método de almacenamiento (memoria); tiene un cabezal, el cual puede leer, escribir y moverse a lo largo de la cinta.

Inicialmente la cinta contiene únicamente una cadena de entrada, si la máquina necesita guardar información escribirá sobre la cinta. Para poder acceder a la información la máquina puede mover su cabezal. La máquina continua con el proceso de computación asta que decide producir una salida, las salidas de _aceptación_ y de _rechazo_ son obtenidas a partir del diseño de los mismos, por otro lado, si no se tiene una opción donde la máquina tenga un estado de _aceptación_ o _rechazo_ la máquina seguirá computando para siempre, es decir sin _parar_.

Algo importante a considerar es las diferencias que presenta con respecto a los autómatas finitos.

- Una máquina de Turing puede escribir sobre la cinta y leer a partir de ella.
- El proceso de lecto-escritura puede llevarse a cabo moviéndose a la izquierda o a la derecha.
- La cinta es infinita.
- Los estados de aceptación o rechazo toman efecto de manera inmediata.

Formalmente, una máquina de Turing es una 7-tupla $M=(Q, \Sigma, \Gamma, \delta, q_0, q_{acc} ,q_{rej} )$ donde $Q, \Sigma, \Gamma$ son cojuntos finitos y:

- $Q$ es el conjunto de estados,
- $\Sigma$ es la entrada del alfabeto la cual no contiene a $\sqcup$,
- $\Gamma$ es la cinta del alfabeto, donde $\sqcup \in \mathrm{I}$ y $\Sigma \subseteq \mathrm{I}$,
- $\delta: Q \times \Gamma \longrightarrow Q \times \Gamma \times\{\mathrm{L}, \mathrm{R}\}$ es la función de transición,
- $q_{0} \in Q$ es el estado inicial,
- $q_{\text {acc }} \in Q$ es el estado de aceptación, and
- $q_{\text {rej}} \in Q$ es el estado de rechazo, y en donde se debe cumplir que: $q_{\text {rej }} \neq q_{\text {acc }}$.

* Un aspecto importante a considerar es que en general la función de transición actúa sobre $\{L,R\}$, sin embargo, puede determinarse que para una máquina de Turing que tenga algoritmo soluble en un tiempo finito la función de transición actuará sobre $\{L,R,H\}$ donde $H$ denota el valor a partir del cual la máquina se detiene, es decir, $H$ "generará" estados de la forma $q_{acc},q_{rej}$.

Pese a que la representación anterior es sumamente útil para llevar a cabo el cómputo, una representación alternativa es propuesta por Penrose en [cita], en donde, de manera similar a lo descrito anteriormente describe a la máquina de Turing como un dispositivo orientado a la realización del cómputo en general compuesto por una cinta, un cabezal y la transición de derecha a izquierda. En este caso se propone una cinta sobre la cual el cabezal se moverá, esta estará conformada por casillas "rellenas" de $\{0,1\}$, en este caso el $0$ denota una casilla en blanco y el 1 como las casillas no vacías. 

Un aspecto importante a considerar es que los estados que componen a la máquina han de ser tales que sean finitos, de manera que el comportamiento de la máquina de Turing estará completamente determinado por un estado interno y la entrada de la cinta, misma que como se mencionó previamente está compuesta únicamente de 0's y 1's.

En particular hemos de decir que siempre comenzaremos en el estado 0 y la cinta siempre deberá moverse a la derecha, esto por las razones expuestas previamente. A partir de aquí el comportamiento de la máquina de Turing será completamente determinado por las transiciones/reglas que determinan la misma.

Es posible asociar un estado de la máquina de Turing a un número natural (Considérese que $\mathbb{N}^{\prime}=\mathbb{N}+\{0\}$), bajo esta conversión podemos realizar un mapeo en un sistema numérico equivalente. El sistema binario nos servirá para llevar a cabo la codificación de los elementos de la cinta, esto es fácilmente visible si se toma en cuenta que la codificación de la cinta está compuesta por 0's y 1's. Las razones por las que la cinta está codificada en binario en lugar de algún otro sistema como el unario recae en el hecho del tamaño de memoria, pese a que para números pequeños el sistema unario es muy eficaz en números grandes el sistema binario es más compacto.

Un aspecto importante a considerar es que en el proceso descrito por Penrose para llevar a cabo la codificación se considera una "variante" del binario, la cual es descrita como _binario_ extendido. El procedimiento para convertir una salida de binario a binario extendido es sencillo, se siguen las reglas: ", → 110", "0 → 1", "1→10"

En la codificación de Penrose es posible codificar a los estados que componen a una máquina de Turing de la siguiente manera:
$0 \rightarrow 0$
$10 \rightarrow 1$
$110 \rightarrow R$
$1110 \rightarrow L$
$11110 \rightarrow S T O P$ 

A este proceso podemos llamarle _traducción_ de la máquina de Turing o _Codificación de Penrose_, pse a que las razones de esta codificación no han sido descritas formalmente aquí es posible advertir que el resultado de estas nos darán una estructura de grafo, similar a la propuesta inicialmente con la definición formal de máquina de Turing.

Podemos resumir lo descrito previamente en una serie de pasos:

*    Consideremos a un conjunto de valores \[1,2,3,4,5,...,n\] que representen los estados finitos de la cinta.

*    Podemos referirnos a los valores como instrucciones/operaciones, en donde la coma solo denota el espacio entre los números.

*    La codificación para denotar a los números se hace en binario considerando que ", → 110", "0 → 1", "1→10", de manera que el proceso de escritura en binario expandido sería mediante la lectura de los valores en binario y mediante el uso de las sustituciones previas.

*   Una condición importante es que los ceros iniciales a la izquierda son reduntantes, pues no expresan ningún valor en la codificación individual de cada número.

De esta manera es posible expresar a los elementos de la máquina de Turing en una codificación más compacta y legible pues ahora el funcionamiento de una máquina de Turing estará descrito por un conjunto finito de instrucciones. 



# La máquina de Turing Universal
La forma de describir una máquina de Turing universal o UTM por sus siglas en inglés es en principio simple, su funcionamiento consiste en traducir una lista de instrucciones de una máquina de Turing arbitraria a una cadena de 0's y 1's representadas en una cinta. La cinta es entonces usada como la parte inicial de alguna entrada para alguna máquina de Turing, la cual es llamada UTM. La máquina de Turing es un mimetizador universal, la parte inicial de la cinta provee a la UTM de toda la información que necesita para imitar cualquier máquina de Turing $T_n$ de manera exacta.

Para verificar su funcionamiento es importante tener en claro como se lleva a cabo el proceso sistemático de numeración de las máquinas de Turing. El proceso de decodificación se hace tomando en cuenta el proceso inverso a la codificación, considerando una salvedad, la introducción de unos caracteres de inicio y fin, los cuales están determinados por "110 → ," y que se puede considerar únicamente como elementos que separan a los números que deben ser leídos. Por consiguiente se adopta la codificación:
  $0$ para $0$ ó $0$,
$\quad10$ para 1 ó $1$,
$\quad 110$ para $R$,
$\quad1110$ para $L$,
$\quad 11110$ para STOP/H
Bajo este procedimiento es posible etiquetar a las máquinas de Turing, en particular las primeras 13 son:
$
\begin{aligned}
&T_{0}: \quad 00 \rightarrow 0 \mathrm{OR}, \quad 01 \rightarrow 0 \mathrm{OR}\\
&T_{1}: \quad 00 \rightarrow 00 R, \quad 0 1 \rightarrow 00 L\\
&T_{2}: \quad 00 \rightarrow 0 O R, \quad 0 1 \rightarrow 01 R \text {, }\\
&T_{3}: \quad 00 \rightarrow 0 \text { OR, } \quad 01 \rightarrow 0 \text { OSTOP, }\\
&T_{4}: \quad 00 \rightarrow 0 O R, \quad 0 1 \rightarrow 10 R \text {, }\\
&T_{5}: \quad 00 \rightarrow 0 O R, \quad 01 \rightarrow 01 \mathrm{~L} \text {, }\\
&T_{6:} \quad 00 \rightarrow 0 O R, \quad 0 1 \rightarrow 0 O R, \quad 10 \rightarrow 0 O R \text {, }\\
&T_{7:} \quad 00 \rightarrow 0 O R, \quad 0 1 \rightarrow \text { ???, }\\
&T_{8}: \quad 00 \rightarrow 0 O R, \quad 01 \rightarrow 100 R \text {, }\\
&T_{9:} \quad 00 \rightarrow 0 \mathrm{OR}, \quad 01 \rightarrow 10 \mathrm{~L},\\
&T_{10}: \quad 00 \rightarrow 0 \mathrm{OR}, \quad 01 \rightarrow 11 \mathrm{R} \text {, }\\
&T_{11}: \quad 00 \rightarrow 0 \text { OR, } \quad 01 \rightarrow 0 \text { 1STOP, }\\
&T_{12}: \quad 00 \rightarrow 00 R, \quad 0 1 \rightarrow 0 O R, \quad 10 \rightarrow 0 O R .
\end{aligned}
$
Ahora, es posible considerar la acción de una máquina de Turing $T_n$ en alguna cadena finita de 0's y 1's sobre una cinta la cual siempre alimentemos a la derecha, misma que como se discutió previamente debe estar codificada en binario extendido. Si la cinta generada de la máquina $T_n$ eventualmente se detiene la cadena de números binarios que se ha producido es la respuesta al cálculo que realiza la máquina de Turing $T_n$, dicho de otra manera:

> Una cinta de instrucciones finitas con paro conduce a la computación de la máquina de Turing $T_n$ sobre algún valor numérico, es decir: $T_n(m)=p$.
En resumen,la máquina $T_n$ será codificada en una cinta que recibirá como entrada un número m y tendrá como salida un número p.

Por ejemplo, considérese el caso en donde $T_k$ es la máquina de Turing que calcula el valor del cuadrado de un número, se tendrá que $T_k(m)=p,\text{con: } p=m^2$.

En particular en este trabajo se implementarán las máquinas de Turing $XN\times 2$ y la máquina de Turing $XN+1$ las cuales corresponden en la codificación de números naturales a la máquinas $450813704461563958982113775643437908 \text{y} 10389728107$ respectivamente.

En general, la máquina de Turing Universal se puede escribir formalmente como:
$U(n,m)=T_n(m)$ 
es decir, la máquina de Turing es una máquina que recibe dos entradas, $n$ que corresponde al número de la máquina de Turing por mimetizar y $m$, el número sobre el cual la máquina de Turing $T_n$ debe computar.

Sin embargo, como se ha descrito previamente la máquina de Turing universal es un mimetizador universal, la pregunta es, ¿existe una máquina de Turing que mimetice el comportamiento de la máquina universal?, la respuesta es sí el número $u$ que genera la máquina $T_u$.
## Metodología
Para obtener la codificación de Penrose se escribió un  programa en python que genera un archivo  csv con los elementos necesarios para generar nuestras máquinas de Turing. El algoritmo recibe como entrada un número entero m  y devuelve como salida la lista de instrucciones necesarias para aplicar la máquina a un número n. Para ello, se definen dos funciones auxiliares con el propósito de convertir a m en un número binario.  
Posteriormente, se crea la función principal, en ella se aplica sistemáticamente las equivalencias propuestas por Penrose para generar la codificación correspondiente así como las instrucciones implicadas.  Finalmente, se define una interfaz con el objetivo de aplicar las funciones anteriores y así obtener la lista de instrucciones. Para implementar nuestra decodificación se define una función auxiliar con el propósito de realizar la expansión. Dicho código se encuentra adjunto como penrose_encoding.py y corresponde a la tarea entregada anteriormente.

Para visualizar la cinta de la máquina universal de turing se desarrolló el siguiente pseudocódigo con el fin de computar la máquina universal dado un número n y la lista de reglas generada por la codificación de Penrose del programa al anterior, el código se encuentra adjunto como penrose_encoding.py:
Programa: 
## Máquina Universal de Turing

        reglas -> lista de reglas de la cinta
        cinta -> número en binario a procesar
        while True:
          i -> Índice de la i-ésima instrucción
          i_state -> estado actual de la cinta 
          for {i, i_state} in cinta:
            print(i, i_state)

          if i_state = Halt
            break

          j -> j-ésimo elemento de la cinta
          j_rule -> j-ésima regla a aplicar 	
          if {j, j_rule} not in reglas
            break

          new_symbol -> símbolo que escribe
          direction -> dirección del cabezal
          new_state -> símbolo que escribe
          if direction = left
            if pos > 0
              pos = pos - 1
            else
              insertar un 0 en la cinta
          if direction = right
            pos = pos + 1

          i_tape = new_state	
## Resultados

### Máquina Universal de Turing
![image](https://user-images.githubusercontent.com/10681481/176983812-f75f22ba-ce49-4e71-8cc7-f9966f721380.png)
### Máquina de Turing XN+1
![image](https://user-images.githubusercontent.com/10681481/176983817-3a554140-62fa-4990-ba99-f0af1449d1c4.png)
### Máquina de Turing XN*2
![image](https://user-images.githubusercontent.com/10681481/176983820-3fbe2cbc-f216-491a-a727-dc0ed912144c.png)
### Ejecución de la máquina de Turing XN+1
![image](https://user-images.githubusercontent.com/10681481/176983829-29f68eb0-3064-49db-82bd-0c4152d52048.png)
### Ejecución de la máquina de Turing XN*2
![image](https://user-images.githubusercontent.com/10681481/176983834-8059d044-747d-46ed-b7cb-df6ef80a897a.png)

## Conclusiones

En este proyecto se presentó un programa que muestra visualmente el funcionamiento de las Máquinas de Turing y la codificación de Penrose con su equivalente diagrama de estados. Se puede ver claramente que en el caso de las Máquinas de Turing XN+1 y XN*2 que fueron las pruebas ejecutadas, los resultados obtenidos fueron correctos al adicionar o multiplicar las entradas dadas a cada máquina, de igual manera esto se debió a la correcta implementación de la codificación de Penrose en la cinta.
