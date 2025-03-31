# Un par de aspectos sobre la geometría de los mínimos cuadrados

1. Siempre me intrigó que la primera opción para los modelos de regresión fuese minimizar los errores cuadráticos y no los absolutos. ¿Por qué la preferencia? ¿No es más lógico usar los errores absolutos?

$Y = X\beta + \epsilon$ con $\beta=(X^tX)^{-1}X^tY$

2. Aunque ambas alternativas son perfectamente válidas, hay motivos para preferir la primera, salvo en ocasiones especiales (e.g con valores atípicos). Algunos motivos son muy sofisticados, pero aquí quiero hacer foco en algo que siempre me resultó atrapante: la intuición geométrica

3. Definir la función que minimizamos es más que algo simplemente operativo: en realidad, estamos adoptando una estructura para el espacio con el que modelizaremos nuestros datos e inferencias: la forma en que medimos largos, distancias y ángulos.


<img src="images/abstracto.png" width="50%">


4. Y en líneas generales, la estructura supuesta por la minimización de los errores cuadráticos se adapta más "armónicamente" a esa modelización que la de los errores absolutos.


5. Adelantando el final: elegir mínimos cuadrados ordinarios (MCO) es 
usar la geometría de los espacios euclidianos, mientras que el 
método de Mínimas Desviaciones Absolutas (MAD) se asocia a una geometría mucho más "rara" (la "del taxista") ¿Qué es cada cosa? ->


<img src="images/taxista.png" width="50%">


6. Un espacio euclidiano es un espacio vectorial dotado de un producto interno, del cual se deriva una norma (como medimos el largo de los vectores) y de ésta una métrica (como medimos las distancias). Estos elementos permiten también definir la noción fundamental de ángulo.

**Espacios euclidianos de *n* dimensiones**

**Producto interior**

$\langle x,y \rangle=\sum_1^{n}{x_iy_i}$

**Norma** inducida por el producto interior

$\|x\| = \langle x,x \rangle^{1/2}=(\sum_1^{n}{x_i^2})^{1/2}$

**Ángulo**

$\cos(\theta_{xy}) = \frac{\langle x,y \rangle}{\|\mathbf{x}\|\|\mathbf{y}\|}$

7. En los espacios euclidianos se cumple el teorema de Pitágoras.
La distancia entre dos vectores se define como la norma de su diferencia. Esto
no es sino una forma difícil de decir que es la distancia que usamos todos los días! 

$d_{eu}=\lvert \lvert{x-y}\lvert \lvert= 
\langle x-y,x-y \rangle^{1/2}=(\sum_1^{n}{(x_i-y_i)^2})^{1/2}$


8. Con esta métrica puntos equidistantes a otro forman círculos concéntricos y su distancia es la raíz de la suma cuadrática de la diferencia de sus componentes (Pitágoras!) 

<img src="images/Distancia-euclides.png" width="50%">
<img src="images/Euclidiana.png" width="50%">

9. En cambio la distancia manhattan (como veremos, asociada al MAD) es la suma de la diferencia absoluta de los componentes. En este caso los puntos equidistantes forman rombos (horrible!). Eso cambia sustancialmente la geometría del espacio.

$d_{man}=\lvert \lvert{x-y}\lvert \lvert= 
\sum_1^{n}{|x_i-y_i|}$


<img src="images/Manhattan.png" width="50%">


10. Dando un paso más, comparemos ahora la distancia entre un punto (Y) y una recta en cada geometría. Debemos encontrar el punto sobre la recta con menor distancia a Y. Es decir, tenemos que buscar un beta que minimice la distancia en cada caso (ver imagen)

Caso **euclidiano**

$argmin \space \beta: \space \lvert \lvert{x\beta-y}\lvert \lvert=
(\sum_1^{n}{(x_i\beta-y_i)^2})^{1/2}$

Caso **manhattan**

