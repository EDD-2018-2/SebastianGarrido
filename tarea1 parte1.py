class Node: 
       
         def __init__(self, valor):
                   self.valor = valor
                   self.prev = None
                   self.next = None
                   self.value = 0

         def getElemento(self):
               return self.data
 
   class Lista:
 
         def __init__(self):
                  self.head = None
                  self.contador = 0
 
         def agregar(self, valor):
              aux1 = Node(valor)
              aux2 = self.head
              aux1.next = self.head
              if self.head != None:
                      while(aux2.next != self.head):
                            aux2 = aux2.next
                            aux2.next = aux1 
                            self.contador += 1
              else:
                      aux1.next = aux1
                      self.head = aux1
                      self.contador += 1 


          def insertar(self, new_node):

                 temp = self.head
                 if temp is None:
                         new_node.next= new_node
                         self.head = new_node
                         self.contador +=1
                 
                  if (temp.value >= new_node.value):
                        while temp.next != self.head:
                                temp = temp.next
                        temp.next = new_node
                        new_node.next = self.head
                        self.head = new_node
                        self.contador += 1
           
           def borrarNodo(self, valor):
                  aux = self.head
                  tamaño = len(self)
                  if self.head is None :
                          return None
                  for i in range(tamaño):
                          if aux.valor == delete:
                                  pre = aux.prev
                                  aux = aux.next
                                  aux.prev = prev
                                  self.contador -= 1
                           else: 
                                  aux = aux.next
                
            def buscar(self, valor):
                       aux = self.head
                       if self.head is None or valor is None:
                                return None
                       for i in range(self.contador):
                                if aux.valor == valor:
                                            aux.value += 1
                                            return aux
                                 else:
                                            aux = aux.next
                                            
