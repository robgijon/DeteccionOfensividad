### Descripción detallada

Consiste en el estudio, diseño y desarrollo de un sistema de detección de ofensividad que reciba como entrada un texto y que devuelva como salida la clase que el sistema haya obtenido de acuerdo a una escala basada en dos valores: ofensivo y no ofensivo.

Para probar la validez del sistema se utilizará el corpus OffendES, que está formado por comentarios escritos en español extraídos de tres redes sociales: Twitter, Youtube e Instagram.

Este corpus se ha dividido en dos conjuntos de datos: train (para entrenar el sistema) y test (para evaluar el sistema).

A la hora de realizar el clasificador de comentarios en cuanto a lenguaje ofensivo, lo he hecho mediante aprendizaje supervisado. 

Para ello he entrenado el algoritmo con los comentarios como documentos a clasificar y la columna de label como los tags (etiquetas) del fichero train.tsv., y usando este modelo, he clasificado los comentarios del fichero test.tsv. 

El resultado de esta clasificación se ve reflejada en el fichero prediction_test.tsv.
