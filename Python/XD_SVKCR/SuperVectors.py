import random
import math
import sys
""" -- Super Vectors classes and functions --
    :::-----------------------------------:::
    Super Vectors have the same capabilities than regular vectors, but what makes them super, is that they never point at the same direction.
        In addition of the ordinary elements of a vector, Super Vectors have a third proprety: Magic!
        Magic is the seed of how will the SVector move everytime we call it .
        SVectors2 just contain 2 SVectors instead of 1 and have more features too
        BlackBoxes are a new crypto key securing, so secure that I would risklessly say that I'd give 1,000$ to the one who gets, without cheating, a succes Value from calling it


        SuperVectors by CHIBOUNI Aris, Roixd.
        -------------------------------------
        """
class SVector:
    """This is a SVector, a Vector that can perform magic.
        * IMPORTANT: SVectors are only called like a function (with ()) do NOT use them as a variable.

        PARAMETERS
        ----------
        d : the initial value of the vector.
        magic : the "seed" that changes the initial position of the vector each time it's used.

        
        METHODS
        -------
        translate(n) : moves the vector along its only axis(d) by n, works for negative values.
        SVector.refresh(svect) : refreshes svect by placing its value d randomly.

        
        PROPRETIES
        ----------
            magic : the seed of the svector, no getting and if you try to change its value, its reset automatically to 0.
            d : the position of the vector, changes each time you set it, can equal infinity.

            
        STR FORMATING
        -------------
            Format specs:
                * bin : returns its binary value
                * pos : returns the float of its value up to 5 decimal places
                * sig : returns the sigmoid of its value
                * mem : shows its allocation in memory (48 bits)  
        RANDOMIZATION
        -------------
            The program uses the random module, which - as its documentation says - uses SHA256 which is totally random
    """
    def __init__(self, d=1, magic=1.6180339887):
        self.d = d
        self._magic = magic
        SVector.refresh(self)
    
    # Move a vector through d
    def translate(self, n):
        self.d += n
    
    # Everytime it's called...
    def __call__(self):
        SVector.refresh(self)
        return str(self) 
    
    # Refreshes a vector
    @classmethod
    def refresh(cls, svect):
        if svect._magic != 0:
            svect.d = svect.d*(random.randrange(0, math.ceil(abs(svect.d+svect._magic)+1))/svect._magic)
        else:
            svect.d = 1
    # --- Operator & String overrides ---
    
    # +
    def __add__(self, other):
        constd = self.d            
        self.translate(other.d)
        return SVector(constd + other.d, other._magic)
    
    # *
    def __mul__(self, other):
        for _ in range(other):
            self = self + self
        return self

    # str
    def __str__(self):
        SVector.refresh(self)
        return f"<SVector Dimension:{self.d}>"
    
    # format specs (f"{SVector:...}")
    def __format__(self, format_spec):
        SVector.refresh(self)
        match format_spec:
            case "bin":return bin(round(self.d))
            case "pos":return f"{self.d:.5f}"
            case "sig":return str(1 / (1 + math.exp(-self.d)))
            case "mem":return str(sys.getsizeof(self))
            case _:return self
    #
    # --- Propreties --- 
    
    # Dimension
    @property
    def d(self):
        """Getter for d."""
        return self._d
    
    @d.setter
    def d(self, value):
        """Setter for d, refreshes the SVEctor"""
        if value == 0 or value == None:
            SVector.refresh(self)
        elif value == math.inf:
            self._d = self._magic
        else:
            self._d = value
    
    @property
    def magic(self):
        "No getting of magic(protected)."
        pass 
    
    @magic.setter
    def magic(self, _):
        "If you try to set magic, it disappears."
        self._magic = 0


class SVector2:
    """A class for a Super Vector2, which is componed of 2 SVectors.
        
        PARAMETERS
        ----------
            x: the x svector.
            y: the y svector.

            
        METHODS
        -------
            SVector2.refresh(self): Refreshes both inside Vectors.
            Box: Draws a square with both x and y vectors(is also a format spec).  
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    # Box
    def box(self):
        #SVector2.refresh(self)
        return self.x.d * self.y.d
    # Refresh the two inside vectors
    @classmethod
    def refresh(cls, self):
        self.x(), self.y(), self.__init__(self.x, self.y)

    # --- Method overrides... ---
    def __str__(self):
        return f"<SVector2 x -- :{self.x:pos}; y -- :{self.y:pos}>"

    def __call__(self):
        SVector2.refresh(self)
        return f"{self:box}"
    
    def __format__(self, format_spec):
        match format_spec:
            case "box": return f"{self.box()}²"
    # + operator
    def __add__(self, other):
        return SVector2(other.x + self.x, other.y + self.y)
class BlackBox(SVector2):
    """BlackBoxes, literally
    
    * Decends from SVector2

    * When you call itself and specify the <b>test</b> and if it turns out to be the box() of the BlackBox, you 
    Succeed even though I really doubt someone could have this someday anyways if you do, send me a message on
    <b>chibouni562@gmail.com</b> with a legitmate proof.
    """
    def __init__(self, x, y):
        super().__init__(x, y)

    

    def __call__(self, test):
        super().__call__()
        if test == self.box():
            return "Succes"
        else:
            return "Fail"