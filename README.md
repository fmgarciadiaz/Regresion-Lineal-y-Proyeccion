# Un par de aspectos sobre la geometría de los mínimos cuadrados

1. Siempre me intrigó que la primera opción para los modelos de regresión fuese minimizar los errores cuadráticos y no los absolutos. ¿Por qué la preferencia? ¿No es más lógico usar los errores absolutos?

$Y = X\beta + \epsilon$ con $\beta=(X^tX)^{-1}X^tY$

2. Aunque ambas alternativas son válidas hay motivos profundos para preferir la primera, salvo condiciones específicas (e.g. con valores atípicos). Algunos son muy sofisticados, pero hoy quiero hacer foco en algo que siempre me pareció súper atrapante: la intuición geométrica

3. Definir la función que minimizamos es más que algo operativo.
En realidad, implícitamente estamos adoptando una métrica, una forma de medir distancias. Y ello se vincula también al modo en que medimos largos y ángulos (que dependen del produto interior y la norma) 

4. Es decir, estamos adoptando una estructura que abstrae el espacio
en el que vivirán nuestros modelos. Veremos que la estructura supuesta por 
la minimización de errores cuadráticos se adapta más armónicamente
que la de los errores absolutos.

5. Adelantando el final: elegir mínimos cuadrados ordinarios (MCO) es 
usar la geometría de los espacios euclidianos, mientras que el 
método de Mínimas Desviaciones Absolutas (MAD) se asocia a una geometría mucho
más "rara" (a veces llamada "del taxista") ¿qué es cada cosa?

6. Un espacio euclidiano es un espacio vectorial dotado de un producto interno, del cual se deriva una norma (como medimos largo de vectores) y de ésta una métrica (como medimos distancias). Estos elementos permiten también definir la noción fundamental de ángulo.

Espacios euclidianos de n dimensiones
Producto interior

$\langle x,y \rangle=\sum_1^{n}{x_iy_i}$

Norma inducida por el producto interior

$\|x\| = \langle x,x \rangle^{1/2}=(\sum_1^{n}{x_i^2})^{1/2}$

Ángulo

$\cos(\theta_{xy}) = \frac{\langle x,y \rangle}{\|\mathbf{x}\|\|\mathbf{y}\|}$

7. Los euclidianos son espacios donde se cumple el teorema de Pitágoras.
La distancia entre dos vectores se define como la norma de su diferencia. Esto
es una forma difícil de decir que es la distancia usual que usamos todos los días! 

$d_{eu}=\lvert \lvert{x-y}\lvert \lvert= 
\langle x-y,x-y \rangle^{1/2}=(\sum_1^{n}{(x_i-y_i)^2})^{1/2}$


8. Los puntos equidistantes a otro forman círculos concéntricos y su distancia es
la raíz de la suma cuadrática de la diferencia de sus componentes (de nuevo: Pitágoras!) 

<img src="images/Distancia-euclides.png" width="50%">
<img src="images/Euclidiana.png" width="50%">

9. La distancia manhattan (que es la asociada al MAD) es la suma de la diferencia absoluta de los componentes. En este caso los puntos equidistantes forman rombos (rarísimo!). Eso cambia sustancialmente la geometría del espacio.

$d_{man}=\lvert \lvert{x-y}\lvert \lvert= 
\sum_1^{n}{|x_i-y_i|}$


<img src="images/Manhattan.png" width="50%">


10. Comparemos que pasa si queremos saber la distancia entre un punto y una recta en 
cada geometría. Debemos calcular la distancia desde el punto a cada punto sobre la recta y elegir la menor. 

$d_{eu}=\lvert \lvert{x-y}\lvert \lvert= 
\langle x-y,x-y \rangle^{1/2}=(\sum_1^{n}{(x_i-y_i)^2})^{1/2}$


$d_{man}=\lvert \lvert{x-y}\lvert \lvert= 
\sum_1^{n}{|x_i-y_i|}$




 esto involucra minimizar una distancia. 
En un caso minimizamos la raíz de la suma cuadrática de las diferencias; en el otro las
absolutas. 

<img src="images/Comaparacion2.png" width="50%">

11. Vale mencionar que minimizar la raíz cuadrada de una función positiva (como en este caso) es igual a minimizar la directamente la función (la raíz es monótona creciente en dicho caso). El problema euclidiano es el mismo si minimizamos directamente las diferencias cuadráticas

FORMULA DE MINIMOS

11. Con la distancia euclidiana el punto más cercano​ está sobre 
el círculo más pequeño, mientras que con la Manhattan, está sobre el rombo más chico. 
Es decir, cambian tanto el punto más cercano como la distancia. Claramente, 
la euclidiana luce más "natural" 

<img src="images/Comaparacion2.png" width="50%">

12. Y luce más natural porque el segmento entre Y y Pe es *perpendicular* a la recta: Pe es la "proyección ortogonal".
La perpendicularidad requiere de la idea de "ángulo", que se define a partir de las estructuras
que mencionamos: producto interior y norma;

Producto interior de A con B

