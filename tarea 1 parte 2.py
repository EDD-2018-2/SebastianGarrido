class Node:
 
        def __init__(self,valor):
                  self.valor = valor
                  self.next = None

        def getelemento(self):
                return self.valor
 

  class Queue:
         def __init__(self):
                 self.length = 0
                 self.head = None
                 self.last = None

         def es_vacio(self):
                  return self.length == 0

         def encolar(self, valor):
                  node = Node(valor)
                  if self.head is None:
                          self.head = node
                  else:
                     self.last.next = node
                     self.last = node
                     self.length += 1

         def desencolar(self):
                if self.head != None:
                        aux = self.head
                        self.head = self.head.next
                        return aux
   class stack:
          def __init__(self):
                  self.head = None
                  self.contador = 0
   
           def push(self, valor):
                   new_node = Node(valor)
                   self.contador += 1
                   if self.head != None:
                           new_node.next = self.head
                           self.head = new_node
         
            def pop(self):
                    if self.head != None:
                            aux = self.head
                            self.head = self.head.next
                            return aux
             
            def es_vacio(self):
                   if self.head is None:
                           return True 
                   else: 
                           return False
            
        def Notacionpolaca(string):
                operators = stack()
                numbers = queue()
                tamaño = len(string)
                for i in range(tamaño):
                        if string [i] == + or string[i] == * or string[i] == - :
                                   operators.push(string[i]) 
                        else: 
                            if string[i] != None :
                                       numbers.push(string[i])
                                       print (operators.pop() " ")    
                while numbers.es_vacio() == false:
                          if numbers.head ==(:
                                print ( operators.pop() " ")
                          elif numbers.head.next = (:
                                 print( operators.pop() " ")
                          else: 
                                 print( numbers.dequeue() " ")
                 print( " es: " int(string))

          def Notacionpolacainversa(string):
                  operators = queue()
                  numbers = queue()
                  tamaño = len(string)
                  for i in range(length):
		            if string [i] == + or string [i] == * or string [i] == -:
			     operators.push(string [i])

		   elif (string [i] is not None):
			numbers.push(string [i])
	
	           while numbers.is_empty() == false:
		             if numbers.head == (:
			         numbers.dequeue()
		              elif numbers.head.next =! ):
			          print( numbers.dequeue() " ")
	           elif numbers.head == (:
			print( operators.dequeue() " ")
	 print( "Es : " int(string))

                  
