# Un par de aspectos sobre la geometría de los mínimos cuadrados

1. Siempre me extrañó que la primera opción para los modelos de regresión fuese minimizar errores cuadráticos y no absolutos. ¿Por qué esa elección? Hay muchos motivos, y algunos mucha sofisticados. Pero el que más me gusta a mí es de índole geométrico: la forma en que medimos las distancias ¡Veamos!

$Y = X\beta + \epsilon$ con $\beta=(X^tX)^{-1}X^tY$

2. El método de mínimos cuadrados ordinarios (MCO) minimiza los errores cuadráticos. En cambio el método de Mínimas Desviaciones Absolutas (MAD) minimiza, como dice su nombre, los errores absolutos.

MCO: minimiza la suma de errores cuadráticos

$y = \hat{y} + \hat{e} = x\beta + \hat{e}$ con un $\beta$ que minimiza  

$\lvert\lvert\hat{e}\rvert\rvert_{mco}=\sum_{i=1}^{n}\hat{e_i}^2=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2=\sum_{i=1}^{n}(y_i-x_i\beta)^2$

MDA: minimiza la suma de desviaciones absolutas

 $\lvert\lvert\hat{e}\rvert\rvert_{mad}=\sum_{i=1}^{n}\lvert\hat{e_i}\rvert=\sum_{i=1}^{n}\lvert y_i-\hat{y}_i\rvert$

3. La diferencia entre ambos métodos puede interpretarse en términos de la geometría que suponen: la geometría del MCO es la euclidiana, el mundo con el que estamos familiarizados, y en el que ciertas correspondencias entre conceptos matemáticos e ideas estadísticas funcionan muy bien.

4. La geometría del MAD es mucho más "fea", implica sacrificar esas correspondencias. Empecemos por el principio: ambos métodos minimizan una función de los errores (la diferencia entre valores estimados y observados). Veremos que esto es la *distancia* entre el vector de valores estimados y el de los observados

5. MCO usa la distancia euclidiana y MAD la Manhattan. En un plano la distancia entre dos puntos es la hipotenusa trazada por la resta de cada coordenada: ¡es el mundo de Pitágoras!. Los puntos equidistantes a otro forman cículos concéntricos: nuestra idea usual de distancia

![](images/Euclidiana.png)


6. La Manhattan es la suma de las diferencias de cada coordenada. Eso implica que los puntos equidistantes forman rombos en lugar de círculos: rarísimo!

![](images/Manhattan.png)

8. La distancia entre un punto (Y) y una recta es la mínima entre Y con cada punto sobre la recta. Y acá la primera clave: el punto que minimiza la distancia depende de la distancia usemos! Con la euclidiana el punto es Pe, con Manhattan Pm. 

![](images/Comaparacion2.png)

9. Notemos que con la euclidiana Pm está más lejos que Pe porque se ubica sobre un círculo mayor. Pero más cerca con 
Manhattan porque está en un rombo más chico. Parece claro que la euclidiana es la que todos tenemos en mente cuando hablamos de distancia cotidianamente.

![](images/Comaparacion2.png)

10. Noten que el segmento entre Y y Pe es perpendicular a la recta (ángulo de 90): Pe es la "proyección ortogonal" de Y. La idea de ángulo es otra noción clave y se asocia a un producto interior. La forma en que se define este producto *también* depende de cómo medimos la distancia

Producto interior de A con B

$\mathbf{A} \cdot \mathbf{B} = \|\mathbf{A}\|\|\mathbf{B}\|\cos(\theta)$

es decir

$\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\|\|\mathbf{B}\|}$


11. Lo interesante del concepto de ángulo (o de producto interno) es que nos da una forma de medir cuán "paralelo" es un vector respecto a otro. Cuándo el ángulo es cero, un vector puede escribise como múltiplo de otro. Y si el ángulo es mayor, se hacen cada vez menos "parecidos"

![](images/angulos.png)

12. ACA Dentro de la geometría euclidiana el producto interior puede escribirse muy fácilmente. Sin embargo, no es posible tener un producto interno compatible con la distancia de Manhattan, y por lo tanto en ese caso no tenemos la idea de ángulo. (motivos dificiles)


11. Dirán: qué tiene que ver todo esto con una regresión lineal? Resulta que todo! Para verlo bien consideremos como es el MCO cuando solamente hay una variable (y), un regresor (x) sin intercepto. Tomemos además dos observaciones: para x=1 se observó y=2 y para x=2, y=5

$y=\beta x + e$ 

$y=(y_1, y_2)=(2,5)$ 

$x=(x_1, x_2)=(1,2)$

11. La ventaja de este modelo de juguete es que podemos representarlo exactamente igual que a los ejemplos: en las ordenadas va la primera observación y en las abcisas la segunda. Entonces y es el punto (2,5), y beta * x forma una recta desde el origen que pasa por x=(1,2).

![](images/MCO-step1.png)

12. La recta es el espacio de los puntos barridos por x con distintos beta. Estimar es buscar el punto de esa recta más cercano a Y. Es lo mismo que encontrar un beta que multiplique a (1,2) dando el punto más cercano a (2,5). Y como hablamos de cercanía hay que elegir una distancia!

13. MCO usa la distancia de todos los días: la perpendicular de Y a la recta da la estimacion: proyección ortogonal de Y sobre la recta. El segmento perpendicular es el vector de errores e=(2-2.4, 5-4,8)=(-0,4, 0,2). Y el beta es lógicamente 2,4 ya que 2,4 * (1, 2) = (2,4, 4,8)

![](images/MCO-step2.png)

14. Como dijimos, en el mundo euclidiano el ángulo es función del producto interior, definido como suma de productos de los componentes de cada vector. El ángulo es recto cuando este último se anula. Con MCO el vector de errores es perpendicular a la recta y por eso (-0,4 * 2.4)  + (0,2 * 4,8) = 0

![](images/MCO1.png)

15. Comparado, el MAD usa la distancia Mahattan y por lo tanto el y estimado, el punto más cercano de la recta by al punto y, es distinto. Por este motivo, el B es también distinto. El error ya no es ortogonal, porque Yestimado no es una proyección. De hecho, no hay un producto interior compatible y por ende ni siquiera es posible definir la covarianza de dos vectores.

![](images/MCO2.png)

16. Este ejemplo con dos variables se puede generalizar en muchos niveles. Con más regresores, con más observaciones, la idea es exactamente la misma. más aún, si en lugar de tomar vectores de puntos tomamos variables aleatorias la geometría se generaliza. Para eso en lugar de espacios euclidianos hay que usar espacios de Hilbert. 

17. Los conceptos son los mismos: distancia, producto interior