# Un par de aspectos sobre la geometría de los mínimos cuadrados

1. Siempre me intrigó que la primera opción para los modelos de regresión fuese minimizar los errores cuadráticos y no los absolutos. ¿Qué hay detrás de cada opción? ¿Por qué la preferencia? ¿No es más lógico usar los absolutos?

$Y = X\beta + \epsilon$ con $\beta=(X^tX)^{-1}X^tY$

2. Aunque ambas alternativas son válidas, hay motivos que favorecen a la primera opción, excepto en condiciones específicas. En este post quiero hacer foco en algo que siempre me fascinó: la intuición geométrica detrás de estas alternativas metodológicas.

3. Es que en realidad, al definir qué minimizamos estamos adoptando una métrica, 
una forma de medir distancias entre vectores. Y esa métrica se asocia también
al modo en que medimos largos y ángulos (produto interior y norma). 

- dicho de otra forma estamos adoptando una estructura para el espacio
en el que viven nuestros datos. Y como veremos, la estructura del espacio
que subyace a la elección de los errores cuadráticos es bastante más
útil que la de los absolutos.

veremos que MCO es euclidiano y MAD no.

repasar diferencias entre distancias

punto recta: euclides única e intuitiva manhattan no

ángulo: da una medida de similitud lineal.
proyeccion ortogonal. depende de como medimos largos y
del producto interior.

manhattan no tiene producto interior, no hay angulos ni
proyeccion ortogonal

MCO es euclidiano: ejemplo

MAD no: ejemplo

generalizacion

correlacion es el angulo (producto interior sobre normas)
esperanza condicional es la proyeccion etc

4. Recapitulemos. El método de mínimos cuadrados ordinarios (MCO) minimiza los errores cuadráticos. En cambio el método de Mínimas Desviaciones Absolutas (MAD) minimiza los errores absolutos. La diferencia entre ambos puede interpretarse en términos de la geometría que suponen

MCO: minimiza la suma de errores cuadráticos

$y = \hat{y} + \hat{e} = x\beta + \hat{e}$ con un $\beta$ que minimiza  


$\lvert\lvert\hat{e}\rvert\rvert_{mco}=\sum_{i=1}^{n}\hat{e_i}^2=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2=\sum_{i=1}^{n}(y_i-x_i\beta)^2$


MDA: minimiza la suma de desviaciones absolutas

 $\lvert\lvert\hat{e}\rvert\rvert_{mad}=\sum_{i=1}^{n}\lvert\hat{e_i}\rvert=\sum_{i=1}^{n}\lvert y_i-\hat{y}_i\rvert$


5. La geometría que subyace en el MCO es la euclidiana: el mundo con el que estamos familiarizados. En él, hay correspondencias muy útiles entre conceptos matemáticos e ideas estadísticas. En cambio, la geometría del MAD es menos intuitiva y sacrifica estas correspondencias.

6. Empecemos desde el principio: ambos métodos minimizan una función de los errores. Veremos que eso es lo mismo que minimizar una distancia entre el vector de valores estimados y el de observados.

7. MCO usa la distancia euclidiana y MAD usa la distancia Manhattan. Con la distancia euclidiana, la distancia entre dos puntos es la hipotenusa trazada por la resta de cada coordenada: ¡Pitágoras! Los puntos equidistantes a otro forman círculos concéntricos, nuestra idea usual de distancia.

<img src="images/Distancia-euclides.png" width="50%">

<img src="images/Euclidiana.png" width="50%">

8. La Manhattan, por su parte, es la suma de las diferencias absolutas de cada coordenada. Eso implica que los puntos equidistantes forman rombos en lugar de círculos: ¡rarísimo!

<img src="images/Manhattan.png" width="50%">

7. Dando un paso más, la distancia entre un punto 𝑌 y una recta es la mínima entre el punto 
y todos los puntos sobre la recta. Noten que aquí estamos hablando de una minimización, y veremos que estimar linealmente es algo muy similar a esto. La diferencia está en la métrica: euclidiana -> Pe, Manhattan -> Pm.

<img src="images/Comaparacion2.png" width="50%">

