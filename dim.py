###########################################################################
# class    : dim.py                                                       #
# Scopo    : creare degli arrey tipo basic con indici personalizzabili    #
# Autore   : Marco Salvati                                                #
# Email    : salvatimarco61@gmail.com                                     #
# Data     : 2019-11-28                                                   #
###########################################################################

class dim():
    """
        class    : dim
        Scopo    : creare degli arrey tipo basic con indici personalizzabili
        Autore   : Marco Salvati
        Email    : salvatimarco61@gmail.com
        Data     : 2019-11-28
    """
    def __init__(self,atype,start,end,data=[]):
        """ atype tipo di array: integer, float, string, complex, bool, any
        any accetta tutti i tipi
        esempio d'uso: a=dim('integer',-7,7)
        crea un array di interi con indici che vanno da -7 a 7
        """
        self.__atype=atype.upper()
        self.__start=start
        self.__end=end
        self.__range=range(self.__start,self.__end+1)
        self._posti=len(self.__range)
        self.__valori_iniziali={"INTEGER":0,"FLOAT":0.0,"COMPLEX":(0+0j),"STRING":"",\
                "BOOL":False,"ANY":None}  
        self.__array=[(self.__valori_iniziali[self.__atype])]* self._posti
        for i in range(len(data)): # sono presenti dei valori da settare
            self.__array[i] = data[i]
            
    def LBound(self):
        """ Ritorna il limite inferiore dell'array """
        return self.__start
    def UBound(self):
        """ Ritorna il limite superiore dell'array """
        return self.__end 
    
    def __getitem__(self,item):
        if isinstance(item,slice):
            if item.start is None:
                start=0
            else:
                start=self.__range.index(item.start)
            if item.stop is None:
                stop=len(self.__array)
            else:
                stop=self.__range.index(item.stop)
            if item.step is None:
                step=1
            else:
                step=item.step
            return self.__array[start:stop:step]
        
        elif isinstance(item,int):
            if not item in self.__range :
                raise ValueError("Indice fuori scala")
            return self.__array[self.__range.index(item)]               
        else:
            raise KeyError("L' item deve essere intero o slice")
    def __setitem__(self,item,value):
        if isinstance(item,slice):
            for v in value:
                if not self.__is_valid_value(v):
                    raise ValueError("il Valore richiesto deve essere {}".format(self.__atype))  
            if item.start is None:
                start=0
            else:
                start=self.__range.index(item.start)
            if item.stop is None:
                stop=len(self.__array)
            else:
                stop=self.__range.index(item.stop)
            if item.step is None:
                step=1
            else:
                step=item.step
            self.__array[start:stop:step]=value
        
        elif isinstance(item,int):
            if not item in self.__range :
                raise ValueError("Indice fuori scala")              
            if self.__is_valid_value(value):
                self.__array[self.__range.index(item)]=value
            else:
                    raise ValueError("il Valore richiesto deve essere {}".format(self.__atype))

    def __is_valid_value(self,value):
        """ Ritorna True se il valore è del tipo corretto """
        if self.__atype=="ANY":
                return True             
        if self.__atype=="INTEGER":
            if isinstance(value,int):
                    return True
            else:
                    return False
        elif self.__atype=="FLOAT":
            if isinstance(value,float):
                return True
            else:
                return False                
        elif self.__atype=="COMPLEX":
            if isinstance(value,complex):
                return True
            else:
                return False
        elif self.__atype=="STRING":
            if isinstance(value,str):
                return True
            else:
                return False          
        elif self.__atype=="BOOL":
            if isinstance(value,bool):
                return True
            else:
                return False
                  
        else:
            return False

    def index(self,*args):
        """ritorna l'indice relativo a un valore dell'array:
           esempio su un array di interi:
           a.index(88) ritorna l'indice del valore 88 
           a.index(88,3) ritorna l'indice del valore 88 a partire dall'indice 3
           a.index(88,3,5) ritorna l'indice del valore 88 nel range indici da 3 a 5
           """
        if len(args)==1:
            ir=self.__array.index(args[0])
            return self.__range[ir]
        elif len(args)==2:
            s=self.__range.index(args[1])
            ir=self.__array.index(args[0],s)
            return self.__range[ir]
        elif len(args)==3:
            s=self.__range.index(args[1])
            e=self.__range.index(args[2])
            ir=self.__array.index(args[0],s,e)
            return self.__range[ir]
        else:
            raise ValueError('il valore non non è presente')
        
    def clear(self):
        """ azzerra l'array """
        for  i in range(len(self.__array)): self.__array[i]=(self.__valori_iniziali[self.__atype])
   
    def __str__(self):
        """array to string"""
        return str(self.__array)
    def __repr__(self):
        """implementazione metodo repr"""
        return "%s.%s('%s',%d,%d,data=%s)" % (self.__class__.__module__,
                                      self.__class__.__qualname__,self.__atype,
                                      self.__start,self.__end,repr(self.__array))

    
    def __iter__(self):
        "Ritorna un iteratore su i valori"
        return iter(self.__array)

    def __contains__(self, key):
        """operatore in"""
        return key in self.__array

    def sort(self, reverse=False):
        "Ordina l'array"
        self.__array.sort(reverse=reverse)
        
    def reverse(self):
        """ inverte l'array """
        self.__array.reverse()

    def __reversed__(self):
        """ Ritorna un iteratore con l'array invertito"""
        return reversed(self.__array)
    def count(self,value):
        """ Conta il numero di ripetizioni di un valore"""
        return self.__array.count(value)
    def keys(self):
        """ Ritorna un iteratore sugli indici """
        return self.__range
    def append(self,item=1): # aggiungi 1 o più indici
        """ Aggiunge altri posti nell'array default 1 posto"""
        for i in range(item):
            self.__array.append(self.__valori_iniziali[self.__atype])
        self.__end+=item
        self.__range=range(self.__start,self.__end+1) 
    def __len__(self):
        """ Ritorna la lunghezza della'array"""
        return len(self.__array)
