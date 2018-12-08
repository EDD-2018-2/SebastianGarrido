Python 3.7.1rc1 (v3.7.1rc1:2064bcf6ce, Sep 26 2018, 15:15:36) [MSC v.1914 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from jikanpy import Jikan
jikan = Jikan()

def main():
    if EddActual is None
        print ('Elige que estructura quiere ocupar')
        print ('1. Arbol binario')
        print ('2. AVL')
        print ('3. Arbol 2-3')

        opcion1 = imput ()
        
        if opcion1==1:
            EddActual = ArbolBinarioBusqueda()
        elif opcion1==2:
            EddActual = AVL()
        elif opcion1==3:
            EddActual = BTree()
     else:
        print ("Selecciona una opción")
        print (".1 - Insertar:")
        print (".2 - Buscar:")
        print (".3 - Eliminar")
        opcion2 = imput()
        if opcion1 == 1:
            if opcion2 == 1:
                print ('Ingrese nombre, género, puntuacion:')
                n=input()
                g=input()
                pun=input()
                EddActual.agregar(pun,n,genero)
            elif opcion2 == 2:
                print ('por favor ingresa el nombre:')
                n=input()
                EddActual.buscar(n)
            elif opcion2 == 3:
                print ('por favor ingresa nombre de Anime a eliminar:')
                n=input()
                EddActual.eliminar(n)
        if opcion1 == 2:
            if opcion2 ==1:
                print ('Ingresa nombre, género, puntuacion:')
                n=input()
                g=input()
                pun=input()
                EddActual.insert(pun,n,genero)
            elif opcion2 ==2:
                print ('Ingrese el nombre:')
                n=input()
                EddActual.search(n)
            elif opcion2 ==3:
                print ('Ingrese nombre de Anime que quiere eliminar:')
                n=input()
                delete(n)
        if opcion1 == 3:
            if opcion2==1:
                print ('Ingrese nombre,puntuacion,genero :')
                n=input()
                g=input()
                pun=input()
                EddActual.add(pun,n,genero)
            elif opcion2==2:
                print ('Ingrese el nombre:')
                n=input()
                EddActual.find(n)
            elif opcion2==3:
                print ('Ingrese nombre de Anime que quiere eliminar:')
                n=input()
                delete(n)
      
class Anime:
    def __init__(self,puntuacion,nombre,genero,izquierdo,derecho,padre):
        self.puntuacion = puntuacion
        self.cargaUtil = valor
        self.nombre = nombre
        self.genero = genero
        self.padre = None
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.height = 0


    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,puntuacion,nombre,genero,hijoizq,hijoder):
        self.puntuacion = puntuacion
        self.hijoIzquierdo = hijoizq
        self.hijoDerecho = hijoder
        self.nombre = nombre
        self.genero = genero
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self
   
 
    def right(self):
        return self.hijoDerecho

  
    def right(self, Anime):
        if Anime is not None:
            Anime.padre = self
            self.hijoDerecho = Anime

  
    def left(self):
        return self.hijoIzquierdo

    
    def left(self, Anime):
        if Anime is not None:
            Anime.padre = self
            self.hijoIzquierdo = Anime

   
    def padre(self):
        return self.padre

    
    def padre(self, Anime):
        if Anime is not None:
            self.padre = Anime
            self.height = self.padre.height + 1
        else:
            self.height = 0

