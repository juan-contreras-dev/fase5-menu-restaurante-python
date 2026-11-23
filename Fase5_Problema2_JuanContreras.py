# Juan Felipe Contreras Novoa
# Curso: Fundamentos de Programación (213022)
# Grupo: 213022B_2204
# Fase 5 Evaluacion Final - Problema 2
# Autor: Juan Contreras
# Código de autoría propia

CATEGORIA_OBJETIVO = "Bebidas"   
UMBRAL_PRECIO = 15000            
PORCENTAJE_DESCUENTO = 0.15      

menu = [
    ["Limonada de coco",      "Bebidas",  16000],
    ["Jugo de mora",          "Bebidas",   9000],
    ["Malteada de vainilla",  "Bebidas",  18500],
    ["Hamburguesa clásica",   "Platos",   28000],
    ["Bandeja paisa",         "Platos",   35000],
    ["Ensalada César",        "Entradas", 17000],
    ["Torta de chocolate",    "Postres",  12000],
]


def calcular_precio_final(categoria, precio_base):
    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        precio_final = precio_base * (1 - PORCENTAJE_DESCUENTO)
    else:
        precio_final = precio_base
    return precio_final

print("=" * 60)
print(f"{'Producto':<25} | {'Precio base':>12} | {'Precio final':>12}")
print("=" * 60)

for producto in menu:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]
    precio_final = calcular_precio_final(categoria, precio_base)
    print(f"{nombre:<25} | {precio_base:>12,.0f} | {precio_final:>12,.0f}")

print("=" * 60)
print(f"Descuento del {PORCENTAJE_DESCUENTO * 100:.0f}% aplicado a '{CATEGORIA_OBJETIVO}' "
      f"con precio mayor a {UMBRAL_PRECIO:,}")