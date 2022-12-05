# Relaciones entre clases/tablas
1. Uno a uno: oneToOneField(Clase, on_delete=models.CASCADE)
2. Uno a muchos (a través de clave foránea):      reporter = models.models.ForeignKey(Reporter, on_delete=models.CASCADE)
   1. Acceder al uno desde muchos: art1.reporter.first_name
   2. Acceder al muchos desde el 1 (con clase_set): rep1.article_set.all()
