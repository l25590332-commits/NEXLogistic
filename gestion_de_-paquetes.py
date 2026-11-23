PRIORIDADES = {1: "Estándar", 2: "Exprés", 3: "Urgente"}
ESTADOS = ["Registrado", "En tránsito", "En reparto", "Entregado", "Cancelado"]

paquetes = {}  # Aquí se guardan todos los paquetes: {"PKG-01": {datos}, ...}


def texto(p):
    return f"[{p['id']}] {p['origen']} -> {p['destino']} | {PRIORIDADES[p['prioridad']]} | {p['estado']}"


def registrar(id_, origen, destino, prioridad):
    id_ = id_.strip().upper()
    if not id_ or id_ in paquetes:
        print("Error: el ID está vacío o ya existe.")
    elif not origen.strip() or not destino.strip():
        print("Error: origen y destino son obligatorios.")
    elif prioridad not in PRIORIDADES:
        print("Error: la prioridad debe ser 1, 2 o 3.")
    else:
        paquetes[id_] = {"id": id_, "origen": origen.strip(), "destino": destino.strip(),
                         "prioridad": prioridad, "estado": "Registrado"}
        print("Registrado:", texto(paquetes[id_]))


def consultar(id_):
    p = paquetes.get(id_.strip().upper())
    print(texto(p) if p else "No se encontró ese paquete.")
    return p


def listar():
    if not paquetes:
        print("No hay paquetes registrados.")
    for p in paquetes.values():
        print(texto(p))


def modificar(id_, campo, valor):
    p = paquetes.get(id_.strip().upper())
    if not p:
        print("No se encontró ese paquete.")
    elif campo not in ("estado", "prioridad", "origen", "destino"):
        print("Campo inválido.")
    elif (campo == "estado" and valor not in ESTADOS) or \
         (campo == "prioridad" and valor not in PRIORIDADES) or \
         (campo in ("origen", "destino") and not valor.strip()):
        print("Valor inválido para", campo)
    else:
        p[campo] = valor.strip() if isinstance(valor, str) else valor
        print("Actualizado:", texto(p))


def menu():
    while True:
        op = input("\n1.Registrar  2.Consultar  3.Listar  4.Modificar  0.Salir: ").strip()
        if op == "1":
            id_, origen, destino = input("ID: "), input("Origen: "), input("Destino: ")
            prio = input("Prioridad (1=Estándar, 2=Exprés, 3=Urgente): ")
            registrar(id_, origen, destino, int(prio) if prio.isdigit() else 0)
        elif op == "2":
            consultar(input("ID: "))
        elif op == "3":
            listar()
        elif op == "4":
            id_, campo = input("ID: "), input("Campo (estado/prioridad/origen/destino): ").strip()
            valor = input("Nuevo valor: ")
            modificar(id_, campo, int(valor) if campo == "prioridad" and valor.isdigit() else valor)
        elif op == "0":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()