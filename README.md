# Lyra_Innovation

### Desarrollado en **Python** por familiaridad y velocidad de prototipado.

---

## Descripción del reto

Dado un string compuesto únicamente por dígitos y un número objetivo, el desafío consiste en determinar si es posible insertar los símbolos `+` y `-` **delante de cada dígito individual**, de modo que al evaluar la expresión resultante, se obtenga exactamente el número indicado.

---

## Enfoque y solución

Al analizar el enunciado, quedó claro que era necesario **explorar todas las combinaciones posibles de sumas y restas** aplicadas a cada dígito. Esto forma un problema clásico de toma de decisiones binarias, donde la **recursividad** encaja de forma natural y elegante.

La recursividad fue elegida no solo por su claridad conceptual, sino porque refleja perfectamente el proceso de exploración:  
- en cada paso, se decide si **sumar** o **restar** el dígito actual,  
- y luego se continúa con el siguiente dígito.

La función se invoca a sí misma recursivamente, **avanzando dígito por dígito** y generando todas las rutas posibles en un árbol de decisiones.  
Tan pronto como se encuentra una combinación que conduce al resultado esperado, la búsqueda se **interrumpe** devolviendo `True`.

> No se utiliza `break` como en los bucles tradicionales, ya que en recursión el control de flujo se gestiona a través de los `return`.  
> En este caso, `return True` actúa como una señal de éxito, propagándose hacia arriba y cortando el resto de la exploración innecesaria.

---

## Resultado

El algoritmo imprime `"yes"` si existe **al menos una** combinación de signos que produzca el número deseado, o `"no"` si **ninguna** combinación posible lo logra.