class AVL:

    def __init__(self):
        self.raiz = None
        self.tamaño = 0

    def insert(self, puntuacion,nombre,genero):
        Anime = Anime(puntuacion,nombre genero)

        if self.raiz is None:
            self.raiz = Anime
            self.raiz.height = 0
            self.tamaño = 1
        else:
            Anime.padre = None
            Anime = self.raiz

            while True:
                if Anime is not None:

                    Anime.padre = Anime

                    if Anime.puntuacion < Anime.puntuacion:
                        Anime = Anime.left
                    else:
                        Anime = Anime.right
                else:
                    Anime.height = Anime.padre.height
                    Anime.padre.height += 1
                    if Anime.puntuacion < Anime.padre.puntuacion:
                        Anime.padre.left = Anime
                    else:
                        Anime.padre.right = Anime
                    self.rebalance(Anime)
                    self.tamano += 1
                    break

    def rebalance(self, Anime):
        n = Anime

        while n is not None:
            heighthijoDerecho = n.height
            heighthijoIzquierdo = n.height

            if n.right is not None:
                heighthijoDerecho = n.right.height

            if n.left is not None:
                heighthijoIzquierdo = n.left.height

            if abs(heighthijoIzquierdo - heighthijoDerecho) > 1:
                if heighthijoIzquierdo > heighthijoDerecho:
                    left_child = n.left
                    if left_child is not None:
                        hhijoDerecho = (left_child.right.height
                                    if (left_child.right is not None) else 0)
                        hhijoIzquierdo = (left_child.left.height
                                    if (left_child.left is not None) else 0)
                    if (hhijoIzquierdo > hhijoDerecho):
                        self.rotatehijoIzquierdo(n)
                        break
                    else:
                        self.double_rotatehijoDerecho(n)
                        break
                else:
                    right_child = n.right
                    if right_child is not None:
                        hhijoDerecho = (right_child.right.height
                            if (right_child.right is not None) else 0)
                        hhijoIzquierdo = (right_child.left.height
                            if (right_child.left is not None) else 0)
                    if (hhijoIzquierdo > hhijoDerecho):
                        self.double_rotatehijoIzquierdo(n)
                        break
                    else:
                        self.rotatehijoDerecho(n)
                        break
            n = n.padre

    def rotatehijoIzquierdo(self, Anime):
        aux = Anime.padre
        Anime.padre = Anime
        Anime.padre.right = Anime
        Anime.padre.right.height = Anime.padre.height + 1
        Anime.padre.left = Anime.right


    def rotatehijoDerecho(self, Anime):
        aux = Anime.padre
        Anime.padre = Anime
        Anime.padre.left = Anime
        Anime.padre.left.height = Anime.padre.height + 1
        Anime.padre.right = Anime.right

    def double_rotatehijoIzquierdo(self, Anime):
        self.rotatehijoDerecho(Anime.getRight().getRight())
        self.rotatehijoIzquierdo(Anime)

    def double_rotatehijoDerecho(self, Anime):
        self.rotatehijoIzquierdo(Anime.getLeft().getLeft())
        self.rotatehijoDerecho(Anime)

    def search(self,puntuacion):
       if self.raiz:
           res = self._search(puntuacion,self.raiz)
           if res:
                  return res.nombre
           else:
                  return None
       else:
           return None

    def _search(self,nombre,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.nombre == nombre:
           return nodoActual
       elif nombre < nodoActual.nombre:
           return self._search(nombre,nodoActual.hijoIzquierdo)
       else:
           return self._search(nombre,nodoActual.hijoDerecho)


    def empty(self):
        if self.raiz is None:
            return True
        else:
            return False

    def preShow(self, Anime):
        if Anime is not None:
            self.preShow(Anime.left)
            print(Anime.puntuacion, end=" ")
            self.preShow(Anime.right)

    def preorder(self, Anime):
        if Anime is not None:
            self.preShow(Anime.left)
            self.preShow(Anime.right)
            print(Anime.puntuacion, end=" ")

    def getraiz(self):
        return self.raiz


class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamaño = 0

    def longitud(self):
        return self.tamaño

    def __len__(self):
        return self.tamaño

    def agregar(self,puntuacion,nombre,genero):
        if self.raiz:
            self._agregar(puntuacion,nombre,genero,self.raiz)
        else:
            self.raiz = Anime(puntuacion,nombre)
        self.tamaño = self.tamaño + 1

    def _agregar(self,puntuacion,nombre,genero,nodoActual):
        if puntuacion < nodoActual.puntuacion:
            if nodoActual.tieneHijoIzquierdo():
                   self._agregar(puntuacion,nombre,genero,nodoActual.hijoIzquierdo)
            else:
                   nodoActual.hijoIzquierdo = Anime(puntuacion,nombre,genero,padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                   self._agregar(puntuacion,nombre,genero,nodoActual.hijoDerecho)
            else:
                   nodoActual.hijoDerecho = Anime(puntuacion,nombre,genero,padre=nodoActual)

    def __setitem__(self,c,v,d):
       self.agregar(c,v,d)

    def buscar(self,puntuacion):
       if self.raiz:
           res = self._buscar(puntuacion,self.raiz)
           if res:
                  return res.cargaUtil
           else:
                  return None
           else:
                  return None

    def _buscar(self,nombre,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.nombre == nombre:
           return nodoActual
       elif nombre < nodoActual.nombre:
           return self._buscar(nombre,nodoActual.hijoIzquierdo)
       else:
           return self._buscar(nombre,nodoActual.hijoDerecho)

    def __getitem__(self,nombre):
       return self.buscar(nombre)

    def eliminar(self,nombre):
      if self.tamaño > 1:
         nodoaEliminar = self._buscar(nombre,self.raiz)
         if nodoaEliminar:
             self.remover(nodoAEliminar)
             self.tamaño = self.tamano-1
         else:
             print('el nombre no está en el arbol')
      elif self.tamaño == 1 and self.raiz.nombre == nombre:
         self.raiz = None
         self.tamaño = self.tamaño - 1
      else:
         print ('Error, el nombre no se encuentra en el arbol')

    def __delitem__(self,nombre):
       self.eliminar(nombre)

    def unir(self):
       if self.esHoja():
           if self.esHijoIzquierdo():
                  self.padre.hijoIzquierdo = None
           else:
                  self.padre.hijoDerecho = None
       elif self.tieneAlgunHijo():
           if self.tieneHijoIzquierdo():
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoIzquierdo
                  else:
                     self.padre.hijoDerecho = self.hijoIzquierdo
                  self.hijoIzquierdo.padre = self.padre
           else:
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoDerecho
                  else:
                     self.padre.hijoDerecho = self.hijoDerecho
                  self.hijoDerecho.padre = self.padre

    def encontrarSucesor(self):
      suc = None
      if self.tieneHijoDerecho():
          suc = self.hijoDerecho.encontrarMin()
      else:
          if self.padre:
                 if self.esHijoIzquierdo():
                     suc = self.padre
                 else:
                     self.padre.hijoDerecho = None
                     suc = self.padre.encontrarSucesor()
                     self.padre.hijoDerecho = self
      return suc

    def encontrarMin(self):
      actual = self
      while actual.tieneHijoIzquierdo():
          actual = actual.hijoIzquierdo
      return actual

    def remover(self,nodoActual):
         if nodoActual.esHoja(): 
           if nodoActual == nodoActual.padre.hijoIzquierdo:
               nodoActual.padre.hijoIzquierdo = None
           else:
               nodoActual.padre.hijoDerecho = None
         elif nodoActual.tieneAmbosHijos(): 
           suc = nodoActual.encontrarSucesor()
           suc.empalmar()
           nodoActual.puntuacion = suc.puntuacion
           nodoActual.nombre = suc.nombre
           nodoActual.genero = suc.genero

         else: 
           if nodoActual.tieneHijoIzquierdo():
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.puntuacion,
                                    nodoActual.hijoIzquierdo.cargaUtil,
                                    nodoActual.hijoIzquierdo.hijoIzquierdo,
                                    nodoActual.hijoIzquierdo.hijoDerecho)
           else:
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.puntuacion,
                                    nodoActual.hijoDerecho.cargaUtil,
                                    nodoActual.hijoDerecho.hijoIzquierdo,
                                    nodoActual.hijoDerecho.hijoDerecho)

     if__name__== "__main__"
         EddActual = None
         while True
           main()
