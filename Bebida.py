class bebida():
    def __init__(self, id, nombre, tags, categoria, alcohol, vaso, instrucciones, imagen, ingredientes, medidas, bienElectrico):
        self.id = id
        self.nombre = nombre
        self.tags = tags #dato variante segun la bebida
        self.categoria = categoria
        self.alcohol = alcohol
        self.vaso = vaso
        self.instrucciones = instrucciones
        self.imagen = imagen
        self.ingredientes = ingredientes #dato variante segun la bebida
        self.medidas = medidas  # dato variante segun la bebida
        self.bienElectrico = bienElectrico #campo en donde pondremos con cuantas te pones bien electrico

    def __str__(self):
        if self.tags != None:
            return str(f"Tu bebida es:"+"\n"+f"Nombre -> {self.nombre}"+"\n"+f"Tags -> {self.tags}"+"\n"+f"Categoria -> {self.categoria}"+"\n"+f"Alcohol -> {self.alcohol}"+"\n"+f"Vaso -> {self.vaso}"+"\n"+f"Instrucciones -> {self.instrucciones}"+"\n"+f"Imagen -> {self.imagen}"+"\n"+f"Ingredientes -> {self.ingredientes}"+"\n"+f"Medidas -> {self.medidas}"+"\n"+f"Te pones Bien Electrico con -> {self.bienElectrico}")
        else:
            return str(f"Tu bebida es:" + "\n" + f"Nombre -> {self.nombre}"+"\n" + f"Categoria -> {self.categoria}" + "\n" + f"Alcohol -> {self.alcohol}" + "\n" + f"Vaso -> {self.vaso}" + "\n" + f"Instrucciones -> {self.instrucciones}" + "\n" + f"Imagen -> {self.imagen}" + "\n" + f"Ingredientes -> {self.ingredientes}" + "\n" + f"Medidas -> {self.medidas}" + "\n" + f"Te pones Bien Electrico con -> {self.bienElectrico}")

    def __eq__(self, bebida):
        if bebida.id != self.id:
            return False

        if bebida.nombre != self.nombre:
            return False

        if bebida.tags != self.tags:
            return False

        if bebida.categoria != self.categoria:
            return False

        if bebida.alcohol != self.alcohol:
            return False

        if bebida.vaso != self.vaso:
            return False

        if bebida.instrucciones != self.instrucciones:
            return False

        if bebida.imagen != self.imagen:
            return False

        if bebida.ingredientes != self.ingredientes:
            return False

        if bebida.medidas != self.medidas:
            return False

        if bebida.bienElectrico != self.bienElectrico:
            return False