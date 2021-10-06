#defining a class book
class book:
    def __init__(self,tit,aut,pub,p,cp=0):#Initializing it with instances variables as title,author,publisher,price,copies
        self.title=tit
        self.author=aut
        self.publisher=pub
        self.price=p
        self.copies=cp
    #Using getter and setter method for title variable    
    def get_title(self):
        return self._title
    def set_title(self,tit):
        self._title=tit
        return
    title=property(get_title,set_title)
    #Using getter and setter method for author variable  
    def get_author(self):
        return self._author
    def set_author(self,aut):
        self._author=aut
        return
    author=property(get_author,set_author)
    #Using getter and setter method for publisher variable  
    def get_publisher(self):
        return self._publisher
    def set_publisher(self,pub):
        self._publisher=pub
        return
    publisher=property(get_publisher,set_publisher)
    #Using getter and setter method for price variable  
    def get_price(self):
        return self._price
    def set_price(self,p):
        self._price=p
        return
    price=property(get_price,set_price)
    #Using getter and setter method for copies variable  
    def get_copies(self):
        return self._copies
    def set_copies(self,cp):
        self._copies=cp
        return
    copies=property(get_copies,set_copies)
    #defining a method for calculating royality
    def get_royality(self):
        if self.copies<=500:#10% of price for first 500 copies
            self._royality=self.copies*self.price*10/100
        elif self.copies<=1000:#12.5% of price for next 1000 copies
            self._royality=500*self.price*10/100+(self.copies-500)*self.price*12.5/100
        else:# 15% of price for all further copies
            self._royality=500*self.price*10/100+500*self.price*12.5/100+(self.copies-1000)*self.price*15/100
        return self._royality
    royality=property(get_royality)

# definig a inherited class ebook from the base class book
class ebook(book):
    def __init__(self,tit,aut,pub,p,cp=0,form=None):#Initializing a new instance variale format
        super().__init__(tit,aut,pub,p,cp)#Using super function for getting the old variables
        self.format=form
    def get_format(self):
        return self._format
    def set_format(self,form):
        self._format=form
        return
    format=property(get_format,set_format)
    #Redifining royality method 
    def get_royality(self):
        ryl=super().get_royality()
        ryl=ryl-ryl*12/100 #deduct GST of 12% onn ebook 
        self._royality=ryl
        return self._royality
#making objects
if __name__=="__main__":
    #b1 object is created for book class
    b1=book('Object oriented programming','Umakshi','U.Sharma',1000,6000)
    print('The name of the book is {} ,its author is {} and its publisher is {}'.format(b1.title,b1.author,b1.publisher))
    print("The Royality earned by author is {}".format(b1.get_royality()))
    #e1 object is created for ebook class
    e1=ebook('Object oriented programming','Umakshi','U.Sharma',1000,6000,'PDF')
    print('Ebook of the {} is available in {} format which is written by {} and published by {}'.format(e1.title,e1.format,e1.author,e1.publisher))
    print("The Royality earned by author in ebook is {}".format(e1.get_royality()))      
    
