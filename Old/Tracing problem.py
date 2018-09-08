class B:
    def __init__(self, name):
        """
        @type self: B
        @type name: str
        @rtype: None
        """
        self._name = name

    def __str__(self):
        return "Iâ€™m a B named " + self._name

    def mB(self, n):
        """
        @type self: B
        @type n: int 
        @rtype: None
        """
        print("mB", self._name, str(n))


class C(B):
    def __init__(self, name):
        """
        @type self: C
        @type name: str
        @rtype: None
        """
        B.__init__(self, name)
        self._name_len = len(name)

    def __str__(self):
        """
        @type self: C
        @rtype: str
        """
        return "Iâ€™m a C named " + self._name + "-" + str(self._name_len)

    def mC(self, n: int):
        """
        @type self: C
        @type n: int
        @rtype: None
        """
        print("mC", end = " ")
        B.mB(self, n+1)


class D(C):
    def __init__(self, name):
        """
        @type self: D
        @type name: str
        @rtype: none
        """
        C.__init__(self, "Super " + name)
        self._junk = self._name_len + 3

    def mC(self, n):
        """
        @type self: D
        @type n: int
        @rtype: None
        """
        print(str(self._junk), end="")
        C.mC(self, n+1)

if __name__ == "__main__":
    b = B("Bob")
    c = C("Carole")
    d = D("Dan")