$argmin \space \beta: \space \lvert \lvert{x\beta-y}\lvert \lvert= 
\sum_1^{n}{|x_i\beta-y_i|}$


11. Nota para más adelante: minimizar la raíz cuadrada de una función positiva da lo mismo que minimizar directamente la función (la raíz es monótona creciente en dicho caso). Es decir, el problema euclidiano es el mismo si minimizamos directamente las diferencias cuadráticas.

$argmin \space \beta: \space \lvert \lvert{x\beta-y}\lvert \lvert=
(\sum_1^{n}{(x_i\beta-y_i)^2})^{1/2}$ 

es equivalente a 

$argmin \space \beta: \space \lvert \lvert{x\beta-y}\lvert \lvert=
\sum_1^{n}{(x_i\beta-y_i)^2}$ 



12. Los resultados de esta minimización difieren con cada métrica (tanto en la distancia como en el punto de mínima distnacia). Con la euclidiana el punto más cercano (Pe) está sobre el círculo tangente, mientras que con manhattan (Pm), está sobre el rombo tangente 

<img src="images/Comaparacion2.png" width="50%">


12. El punto Pe luce más "natural" porque como dijimos, minimiza la distancia
euclidiana que es la que "usamos" todos los días. En este caso el segmento entre Y y Pe es *perpendicular* a la recta.

13. En este caso Pe es la llamada "proyección ortogonal" del punto Y sobre la recta. La perpendicularidad requiere de la idea de "ángulo", que se define a partir de las estructuras que mencionamos: producto interior y norma

Producto interior de A con B

$\mathbf{A} \cdot \mathbf{B} = \|\mathbf{A}\|\|\mathbf{B}\|\cos(\theta)$

es decir

$\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\|\|\mathbf{B}\|}$

14. Lo interesante del concepto de ángulo es que permite medir cuán "paralelos" son dos vectores. Cuando el ángulo es cero un vector puede escribise exactamente como múltiplo del otro. Cuando el ángulo crece los vectores son cada vez "menos proporcionales". 

![](images/angulos.png)

15. La idea de correlación lineal depende crucialmente de la de ángulo. Los vectores perpendiculares son (lineamente) todo lo diferentes que pueden ser: aquí se anula el producto interior (en un espacio euclidio se define como la suma del producto componente a componente) 


16. Una gran desventaja de la distancia manhattan es que no es posible insertarla en una estructura geométrica semejante. No hay producto interior compatible, por lo que no tenemos ángulos ni proyecciones ortogonales. Peor aún, los puntos de mínima distancia pueden no ser únicos!


<img src="images/Manhattan2.png" width="50%">


14. ¿Qué tiene que ver todo esto con la regresión lineal? ¡Todo! Recapitulemos. El  (MCO) minimiza los errores cuadráticos. El método de Mínimas Desviaciones Absolutas (MAD) minimiza los errores absolutos. El primero es compatible con el mundo euclidiano, el segundo es algo muy diferente

**MCO:** minimiza la suma de *errores cuadráticos*

$y = \hat{y} + \hat{e} = x\beta + \hat{e}$ con un $\beta$ que minimiza  


$\lvert\lvert\hat{e}\rvert\rvert_{mco}=\sum_{i=1}^{n}\hat{e_i}^2=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2=\sum_{i=1}^{n}(y_i-x_i\beta)^2=\sum_{i=1}^{n}(x_i\beta-y_i)^2$


**MAD:** minimiza la suma de *desviaciones absolutas*

 $\lvert\lvert\hat{e}\rvert\rvert_{mad}=\sum_{i=1}^{n}\lvert\hat{e_i}\rvert=\sum_{i=1}^{n}\lvert y_i-\hat{y}_i\rvert=\sum_{i=1}^{n}\lvert \hat{y}_i-y_i\rvert$


15. La similitud formal de estas minimizaciones con la distancia de un punto a una recta (que vimos antes) no es casual. ¡Es que se trata esencialmente de lo mismo!

