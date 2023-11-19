
try:
    import naoqi
    print("naoqi found")
except Exception as e:
    print("Error: naoqi not found", e, sep='\n')