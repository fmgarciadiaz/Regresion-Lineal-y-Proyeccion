# Un par de aspectos sobre la geometría de los mínimos cuadrados

1. Siempre me extrañó que la primera opción para los modelos de regresión fuese minimizar errores cuadráticos y no absolutos. Sin embargo hay muchos motivos, algunos muy sofisticados. El que más me gusta es geométrico: la forma en que medimos largos, distancias y ángulos

$Y = X\beta + \epsilon$ con $\beta=(X^tX)^{-1}X^tY$

2. El método de mínimos cuadrados ordinarios (MCO) minimiza los errores cuadráticos. En cambio el método de Mínimas Desviaciones Absolutas (MAD) minimiza los errores absolutos. La diferencia entre ambos puede interpretarse en términos de la geometría que suponen

MCO: minimiza la suma de errores cuadráticos

$y = \hat{y} + \hat{e} = x\beta + \hat{e}$ con un $\beta$ que minimiza  

$\lvert\lvert\hat{e}\rvert\rvert_{mco}=\sum_{i=1}^{n}\hat{e_i}^2=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2=\sum_{i=1}^{n}(y_i-x_i\beta)^2$

MDA: minimiza la suma de desviaciones absolutas

 $\lvert\lvert\hat{e}\rvert\rvert_{mad}=\sum_{i=1}^{n}\lvert\hat{e_i}\rvert=\sum_{i=1}^{n}\lvert y_i-\hat{y}_i\rvert$

3. La geometría que subyace en el MCO es la euclidiana: el mundo con el que estamos familiarizados. En él hay  correspondencias muy útiles entre conceptos matemáticos e ideas estadísticas. La geometría que supone el MAD es mucho más "fea" y sacrifica esas correspondencias. 

4. Empecemos por el principio: ambos minimizan una función de los errores. Veremos que eso es lo mismo que minimizar una *distancia* entre el vector de valores estimados y el de observados.

5. MCO usa la distancia euclidiana y MAD la Manhattan. Con la primera, la distancia entre dos puntos es la hipotenusa trazada por la resta de cada coordenada: Pitágoras!. Los puntos equidistantes a otro forman cículos concéntricos: nuestra idea usual de distancia

<img src="images/Distancia-euclides.png" width="50%">

<img src="images/Euclidiana.png" width="50%">

6. La Manhattan es la suma de las diferencias de cada coordenada. Eso implica que los puntos equidistantes forman rombos en lugar de círculos: rarísimo!

<img src="images/Manhattan.png" width="50%">

7. Dado un paso más, la distancia entre un punto Y y una recta es la mínima con cada punto sobre la recta. Noten que acá aparece una minimización, y veremos que estimar linealmente es algo muy parecido a esto. Noten que el punto mínimo depende de la métrica: euclidiana -> Pe, Manhattan -> Pm!

<img src="images/Comaparacion2.png" width="50%">

8. Con la distancia euclidiana Pm está más lejos que Pe porque se ubica sobre un *círculo mayor*. Pero más cerca con la Manhattan porque está en un *rombo más chico*. Claramente la distancia más "natural" es la euclidiana

<img src="images/Comaparacion2.png" width="50%">

9. Algunas cosas lindas de un espacio euclidiano: el segmento entre Y y Pe es *perpendicular* a la recta (ángulo de 90). Pe se llama "proyección ortogonal" de Y. Es única y requiere de la idea de "ángulo", que
se define a su vez a partir del producto interior. 

Producto interior de A con B

$\mathbf{A} \cdot \mathbf{B} = \|\mathbf{A}\|\|\mathbf{B}\|\cos(\theta)$

es decir

$\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\|\|\mathbf{B}\|}$

11. Lo interesante del concepto de ángulo es que nos da una forma de medir cuán "paralelos" son dos vectores. Cuando el ángulo es cero un vector puede escribise exactamente como múltiplo del otro. Cuando el ángulo crece los vectores son cada vez menos proporcionales.

![](images/angulos.png)

12. Los vectores perpendiculares son lineamente todo lo distinto que pueden ser. En ese caso, su producto interior, 
que en un espacio euclidio puede definirse como la suma del producto de dos vectores componente a componente, 
se anula. 

13. Una "desventaja" de la distancia Manhattan es que no es compatible 
con ninguna definición de producto interno. Tampoco podemos definirle ángulos, ni proyecciones ortogonales. 
Para colmo, puede haber más de un punto en una recta que minimice la distancia a otro punto.

14. Dirán: qué tiene que ver todo esto con una regresión lineal? Todo! Para verlo gráficamente consideremos el MCO con una sola variable (y) y un regresor (x), sin intercepto. Tomemos dos observaciones: para x=1 se observó y=2 y para x=2, y=5

$y=\beta x + e$ 

$y=(y_1, y_2)=(2,5)$ 

$x=(x_1, x_2)=(1,2)$

15. Lo bueno de este modelo de juguete es que podemos representarlo exactamente igual que antes: en las abcisas pongamos la primera observación y en las ordenadas la segunda. Entonces y es el vector (2,5), y beta * x genera una recta desde el origen que pasa por x=(1,2).

<img src="images/MCO-step1.png" width="50%">

16. La recta es el espacio que representa los puntos "barridos" por x con cada beta. Si lo miramos fijo descubrimos que estimar no es sino *minimizar* la distancia entre esa recta e y: un problema geométrico! Y que entonces puede
abordarse con distintas geometrías subyacentes.

<img src="images/MCO-step2.png" width="50%">

17. Como decíamos el MCO usa la distancia de todos los días: nuestra estimación se obtiene trazando la perpendicular de Y a la recta (proyección ortogonal de Y). En este ejemplo da (2,4, 4,8). La perpendicular es el vector de errores e=(2-2.4, 5-4,8)=(-0,4, 0,2). El beta es 2,4 ya que 2,4 * (1, 2) = (2,4, 4,8)

<img src="images/MCO-step3.png" width="50%">

18. El producto interior euclidiano entre el vector de errores y la estimación se anula, porque su ángulo es de 90 grados: efectivamente (-0,4 * 2.4)  + (0,2 * 4,8) = 0. 

<img src="images/MCO-step4.png" width="50%">

19. Comparado, el MAD usa la distancia Mahattan y por lo tanto el y estimado, el punto más cercano de la recta al punto y, es distinto. También el beta es distinto. Pero el error ya no es ortogonal (ni siquiera podemos definir el concepto, por motivos que escapan a este post). 

<img src="images/MCO-step5.png" width="50%">

20. Este ejemplo se puede generalizar en muchos niveles. Con más observaciones y regresores
ya no se puede representar visualmente pero la interpretación geomética sigue siendo válida.
Por eso en el MCO aparece la matriz de proyección:



21. Podemos incluso generalizar espacios vectores (de datos) a variables aleatorias 
(funciones) y en lugar de distancia euclidiana vs. manhattan tendremos 
espacios de Hilbert (e.g. norma L2) vs. espacios de Banach (e.g. norma L1)