16. Para visualizar este hecho consideremos la regresión de una variable (y) con un regresor (x), sin intercepto. Para el ejemplo tomemos dos observaciones: para x=1 se observó y=2 y para x=2, y=5

$y=\beta x + e$ 

$y=(y_1, y_2)=(2,5)$ 

$x=(x_1, x_2)=(1,2)$


16. Lo bueno de este ejemplo de juguete es que podemos representarlo en 2D igual que antes: en las abcisas ubicaremos la primera observación y en las ordenadas la segunda. Entonces y es el vector (2,5), y beta * x genera una recta desde el origen que pasa por x=(1,2).

<img src="images/MCO-step1.png" width="50%">

17. La recta es el espacio que representa los puntos "barridos" por el vector x con cada valor de beta. Si lo miramos fijo descubrimos lo mencionado:  estimar linealmente es minimizar la distancia entre la recta e y. Y la solución varía con la geometría que estemos suponiendo.

<img src="images/MCO-step2.png" width="50%">


17. Como dijimos, MCO usa la distancia euclidiana: hay que trazar una perpendicular a la recta que pasa por Y (proyección ortogonal). En este ejemplo eso da Ymc = (2,4, 4,8). El vector de errores es 
e=(2-2.4, 5-4,8)=(-0,4, 0,2). El beta es 2,4 ya que 2,4 * (1, 2) = (2,4, 4,8)

<img src="images/MCO-step3.png" width="50%">

18. El vector de errores es perpendicular a la recta y, efectivamente,pel producto interior se anula (-0,4 * 2.4)  + (0,2 * 4,8) = 0. 

<img src="images/MCO-step4.png" width="50%">

19. En cambio el MAD usa la distancia mahattan; la estimación (y el beta) es diferente Yad = (2,5, 5).  El error ya no es ortogonal (no hay proyección ortogonal). Como no hay idea de ángulo, no existe medida de correlación lineal (hay que utilizar otros instrumentos, más complicados) 

<img src="images/MCO-step5.png" width="50%">

20. En suma, la geometría del MCO se presta mejor que la del MAD para definir conceptos fundamentales de la modelización estadística. La navaja de Ockham favorece al MCO, excepto en ciertos casos en los que los beneficios del MAD superan sus costos.

21. Con más observaciones y regresores se hace imposible hacer una representación visual sencilla . Sin embargo, la interpretación geométrica sigue siendo la misma. Por eso el operador para estimar con el MCO se llama "matriz de proyección" 


$\hat{y}=X\hat\beta = X(X^tX)^{-1}X^ty=Py$

donde $P$ es la *matriz de proyección* 
de $y$ en el espacio generado por $X$.


21. Esta interpretación se puede extender de espacios de vectores de datos (el MCO más elemental) a variables aleatorias. En dicho caso hay que pensar en espacios de funciones (las variables aleatorias son funciones medibles), pero *maravillosamente* la geometría es la misma.

22. Los espacios euclidianos pasan a ser espacios de Hilbert (con norma L2) y la distancia Manhattan a espacios de Banach (con norma L1). Y los espacios de Hilbert mantienen su ventaja en simplicidad sobre los demás porque tienen producto interior, ángulos y proyecciones ortogonales 


24. Bonus track: los espacios de Hilbert (y su geometría) unifican campos de estudio tan diversos como la i) probabilidad, la estadística y la econometría (la proyección ortogonal es la base para definir la varianza, la covarianza/correlación, la esperanza condicional, etc.)

25. ii) La física cuántica (los estados cuánticos son elementos de un espacio de Hilbert y las amplitudes de probabilidad de transicionar de un estado a otro están dadas por el producto interno entre ambos)

26. iii) El análisis espectral (análisis de Fourier) de una onda (o de un proceso estocástico) también es la proyección de una función sobre la "base" formada por las exponenciales complejas (o sobre senos y cosenos).