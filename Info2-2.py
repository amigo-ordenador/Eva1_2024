vlanId = int(input("Ingrese ID de VLAN: "))
if vlanId >= 1 and vlanId <= 1005:
    print("Esta Vlan se encuentra dentro del rango Normal.")
elif vlanId >=1006 and vlanId <= 4095:
    print("Esta Vlan se encuentra dentro del rango Extendido.")
else:
    print("Rango de VLAN desconocido.")