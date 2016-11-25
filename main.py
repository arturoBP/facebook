from face import user
usuario = user()

print(type(usuario))

print("nombre del usuario")


respuesta = usuario.obtenerinformacion()
print(usuario.nombre)
print("respuesta")

print(type(respuesta))
coment = usuario.publicarComentario(input("comentario"))
print(coment)