8. Con la distancia euclidiana, el punto más cercano 𝑃𝑒​ está sobre 
el círculo más pequeño, mientras que con la Manhattan, el punto más cercano 
𝑃𝑚 está sobre el rombo más pequeño. 
Claramente, la distancia más "natural" es la euclidiana.

<img src="images/Comaparacion2.png" width="50%">

9. Algunas cosas lindas de un espacio euclidiano: el segmento entre Y y Pe es *perpendicular* a la recta (ángulo de 90). Pe se llama "proyección ortogonal" de Y. Es única y requiere de la idea de "ángulo", que
se define a su vez a partir del producto interior. 

Producto interior de A con B

$\mathbf{A} \cdot \mathbf{B} = \|\mathbf{A}\|\|\mathbf{B}\|\cos(\theta)$

es decir

$\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\|\|\mathbf{B}\|}$

11. Lo interesante del concepto de ángulo es que nos da una forma de medir cuán "paralelos" son dos vectores. Cuando el ángulo es cero un vector puede escribise exactamente como múltiplo del otro. Cuando el ángulo crece los vectores son cada vez menos proporcionales.

![](images/angulos.png)

12. Los vectores perpendiculares son lineamente todo lo distintos que pueden ser. En ese caso, su producto interior, que en un espacio euclidio puede definirse como la suma del producto de dos vectores componente a componente, se anula. 

13. Una desventaja de la distancia Manhattan es que no es compatible con ninguna definición de producto interior, lo que impide la definición de ángulos o proyecciones ortogonales. Además, puede haber más de un punto en una recta que minimice la distancia a otro punto.

14. ¿Qué tiene que ver todo esto con la regresión lineal? ¡Todo! Para verlo gráficamente, consideremos el MCO con una sola variable y y un regresor x, sin intercepto. Tomemos dos observaciones: para x=1 se observó y=2 y para x=2, y=5

$y=\beta x + e$ 

$y=(y_1, y_2)=(2,5)$ 

$x=(x_1, x_2)=(1,2)$

15. Lo bueno de este modelo de juguete es que podemos representarlo en 2D igual que antes: en las abcisas pondremos la primera observación y en las ordenadas la segunda. Entonces y es el vector (2,5), y beta * x genera una recta desde el origen que pasa por x=(1,2).

<img src="images/MCO-step1.png" width="50%">

16. La recta es el espacio que representa los puntos "barridos" por x con cada valor de beta. Si lo miramos fijo descubrimos que estimar no es sino *minimizar* la distancia entre esa recta e y: un problema geométrico! Y que entonces puede
abordarse con distintas geometrías subyacentes.

<img src="images/MCO-step2.png" width="50%">

17. Como decíamos el MCO usa la distancia de todos los días: la estimación se obtiene trazando la perpendicular de Y a la recta (proyección ortogonal). En este ejemplo da (2,4, 4,8). La perpendicular es el vector de errores e=(2-2.4, 5-4,8)=(-0,4, 0,2). El beta es 2,4 ya que 2,4 * (1, 2) = (2,4, 4,8)

<img src="images/MCO-step3.png" width="50%">

18. Como es de esperar, el producto interior entre el vector de errores y la estimación es cero, ya que los vectores son perpendiculares. (-0,4 * 2.4)  + (0,2 * 4,8) = 0. 

<img src="images/MCO-step4.png" width="50%">

19. El MAD usa la distancia Mahattan y por lo tanto el y estimado, el punto más cercano es distinto (2,5, 5). También el beta es distinto. Pero el error ya no es ortogonal (ni siquiera podemos definir el concepto, por motivos que escapan a este post). 

<img src="images/MCO-step5.png" width="50%">

20. Este ejemplo es fácilmente representable en 2D, pero con más observaciones y regresores no se puede visualizar directamente. Sin embargo, la interpretación geométrica sigue siendo la misma. De ahí que en el MCO aparezca la "matriz de proyección".

$\hat{y}=X\hat\beta = X(X^tX)^{-1}X^ty=Py$
donde P es la matriz de proyección 
de y en el espacio barrido por X.


21. Podemos incluso generalizar de espacios vectoriales en Rn (n datos) a variables aleatorias 
(funciones). En lugar de distancia euclidiana vs. manhattan tendremos 
espacios de Hilbert (e.g. norma L2) vs. espacios de Banach (e.g. norma L1)
