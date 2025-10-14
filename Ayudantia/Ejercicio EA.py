class Playlist:
    total_playlist = 0 #Variable de clase
    
    def __init__ (self, usuario: str): 
        self.usuario = usuario # Atributo Publico
        self.__canciones = [] # Atributo Privado
        Playlist.total_playlist += 1 #Incrementador

    def agregar_cancion(self,nombre:str) -> None:
        if nombre != "":
            self.__canciones.append(nombre)
        else:
            print("No se puede agregar una canción sin nombre")

    def eliminar_cancion(self, nombre:str) ->None:
        if nombre in self.__canciones:
                self.__canciones.remove(nombre)
        else:
            print(f"La canción{nombre}no está en la playlist")

    def __len__(self) -> int:
        return len(self.__canciones)
    
    def __str__(self) -> str:
        return f"Playlist del usuario:{self.usuario}:{self.__canciones}"


p1 = Playlist("Ian")
p1.agregar_cancion("EoO")
p1.agregar_cancion("SATIROLOGIA")
print(p1)
print("Cantidad de canciones:", len(p1))
print("Total de playlists creadas:", Playlist.total_playlist)