$\mathbf{A} \cdot \mathbf{B} = \|\mathbf{A}\|\|\mathbf{B}\|\cos(\theta)$

es decir

$\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\|\|\mathbf{B}\|}$

13. Lo interesante del concepto de ángulo es que permite medir cuán "paralelos" son dos vectores. 
Cuando el ángulo es cero un vector puede escribise exactamente como múltiplo del otro. 
Cuando el ángulo crece los vectores son cada vez menos proporcionales.

![](images/angulos.png)

14. Los vectores perpendiculares son lineamente todo lo distintos que pueden ser: en este caso se anula el producto interior (que en un espacio euclidio se define como la suma del producto de dos vectores componente a componente). 


15. Una gran desventaja de la distancia Manhattan es que no es posible insertarla en una estructura geométrica semejante.
No hay producto interior compatible, por lo que no podemos definir
ángulos ni proyecciones ortogonales. Además los puntos de mínima distancia pueden no ser únicos


<img src="images/Manhattan2.png" width="50%">

14. ¿Qué tiene que ver todo esto con la regresión lineal? ¡Todo! Recapitulemos. El  (MCO) minimiza los errores cuadráticos. El método de Mínimas Desviaciones Absolutas (MAD) minimiza los errores absolutos. El primero es compatible con el mundo euclidiano, el segundo
es algo muy diferente

MCO: minimiza la suma de errores cuadráticos

$y = \hat{y} + \hat{e} = x\beta + \hat{e}$ con un $\beta$ que minimiza  


$\lvert\lvert\hat{e}\rvert\rvert_{mco}=\sum_{i=1}^{n}\hat{e_i}^2=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2=\sum_{i=1}^{n}(y_i-x_i\beta)^2$


MDA: minimiza la suma de desviaciones absolutas

 $\lvert\lvert\hat{e}\rvert\rvert_{mad}=\sum_{i=1}^{n}\lvert\hat{e_i}\rvert=\sum_{i=1}^{n}\lvert y_i-\hat{y}_i\rvert$


15. Para visualizar esto fácilmente consideremos una regresión con una sola variable y y un regresor x, sin intercepto. Tomemos dos observaciones: para x=1 se observó y=2 y para x=2, y=5

$y=\beta x + e$ 

$y=(y_1, y_2)=(2,5)$ 

$x=(x_1, x_2)=(1,2)$


16. Lo bueno de este ejemplo de juguete es que podemos representarlo en 2D igual que antes: en las abcisas pondremos la primera observación y en las ordenadas la segunda. Entonces y es el vector (2,5), y beta * x genera una recta desde el origen que pasa por x=(1,2).

<img src="images/MCO-step1.png" width="50%">

16. La recta es el espacio que representa los puntos "barridos" por el vector x con cada valor de beta. Si lo miramos fijo descubrimos que estimar es minimizar la distancia entre esa recta e y: el problema geométrico que mostramos antes! Su solución varía con la
geometría subyacente

<img src="images/MCO-step2.png" width="50%">


LINK A MINIMIZAR LA DISTANCIA EUCLIDIANA POR TEMA RAIZ

17. El MCO usa la distancia euclidiana: estimar es trazar la perpendicular de Y a la recta (proyección ortogonal). En este ejemplo eso da (2,4, 4,8). El vector de errores es 
e=(2-2.4, 5-4,8)=(-0,4, 0,2). El beta es 2,4 ya que 2,4 * (1, 2) = (2,4, 4,8)

<img src="images/MCO-step3.png" width="50%">

18. En esta línea, el vector de errores es perpendicular a la recta, por lo que el producto interior se anula (-0,4 * 2.4)  + (0,2 * 4,8) = 0. 

<img src="images/MCO-step4.png" width="50%">

19. En cambio el MAD usa la distancia Mahattan y por lo tanto el y estimado (el punto más cercano de la recta) es diferente (2,5, 5). También el beta es distinto. Ahora el error no es ortogonal (la estimación ya no es la proyección ortogonal)

<img src="images/MCO-step5.png" width="50%">

20. Este ejemplo es fácilmente representable en 2D, pero con más observaciones y regresores no se puede visualizar directamente. Sin embargo, la interpretación geométrica sigue siendo la misma. Por ello las estimaciones se obtienen con la llamada "matriz de proyección".

$\hat{y}=X\hat\beta = X(X^tX)^{-1}X^ty=Py$
donde P es la matriz de proyección 
de y en el espacio barrido por X.


21. Podemos generalizar esto de espacios vectoriales en Rn (n datos) a 
variables aleatorias. En dicho caso requeriremos pensar espacios de funciones. 
Los espacios euclidianos pasan a espacios de Hilbert (con norma L2) 
y la distancia Manhattan a espacios de Banach (con norma L1)

22. Los espacios de Hilbert también tienen un producto interior y cuentan con
norma, distancia, ángulos y proyecciones ortogonales, estructuras que se 
utilizan para definir la varianza, covarianza y la estimación lineal de variables
aleatorias en función de otras. 


-----



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
