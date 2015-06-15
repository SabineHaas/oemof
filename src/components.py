class Component:
    """
    """
    def __init__(self, **kwargs):
        """
        :param uid: unique component identifier
        """
        self.uid = kwargs["uid"]

class Transformer(Component):
    """
    """
    def __init__(self, **kwargs):
        """
        :param dict busses: expected keys: "from" and "to" containing the
                            source and target busses (as 'Bus') objects,
                            respectively.
        """
        super().__init__(**kwargs)
        self.busses = kwargs["busses"]
        # TODO: Günni schreibt transformer in busse
        
class Connection(Component):
    """
    """
    def __init__(self, **kwargs):
        """
        :param dict busses: expected keys: "from" and "to" containing the
                            source and target busses (as 'Bus') objects,
                            respectively.
        """
        super().__init__(**kwargs)
        self.busses = kwargs["busses"]
        
class Bus(Component):
    """
    """
    def __init__(self, **kwargs):
        """
        :param type: bus type could be electricity...BLARBLAR
        :param transformers: BLARBLAR
        """
        super().__init__(**kwargs)
        self.type = kwargs["type"]
        self.transformers =  []
    
if __name__ == "__main__":
    my_bus1 = Bus(uid="b1", type="electricity")
    my_bus2 = Bus(uid="b2", type="electricity")
    my_trans = Transformer(uid="t1", busses={"from": [my_bus1], "to": [my_bus2]})
    my_connections = Connection(uid="c1", 
                                busses= {"from": [my_bus1], "to": [my_bus2]})
    print(my_trans.uid)
    print(my_trans.busses["from"][0].uid)
    print(my_bus1.transformers)