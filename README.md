# Un par de aspectos sobre la geometría de los mínimos cuadrados

1. Siempre me extrañó que la primera opción para los modelos de regresión fuese minimizar errores cuadráticos y no los absolutos. Hay muchos motivos, y algunos muy sofisticados. Pero el que más me gusta a mí es de índole geométrico. Veamos!

2. El método de mínimos cuadrados ordinarios (MCO) minimiza los errores cuadráticos. El método que minimiza los desvíos absolutos es el de Mínimas Desviaciones Absolutas (MAD).

MCO: minimiza la suma de errores cuadráticos

$y = \hat{y} + \hat{e} = x\beta + \hat{e}$ con un $\beta$ que minimiza  

$\lvert\lvert\hat{e}\rvert\rvert_{mco}=\sum_{i=1}^{n}\hat{e_i}^2=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2=\sum_{i=1}^{n}(y_i-x_i\beta)^2$

MDA: minimiza la suma de desviaciones absolutas

 $\lvert\lvert\hat{e}\rvert\rvert_{mad}=\sum_{i=1}^{n}\lvert\hat{e_i}\rvert=\sum_{i=1}^{n}\lvert y_i-\hat{y}_i\rvert$

3. La diferencia entre ambos métodos puede interpretarse en términos de la geometría que suponen: la geometría del MCO es la del mundo euclidiano con el que estamos familiarizados, en el que las correspondencias entre conceptos matemáticos e ideas estadísticas funcionan muy bien.

4. La geometría del MAD es mucho más "fea" e implica sacrificar correspondencias "deseables". Empecemos por el principio: ambos métodos minimizan una función de los errores (la diferencia entre $\hat{y}$ e $y$). Esto no es sino la *distancia* entre valores estimados y los observados

5. Más adelante lo veremos mejor, pero básicamente MCO usa la distancia euclidiana mientras que MAD la de Manhattan. Ejemplifiquemos las diferencias en un plano: 

6. La euclidiana es la hipotenusa de los segmentos formados por la diferencia de las coordenadas x e y. Es Pitágoras! (imagen). Por lo tanto, los puntos que están a una misma distancia de otro punto forman cículos concéntricos. Es nuestra idea usual de distancia. 

![](images/Euclidiana.png)


7. La de Manhattan está dada por la suma de las diferencias de las coordenadas de cada punto. Notar que eso implica que los puntos a una misma distancia de otro forman rombos. No es algo que nos resulte intuitivo, pensando en como calculamos las distancias en nuestro día a día.

![](images/Manhattan.png)

8. Y la distancia entre un punto y una recta es la distancia mínima entre el punto y todos los puntos sobre la recta. La cuestión es: ¡el punto más cercano depende de la distancia que usemos! El más cercano a Y con la euclidiana es Pe. Para la otra sería Pm. ¿Cuál les gusta más?

![](images/Comaparacion2.png)

9. Ortogonalidad. en el mundo euclidiano los puntos de una recta (o de un plano, o lo que sea) más cercanos a otro punto están unidos por un segmento perndicular. Se llama proyección ortogonal. Eso no pasa en el otro caso. No es una proyección ortogonal

10. Dirán que tiene que ver un punto y una recta con el modelo de regresión lineal? Todo! Para verlo bien vamos a considerar como es el MCO cuando solamente hay un regresor, sin intercepto y dos observaciones. Esta es la clave de todo.

11. Explicar. vector y, ymc es la proyección ortogonal, errores minimizan la distancia euclidiana entre el punto y la recta generada por bx. E es ortogonal. producto interior que es la covarianza.

![](images/MCO1.png)


12. Comparado, el MAD usa la distancia Mahattan y por lo tanto el y estimado, el punto más cercano de la recta by al punto y, es distinto. Por este motivo, el B es también distinto. El error ya no es ortogonal, porque Yestimado no es una proyección. De hecho, no hay un producto interior compatible y por ende ni siquiera es posible definir la covarianza de dos vectores.

![](images/MCO2.png)

13. Este ejemplo con dos variables se puede generalizar en muchos niveles. Con más regresores, con más observaciones, la idea es exactamente la misma. más aún, si en lugar de tomar vectores de puntos tomamos variables aleatorias la geometría se generaliza. Para eso en lugar de espacios euclidianos hay que usar espacios de Hilbert. 

14. Los conceptos son los mismos: distancia, producto interior