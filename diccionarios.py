midiccionario = {
    "alemania": "Berlin",
    "francia": "paris",
    "reino unido": "madrid"
}
midiccionario["italia"] = "lisboa"
print(midiccionario)
midiccionario["italia"] = "rma"
print(midiccionario)
del midiccionario["reino unido"]
print(midiccionario)

otrodiccionario = {
    123: "unodostres",
    "unodostres": 123
}
print(otrodiccionario)

mitupla = ["españa", "francia", "alemania"]
tudiccionario = {mitupla[0] : "madrid", mitupla[1]: "londres", mitupla[2]: "berlin"}
print(tudiccionario)

sudiccionario = {
    23: "jorfa",
    "nombre": "micjael",
    "aniñños": [1998,1222,1233]
}
print(sudiccionario)
print(sudiccionario["aniñños"][2])

print(sudiccionario.keys())
print(sudiccionario.values())



