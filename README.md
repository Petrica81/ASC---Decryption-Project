# ProiectASC1pet
 Precizez ca este posibil ca parola aflata de mine sa nu coincida cu parola din formularul echipei adverse.
 
 Numele Echipei Noastre: Bizonii
 
 Numele Echipei Adverse: Vigilantes
 
 Cheia Echipei Adverse: c3lzLmFyZ3ZbM10=
 
 Orice cheie, de dimensiune 10-15, introdusa manual este corecta deoarece variabila "key" a lor este realizata prin urmatorele linii de cod:
 
 password="sys.argv[3]".encode("utf-8")
 key=base64.b64encode(password)
 
 Fisierul Output este posibil sa fi fost modificat in momentul încarcarii lui pe github. Cand xorez input.txt cu output ca sa aflu cheia, imi retunează o cheie diferita si de "key".
 P.S. Practic nu a fost nevoie sa ma folosesc de fisierul "input.txt" ca sa aflu cheia cu care s-a realizat codificarea.
