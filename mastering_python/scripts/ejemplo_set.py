"""
Supongamos que temenos dos listas.
    :current_users    :los usuarios actuales en el grupo
    :new_users        :la nueva lista de usuarios del grupo

En los sistemas de permisos un escenario muy común es agregar o eliminar
usuarios de un grupo masivamente. Dentro de muchas bases de datos de
permisos no es fácil establecer la lista completa a la vez, por lo que
se necesita una lista para insertar y una para eliminar. Aquí es donde
un set es útil.
"""

# La función set() toma como argumento una secuencia, por eso es necesario
# el doble parentesis.

current_users = set(('a', 'b', 'd'))
new_users = set(('b', 'c', 'd', 'e'))

to_insert = new_users - current_users
print('Para insertar', sorted(to_insert))

to_delete = current_users - new_users
print('Para eliminar', sorted(to_delete))

# Sin cambios
unchanged = new_users & current_users
print('Sin cambios', sorted(unchanged))

# Notece que se usa la función sorted() para que la impresión sea consistente,
# ya que como los dict, los set no tiene un orden predefinido.
