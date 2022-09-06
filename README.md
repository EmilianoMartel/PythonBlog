# PythonBlog

Cinefans es una web creada en Django para el proyecto final del curso de Python de Coderhouse. Se puede acceder a ella [aquí](http://anselminie.pythonanywhere.com/)

Está inspirada en Letterboxd. La idea de la web es cargar series, películas o cortos. A esos contenidos se les pueden generar opiniones y asociarlos a plataformas de streaming.
De esta manera podríamos buscar una película y ver que críticas tiene y en que plataforma está disponible.

Desde la NavBar se accede a la mayoría de las vistas que están generadas, pero para borrar contenido o plataformas hay que hacerlo desde la tarjeta del objeto en sí.

## Funcionamiento
La web cuenta con dos apps: **_products_** y **_users_**. La mayor parte de las vistas funcionan sin estar logueado. Pero para borrar elementos hay que estar logueado. Los botones de borrar están escondidos en el front y no todas las vistas requieren que el usuario esté logueado mediante decoradores, ya que no investigamos como se podía hacer esto en vistas basadas en clase. Usamos estas vistas por practicidad, ya que tuvimos conflictos con las relaciones entre tablas(modelos) que seteamos cuando hicimos las vistas en modo _python puro_ al usar los métodos save() y terminamos usando las vistas de clases que funcionaron perfecto con poca configuración. Esto es un punto a mejorar, ya que la seguridad no debería estar solo en el front sino bloqueada desde el backend.

### Users
El módulo de usuarios es bastante básico. La única diferencia con el estándar de Django es que cada usuario puede setear su imagen de perfil y sus contenidos favoritos (por ahora solo desde la configuración del perfil, aunque lo ideal sería editar esta relación desde un botón en la lista de contenidos).
La imagen de perfil se muestra en la NavBar si el user está logueado.

### Products
Este es el módulo de contenidos (pero comenzamos haciendo un ecommerce). Aquí tenemos tres modelos: Contenidos, Plataformas de streaming y Reseñas.
- Los contenidos son películas o series. Se clasifican con un choicefield y las imágenes no se guardan en un servidor sino que se invoca una URL externa. Esto es porque lo hicimos antes de ver como manejar imágenes y porque teníamos la idea de hacer una carga masiva de datos con un dataset de IMDB que fue scrappeada por falta de tiempo.
- Los servicios de streaming tienen una relación many to many con contenidos para poder cargarles cuales tienen en catálogo.
- Las reseñas tienen una relación one to many con los contenidos para que los usuarios carguen sus calificaciones y (esto no fue implementado) se pueda mostrar para cada película el puntaje que obtuvo de usuarios y contrastarlo con el de la base (que sería el de IMDB). Tampoco tiene implementado un registro de que usuario la cargó y un límite de 1 reseña por contenido por usuario, para que no puedan spammear.

### Créditos
El trabajo fue realizado por Emiliano Anselmini y Emiliano Martel sin un criterio de repartir funciones muy estricto, ambos hicimos [de todo](https://github.com/Coquito38/PythonBlog/graphs/contributors)
