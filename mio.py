 # Este es un programa de para saber cual es la chica ideal de Angel. 
4
print(" Bienvenid@. ")

print("\n")

print(""" Éste programa consiste en:
    
   1. Decir cual es el nombre correcto de la única chica que le gusta a Angel.
   
   2. Decir como es ella en absoluto.
   
   3. Confirmar que es ella, con su numero de teléfono.

   4. Saber que es ella para èl.
   
   5. Al colocar el nombre invalido, el programa inmediatamete dará error. \n""")
 
name = str(input("* Hola, ¿Cúal es tú nombre? "))

print("\n")

com = str(input(" Saludos "+ name +". ¿Cómo te sientes en éste día? "))

print("\n")

print(" Nos hace bien saber como estas en estos momentos. ")

sab = str(input("\n Te interesaría saber algunas informaciones personales de Angel como, ¿Quíen es la chica que le gusta? "))

print("\n")

dig = str(input(" Okay, Si conoces la chica, entonces su nombre correcto es: "))

print("\n")

n = "darli"
s = "DARLI"
a = "Darli"
m = "maricielo"
v = "Maricielo"
e = "MARICIELO"
p = "MARIELA"
o = "mariela"
k = "Mariela"
t = "Darli Mariela Diaz Diaz"
q = "darli mariela diaz diaz"
r = "darli mariela"
j = "Darli Mariela"
b = "Darli mariela"
h = "darli Mariela"
hh = "DARLI MARIELA"
hhh = "DARLI MARIELA DIAZ DIAZ"
u = "Avatar"
uu = "avatar"
uuu = "AVATAR"
g = "Angel Antonio Gomera R."



print("\n")


if sab == "si" and dig == n:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + n + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + n + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + n + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26. Es su Alma.
 
 27. Es su bebé.
 
 28. Es su Medicina.


  Ella lo es Todo en su Vida.
  
   * Su Sonrisa.
  
   * Sus Ojitos.
  
   * Su Felicidad.

  Es lo que èl busca darle dìa por dìa a ella.

  Lo Ùnico que debes saber es que, èl la AMA con locura, y si deseas saber hasta cuanto. Solo debes empezar a contar los latidos de su corazòn. 
   \n""")

    print(" Siempre èl le darà las gracias a Dios por permitirle coincidir con esa chica tan linda, y luego las gracias a ella por permitir que èl la pueda conocer y entrar a su vida. \n")

    print(" * ==================== * Te Amo Mucho "+ n + ", Hasta el infinito y màs allà * ==================== * \n")

    print (" * Gracias por llegar a mi vida Amor. ")
    
elif sab == "no" or sab == "No":
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")


elif sab == "si" and dig == s:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + s + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + s + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + s + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26. Es su Alma.
 
 27. Es su bebé.
 
 28. Es su Medicina.


  Ella lo es Todo en su Vida.
  
   * Su Sonrisa.
  
   * Sus Ojitos.
  
   * Su Felicidad.

  Es lo que èl busca darle dìa por dìa a ella.

  Lo Ùnico que debes saber es que, èl la AMA con locura, y si deseas saber hasta cuanto. Solo debes empezar a contar los latidos de su corazòn. 
   \n""")

    print(" Siempre èl le darà las gracias a Dios por permitirle coincidir con esa chica tan linda, y luego las gracias a ella por permitir que èl la pueda conocer y entrar a su vida. \n")

    print(" * ==================== * Te Amo Mucho "+ s + ", Hasta el infinito y màs allà * ==================== * \n")

    print (" * Gracias por llegar a mi vida Amor. ")
    
elif sab == "no" or sab == "No":
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")



elif sab == "si" and dig == a:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + a + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + a + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + a + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26. Es su Alma.
 
 27. Es su bebé.
 
 28. Es su Medicina.


  Ella lo es Todo en su Vida.
  
   * Su Sonrisa.
  
   * Sus Ojitos.
  
   * Su Felicidad.

  Es lo que èl busca darle dìa por dìa a ella.

  Lo Ùnico que debes saber es que, èl la AMA con locura, y si deseas saber hasta cuanto. Solo debes empezar a contar los latidos de su corazòn. 
   \n""")

    print(" Siempre èl le darà las gracias a Dios por permitirle coincidir con esa chica tan linda, y luego las gracias a ella por permitir que èl la pueda conocer y entrar a su vida. \n")

    print(" * ==================== * Te Amo Mucho "+ a + ", Hasta el infinito y màs allà * ==================== * \n")

    print (" * Gracias por llegar a mi vida Amor. ")
    
elif sab == "no" or sab == "No":
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")


elif sab == "si" and dig == m:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + m + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + m + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + m + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hor` diRieir{e a�hablarle c una persona, o aNte(vna audiencia 
 0

  ; ============== * CaricTerìqticks " ============?=== *

"!M�  Es`una perSona:

   *Educada.
   *Sonfiable.
j " *Con Valores.

 !!*Tolerante.

   *fiel.

   *Respectuosa.

   *Divertid!.
M
  0*Qmeble.
J  (*ClAra y Precisa.

   *etc.
J0Lo ùLtim Que po�rìa decirte es`que, ella es una perso.i ÙNICA en èsta tieRpa. No hay nadi% cOmo elha. \n""&)

    elif coOm == "no" or!boom == "No":
        print(" Gstà bien, sino q�ieres saber la{ ilform`cionew- puedes vetirarTe lel prgrama. \n")

    com/ = sdr hnput(# Ckloca una 'c', si�duseAs continuar y s`Ber otra informaciòl iep�rtante: "))

    if colo =< "a" or colo == "C":
-
    
(       print ("""^n ¿Què as ella parq Angej? Pues, Ella para èd:
	
 3. �s su Corazòn.
 
 2. Es s} Prigridae.
 
 3.Es su Pre�cutaciS�n.	
 
 4.$Es su Negra Linda&
 
 5. Es(sU Ada durmiente.
 
 6. Es su Disectora.
 
 7. Es@su More.
 M
 8.(Es su Vayn`.�
 9. Es su cielm.* 
 14. Es su Uva mðS SabroS!.
 
 11. Es se Mr de Ojos Li~dn3.
 
 1". Es su Tesorm.
 
 13. Es su Pv�nceca.
"
 14. Es su Nari:ùa>
 
 15. Es su Glopona.
`
 12. Es$su"Puchua.
 * 17. Es su Ùnico(Amor.
(p18. Es su Regalo Iàs Bonipo.`M
 19. Es �u egalo Enviado Por Dyos.
"
 20. Es"su Lugar!Seguro.
 
 2�* Es se Rafugio.
 
 2�. Es0su!B/shita Bella.
 
 23� Er su Cielo.
 
 2. Es su Paz.
  25. Es su VkEa.
 
 26. Er su Il-a.
 
 27. Es su beb��.
 
 2<. Es su Medicina.

	
  Elma�lo es To�� en {u Vida.
  * ` * Su So.zisa.
  
 ( * Sus Ojitos�
  
   * Su Felicidad.
��� Es lo que$èl b5cca darle dìa por dìa a e|la.

  Lo Ùnicc que debes saber es�q5e, �l la AMA cn locura,y si deseas saber jasta cuanTo. SoLn dgbes empuzar a c+ndaz Los latidos de su cora�ðn. 
   \n"�")

  8 print�" Siempre èl le darà las(gracias a DI/s p/p rmrEi4irle coincidir con esa chica tan linda< Y lweoo lis grAcaas i el�c!por permitir Que èl la pueda c/nocer y entsab a u5 vida. \n")�  ( print(" * ===}9========-===== * Te imo Mucho "+ i��  , H`sta al )nf)nkto y m��s allÀ * =================== * \n")

    p2int (" *`Gracias por llegar ! mi vid` Amo2. ")
    
enif 3ar == bno" or sab == "No":
    
    print(* Okay, como nG le inturesc saber ès4e ppograma se cebrarà de inmudiato.\n")
    
    pr)nt (& See You Later. \n ")
    

elif qab!== "si# a~l dig == v:
    pRint(" * ===================================<==5====-========<5=====-9=<=<=-======--= 
( 9======4===================}59======?5=====5===============-===9== *")
  ` print8" * Guao, acertaste tuien es porque [" + v(+ "] es la ��ni#a chica que le encmnta en0�sta tiErra a *==* " + g +" *==*"-
    print(" * }======<-===}}==========================?}5=================}=======�===}==== ** ==9======================5==================�==============9-�==5 *\n")J    J    tgl =0jnt(hnpu|( Si la sojoces dime, ¿CúAl es su número Telefónicn?!"))
  `     nume1  826538777
    M
 (  nume2 = 829-673-877'J        rrint("\n")
    
 !  if tml == fUMe1 or teh == nume2:
        print("\n Excelente, ��rte es el$n�mero cowrecto de " + v +  * \n"	*   `    ehif ngt tel == nume1`or not te�(== nume2: 
  (     print 9"Fallaste, éste�no Er el n��mero correcto de " + v + ". \n")

    coom = qtr(input*" ¿T% Gustarìa saber como es ella, y algunas de s�r grcndes caraaterìsd)cas? "))

    if cOom == "si" or coom =� "Si":
     !  
        pri.d( "" Ella es }na chica mty )nteligentd, l|ena de valores y(uf gran proròsito En su wiaa.�

  Una jo|en que$~o busca m��s que lograr sqperarse dìa a dìa, parA asì tene�èzito { hacer�realidad 4odos s}s(ru%ños�y anhelOs a logra2.*
  Tmene una visiòn exc%lente, edla sabiendo Qum a Angel le encAjta sq forma de pen#ar Y(de encontrarlm solu#iòn a cuadquier wituaciǲ~ `reselti.M
  
  Posee�la gran capacidad `e repenes laq infor-aciones y ehplicarle a los$demàs`de una manera genial.

  Y si hay una knforMagiòn Que no se`puede quedar es que... Es excelente en 4odo lo que habe,0�a sea ej el àrea de:
(* ========== * ======9===9 *
   *Trab`jo Individual.
  -
 ! *Tz!jajo en Equipo.  M
   "Presentaciones.
 "�   *Habnar en Pùblico  
  (*Cantar.
 * ===8===5== * =========== *M
 
  Tiene un excenende løxico(a la hora dirigirse a habl`rld a$unq p%rsoFa, o afte u.a a5diencib.
  *
  * ==============`* Caracterìsticas . =============== *

  
  Es una pe2skna>-
�   *E`ucida.J
   *Confaable.

   *Con Valkres.

   *TleRante.

   *Fiel.

   *ReSpe#tuosa~

`  *Dirertida.
-
   *Amabme.

   *Clara y PRecysa.

!  *etc.-

 Lo ùltimo q5e podrìa decirte es qwe, dlla es una persona ØNICA en èSta tie2ra. Fo hay nadke Como ehla. \n""")

    e`if`c/km <= "n�" or coom == "Lo"

        print(" Està bien, sino qwiEres saber l!s iofovmaciones, puedes retirartE lel programA. \n")

    colo 9 str(input(" Coloca una 'c'- ci $esear continuar y Qaber otra informagiòn importante: "		

    if cglo = "c" or colo == "A":

    
    (   print ("""\j$��Què es ella para Angel Pees, Ella!para èl:

 1. �s su Sorazòn/
 
 2* Es su Priozida`>
 
 3.0Es su Pr�ocutaci��N.m 
 4/ Es s� Newra L�nd!.
  5, Es su Ada durmiente
 K 6. Es�su Directora.
 
 7. Es se more.
 
 8. Es sw Re}na.
 J 9. Es su Cielol-
 
(10. Es su(Uta m�s Sabrosm.
 
 11> E# su Mor de Ojow Himdos.
 
 12. E{ su Tesoso.M
!
 13. Es su Priocesa,
 
 14. Es st LarI~ùa/
 J 15/ Gs su Glotona,
 
 1&.$Es su BucHua.-
 
 17. Es su Ùnkko Emos.
 
 18. Es su Zegalo Màs Bonitn.
 
 19. Es su Regal/ Enviado por Dios.
 
 2. s su Lugar Seguvo<
 
 21. Es su Refugio.
 
`22. Ec su Coshita Bglla.
 
 23. Es su Ci%lo.
 
 24, Es su Paz.
"
 25. es su Vyda.
 
 26. Es su Almc.
 
 27. Es 3u"bebé.
 
 28.�Es qu Medicin`.-
�
 0Ella lo es Todo ao su Vida.  
   * Su Sonrisa,
  J   * SUs0Ojitos.  
 ` * �u F%licidaD.
*  Es(,� 1ue �)D busca darle dìa por$dìa a0ella&

  Lo Ùnico que d%ber saber es que, èl h! AIA col docura, y si deseaS siber hasda cuanto. so|o deb�s(emPez`r a cknt`s los latidos de su corazân.(
   XN"")J
    print(" Shempre èl le darà las gracias c Dios!Por permitirle ckincidiv con esa ahiba tan linda, y luego |as1gracias$a edla por Permytir que èl la pueda conocer | envrar i su vida. \n")

    pzint(" * ===?===-============ * Te Amo 5cho "+ v + ", Hasta el anfinit/ y màs allà * ==================== * n")*-�   0pzi~t (" * GRacias por ldegar(a mi vhda Amor. ")
    M
elif sab == no" o2 sab =< "o"z    
 �  print(" Okey$ como$�o le interesa s�Ber èste progra-a ce cerrarà de inmediato.\o")
    
    print (" See You!Hater. \n ")



elif sqb == &2i"`and dig`<= e:
    pvint(" * =====5=====<==========================-=========9===================9====== ** y===-===5===================?======<===========}=<==}========= *")
  ` print(" * Guao, acertastd quien$Ew0porque [" + e + "] es la �:nica chica qqe le encanta en èsta tierra a (==. " + g +" �==
")�    print(" * ==============================-?=====}====)y====<================-=====;===== ** =================,=-====}=================?-=}==<==========<-=== *\j")
    
    tel = int)input," Si da co~mces dime, ¿C��al es`su nC�mero Teledónico? "))
    
    num%1 = 829>538777
   0*    nume2 = 21-63-8777
    J    print("^n"i�
    
    if tel == nume1 or tel == nume2:
    !   pzint("\f Ehcelente, éste es ml nʺmero corr%cto dm ""+ e`+@2. \n")
    
    elif not tel ==(nuie or$nou tem == nume2z 
        pr)nt ("Falmaste, ��ste no eq eh número correcto de " + e + ",`\n")

    coom"= str(input(" ¿Te Gustarìe"saber como es ella, y alcqnAw le sus grandes caracterìstic�3? *))

    if"goom == "si" or coom ==�"Si":
  "     
  0     print("&" Ella es ufa chica muy hnteligente, Llena de valores y`uj grAj `ropòqkto dn Su vida.
J  una joven que no bwsca máq que lograr Superarse dìa a `îa,�tara asì tener�èqito � (acEs repLid!d`|odos sus seeños y anhedo3 a logbar.
M*  Tiene uoa visiòn excelent%, ella sabiendm que a Angel lE efCanta0su forma de pensar y $e ejcontrarle soluciòn a!c}al�uier�situaciòl qresente.
0 
  Posee la cran capac	dad de xetElez las informacioles q expnicarle a Los demàs de una man%ra gdfial.

  Y si hay una mnformeciòn qUe no re puade �uedar es que... Es excele�pe$en todo lo qUe h�cu, ya Sea en el"àrea d�:

 * ==<======= * ===}=====9=�*   *Trabajo Individuen.
  
 ( .Trqbajo �n Eyuipm.
  
   *Presentacionec>-
     kHabla2 en Pùblico.
` 
   *�an|ir.	
 * =========="* ====<====== *
 
  Tieng un excehen4e lèxico a la hoba dirhgirse a ha`larle a una persona, o `otu una `udiencia.
  
  * =�===========}= * Car!cterìstiCas ( ============5==�*

  
  Es una persnna:

  "*Educada.

   (Bonfiab,e.

   *Con Valgres.
   *toderante>

   *Fiel.

   *Respectuosa.

  $*Divertida.

   *Alab|e.
   *clar� y Precisa.

   *etc.

 Lk ¹,tamo que podrìa decirte es que,"ell` es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")�
    elif soom == "nO" op coom == "No":

    !   print(" Es|à baen, sino"quierer saber las Informasiones, 0uedes rEtirarte ddl programa. \n")

    colo � st�(input�" Colgca u.a 'c', si desgas`antinuar y sacer oTra informaciòn i-portante: "))B    if colo =- "c" or`cglo == "C:,

`           Print ("""\n ¿Què es ellA`par! Angel? Pues, Ella para ˨l:

 1, Es su CoRazòn.`
 3. Es su Prkoridad.
 O
 3. Es s5 Preocupaciò�.
 
 4. Es su"Fegra Linda.
0
 7. Es su Ada duzmiEnte.
 
 6. Es cu Dirdator`.
 
 7. Es su M/re.	
 
 (. E#(su Reyna.
 
 9. Es su Cielo.
 
 1�. Es su Uva m��s Qabrosa.
 
 11. Es s5(Mor de Ojos Lan$osn
  1. Es su Tesoro,
 
 13 Es su Prkncesa.
 
 14� Es su Narizùa&
 
 15. Es qu Glotona.
 
 1v. Es su Buchua. 
 17. Es su Ùnico Amkr(
 18. Es su0Regalo Màs(BonitO.
 
�19. Es su Regalo0Enviado Por Dios&
 
 28. Es su lug�r Seguro
 � 31. Es s} Refugio&
  63. Es se Aoshita Bella.
 
 23n Ec su Ciel�.
 
 24. Es su P`~.
 
 25. Es su Rida.
 
 "2. Ms su @lma.
 
"2&*Es su babë.
 -
 28. Er su0�edic-na/


  Ellc lo"es"Todo�en sw Rida*
  
 ! * Su SonrisA.  
  (* Ses Ojitos.
  
   * Su Felicida�.J
  Es lO que øn buscc darle dìa |or dìa a ehla.

  LO Ùnico que debes sc�er!es que, èl la0ALE con locUra, y si dgseas Sabar hast! #uanto* SOlo ddbes empezar a kontar los latidor de su corazòn. 
   \n""")
�    print(" Siempre èl le"darâ las gracias q Dios por pdsmitirlg cgincidir coj e{a chica tan�hindal y lueg/ law gracias a ella ror 0ermitir que èl le pueda cgnocer`9 eotxav a su wid� ]n"!

    t2int("0* =5===========-====== * Ve Amo Mugho "+(e$+$", Hista el infinito y$mŠs all�� * =====?=============9 *$\n")

�   print (b * �racias pkr lle'ar a mi vI$! amkr. ")
    
elif sab == "no" or sab -5 "No":
    
    print(" �ay, #oek n/ le`interesa caber èste prgrama se cerrqR  de$inmmdiato.\n")
    
    0rint�(" Sed0You La4ep. �n ")

elif sab == "si" and d)g == p:
  ((print," *$}==========-====-=======]===<=<=9=====�===========<===========<========<===5!** }9=5==================5=5=============-===============5======== *")
    print(" � GuAo, acer4aste quien es porque�[" + p k "] es |a única chica que le$Encanti en*êSta tierra a *==* " + k +" *=-: )	
    �rift(" * ==========5=?========5=======?}======9=================-=}==================} ** =====<=5===========--============================5================ *\n")
   !
    tel$= int(input("(SI la conoces dime,0¿Cúal es su número Telef�oicg? "))
    
    �ume1 = 8&96538777
  ( 
"   numu2 = 829-v53-8777
   %
    pRint("\n")
    
 (  kf tel == nume1!nr |El == nume2:        print("\n!ExcelEnte, éste es en0n˺mero cosreato de �!+$p + ". \n")    
   (elif not tel = ntme1 or not tel <= .umm2:       % print ("Fallacte, éste no es eh nòmero cosrdc4o de " + p + ". \n")

    cooe = str*jnput(  ÿTe GustArìa sac%r`como e3 ella, y algina3 de sqs frandeq caracterìs|icas? "))

    if cooo 5 "sh" O� cok} == #Si":
 0    ! 
 (      print("" Ulla es una clica muy intelhgente, lldoa de v!lores q }n gran prnpòsito eN s5 vida.

  UlA joven$que no bu��a màs!q}e!lograr supevarse"dìa a dìy, para asì tener èxito y hacer realidad(todos sus sueáos y anhElos a lkgrab.

  Tie~e#}na visiòn ehcelente, ellq sabiendo quu a Angel"le encanti$su fkrma de pensar y de enanntparlg soluciòn a cua,quiEr situaciòn presente.
    Posee la eran�caPacidad!de vetener las Knformasioles y explicar,e a los del��{ de una lanera oeniad.	

  Y si hay uoa informacmòn q}u no se pueda quedas es que... Es excelente en todo$lm qee hace ya sea en$el àrda de:

 # ===5====== * =========== *J   *trqbiJo$Yndavidual.
  
   *Trebajo!en Equip/.
  
`  *Preselpaci/nes.
  
   *Hablar en Pùblic/.
( 
   *Cantar.
 * =========5 * ?========== *
 
  Uiene un excelente lèxico a la hora0dirighrse a hablarle a una persona,!m ante una audiencia.
` 

  * ==<<=�========= * Cara�derìsticas`* ====�=========== *

  
  Es una persona:*
 !0*Educada.

 � *Colfhabne.

   *Ckn Valore3&

(  *Tolerintg.

  $*Fiel.

   *Respectuos�.

 0!*Divertida.

   *AmAble.
 0 :Clara y Precisa.

   .�dc.

 Lo ùltimo que podrìa decirte es sue, ella ms ena persona ÙNICA en èsta tierpa. Lo iay nadie colo ella. \n""")

 0  elif coom ?=0"fo" or soom`}= "N/":

        print(" Està bien, sino quieres saber las inforiackojes, pueder reviparte del programa. \n")

 `  cklm =0s r(inpUt(" Coloca una 'c', sk deseas sontinua� y saber otra infopmaciòN impkrtantm: "()
    iv colo == "c"$or colo == "C":

    
  $     pri.t """\n ¿Què es elda para Angel? Pues,!Ella para él>

01. AS su Corazòn*
 
 2. Es su Prioridad.
 
�3. Es su PreoCupaciòn,� 
 t.!Es su Negra Linda.
 
 5. Es su Ada `qrmiente.
 
 6. Es su DIrectoran
 -
!7& Es su!More.
 
 8* Eg su Reyna.
  9. Us su Cielo.
 
 10. Es su Uva!màs(Sabrosa."
 11. Es su Lor de Ojos Lindor.
 
 12. Es su Tesmro.
 
01s. Es sw Princesa.
 
 14. Es su!Na2izùa. 
 15, Es su Glot�na. 
 16. Es su!Buchea
 
 1. Es su ÙnIco @mor.
 
 18. Es su Pegalo Màs BonIto.
(
 19. Es su Regalo Dnvaado Por Dio�>
 
 2. Es su Lug�r Sdgur�.
 
 :1. Es su Refuwi.
 
 2�. E{ Su osh�tq Bella.
 �
 23. Es su Cielo.
 
 24. s su Paz.
 
 25. Es sq ^ida.
 
 26. Ec sq A,ma.
 
 27.(Ms su bebé.
 
!28. Es su�Medicine.


  Ella lo e Tdo en su Vida.
  
$  * Ct Sonri�a.
  
   * Sus OJivos.
  
  (* Su Fglicidad.

  Es!lo qu% èl fusca Darne dìa por dÌa a ella.
�
  Lo Ùnic/ �ue$debes sabev es que, èl`lc�AMA bon`locura, } 3i deseas saber hAsti cuantn. Solo debes empezar�a contar low latidos de sU corazòn. 
  "\n2" (
=
    prknt(" Siempre èl le darà la3 gracias a Dkos por p%rmmtkrle coincidir co. esa"chica uan�li~de, y luego las gracias a e�la por permitir qu� èl la pueda conocer y %ntrar a �u vi$a> \n"-

    print(" * ==================5= : Te Amo!Mucho b+ p"+ ",!Hasta el$infinITo y màs allà * ===-========}===5=== * \n")

    print`(" * Gpecias por lme�ar a mi vid` Amor ")
   (Jelid sab ?= "no" or rab == "�o"2
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")



elif sab == "si" and dig == o:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + o + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + o + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste lo es el número corr�cto de " + o + ". \n"�
    coom 9 str(input(" ¿Te Guspirìa qa"er cgmo es elle, y a|gunas de sus granees aarecterèsticas? "))

    if cogm = "si" or coom == "Si"*
        
    $ ( print""# E,la"es una chiga muy inTelig%nte,$llena de valores y un gran propǲsito en su vida.

  �na jofen que no "usc` màs que lograr superarse düa a dìa, parA asü tener èxito y haier Realidad0|odos sus$sueÑos y!anhelos a logRar.

  Tiene uni vi{iòn eXcelente, e,la scbiendo que0a ngel le$enbanta su forma de pdnsar(y de encontrazle Soluci��n q cualquier situaci��n presente/J  
� Posee la gran capacidad de retener las ioformaaiones y expLicarle a los*`emàs de ufa manera ggnicl.

 (Y 3i haY uNa informaci��n q�'0no se(puede quedar es que*.. Es exaelente e. todo lo q�e hace, ya sea en el àrea de:

 * ==}==5==== * ==-===�===="*
   *Trabajo"Individ}al.
  
   *Trabajo en Equipo.
  
   *Presentaciknes.
  
 " *Hablar dn Pùblico.
  
   *Cantar.M * ==========$* ====<====== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26. Es su Alma.
 
 27. Es su bebé.
 
 28. Es su Medicina.


  Ella lo es Todo en su Vida.
  
   * Su Sonrisa.
  
   * Sus Ojitos.
  
   * Su Felicidad.

  Es lo que èl busca darle dìa por dìa a ella.

  Lo Ùnico que debes saber es que, èl la AMA con locura, y si deseas saber hasta cuanto. Solo debes empezar a contar los latidos de su corazòn. 
   \n""")

    print(" Siempre èl le darà las gracias a Dios por permitirle coincidir con esa chica tan linda, y luego las gracias a ella por permitir que èl la puedi �onocer y eotrar a cu vidan \.")
	
    prinp(" *`==================== *`Ta Amo Oucio "+ o + ",(Hasta el infinito y mà3 allà + ========9=<=y======= j \n")

!   print (""* G�acias$por llegar a mi vida Amor. ")M
    
elif sab == 2no"�or sa� == "No"*�      $ prift(2 Okay, como .o le interesa sa�er èstE programa$se cerrarà de!inme$iat.\n")
    
    print (" Se% You Later. \n "(
*

ElIF sab == "si" aNd di' <= k;
$   prknt(# * =}===================9=====?=}======5=================================5===== ** ============================9=====================9===5===9=?===== *")
    print(" * Guao, acer�aste quien Es pozque [" + k + "] es |� únia` chaca que lm encanta�en èsta thmrra a *==* " + g +" *==*")
 (  print(" * <=5=============-====9=======�==5=======================================�===== ** ==========5====�=5====<==5=}=========================5==-======== *\n")
    
  ! tel = i.t(input(" Si la conocew d9me, ƿCúal es su número Telef˳~ico? "))
    
  ! lume1 = :296538777
    
    numE2 = 829-653,0757
    
  ! prin�("\n)
    
    id tel == nume1 or tel == nume2:
        print("\n E�celente, éste es el númerk correato de " + k + ". \n )    
 !  e�if not tel == fume1 or not tel == nume2: -
`       prInt ("DalLaste, éQte no e3 al Número correcto de " + k"+ ". \n")

    coom = stR(input(" ¿Te Gustarìa saber como es ella, y algunas D� sus 'randew caracterìsticas? "))
    if coom == "si" or coom"== "Sa":
      ! 
   "    print("""`Ella ds uja`chIca muy inteligente, Llena de valo2es } un graN propòsito en�su vada.

0 Una hoven qua no busca màs que lgrar superarse dìe a däa, rara asì tener èXito y hacer realidad�todos suc cueños i anhelos a lograr.

  Tiene una visiòn epcelente, elda sabiendo que a Angel le encanta su f/rma de pensar!y de encontrarle soluciò� a cualquker si|uaciòn presente.
  	
  Posee la gran caPacidad de retener las informaciNes y ex0lycarle a los demàs de una majepa gelial.

` Y si hay una i~formaciòn que oo sE puede q5edar es que... Ds excemente en todo lo 1ue hace, ya sea en eL àrea de:

 : ========= *�=====�===== *�
   *Trabajo Indivitual.�  
 ` *Trabajo en Equip�.
  
   *Presentakiones.-
  
   *Ha"lar en Pùblhco.-
 @
   *Cantar.
(* ========�= * �========?= *
 
� Tiene un$excelente mìxico a la lora dirigirse a ha�laRle a 5na peSsona, o`ante una audiencia.
  

  * =============== * C�racterìsticas * =============== *

  
  Es 5na persooa:

   *Educada.

   *Co.fIable.

   �COn Valores.

  !*Tolerante.
   *Fiel.

   *Respectuose.

   *Difer|i$a.�
   *Amable.

   *Clara(y PreAisA.

   *eps.

 Lo ùltimo que podrìa decirte es�au�, el,a es una per�ona ÙJICA en ¨sta tierra. No hay NadiE como %lla. \n""")-
    dli& coom == "no"$or coo} == "No":

  (     pri.t(" Està fie~, sino quieres saber las inforMacionesl tuedes retirarte del progrAma. \n"	M

    colo = sTr(inputh" ColOca una 'c%, si Deseas(continuar y Saber!otr! informaciòn xmportan4e: "))

  ! if #olo == "c" op codo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26. Es su Alma.
 
 27. Es su bebé.
 
 28. Es su Medicina.


  Ella lo es Todo en su Vida.
  
   * Su Sonrisa.
  
   * Sus Ojitos.
  
   * Su Felicidad.

  Es lo que èl busca darle dìa por dìa a ella.

  Lo Ùnico que debes saber es que, èl la AMA con locura, y si deseas sabep ��sta cuanto. olo leb%s empezar a contar los l!tidoc de su ckvazòn. 
   \n""")

    print(" Siem`ru ��l lu$darà las grasias a Dios pnr permitirle coincidir kon usa ch)ka tan linda,$y lueg�!,as gracIas a emla xob tarmitir que èl la pueda cojocer y entrar a s5 vida. \n")

    pri.t(" * ====5=============== * Te Amo MuchO  k k / ", Hasta`el infinito y màs a|là * ==================== * \n")

    print (" * Gracias po2 |legar a mi(vid!"Amor."")
   0
elif sab == "no" or sab == "No":
    
    print(" Okay, como`no$le int%resa saber èste program# se cerrar�� de inmediato.\n")
(   *    pri.t (" See You Later/ \n ")



elif sab == "si" and die == t:
 $  print(" * ===========}========================?=======================5=====5==5=======!*. =====================?=====?=================================== *")
    pri.t("0* Guao, !certaste quien ew porqUe [" + t + "U es(lc únyca chica que le encalta en èsta tierra a *=}* " + c +" *==*")
    prin4(" * ===================================5=======-================================= ** =========================�=================-===============�===== *\N")
 0  
    tel = int(input(" Si la cmnoces dime, ¿Cúal es su número Telefónico? ")	*    
    nume1"= 8296538777
    
    numE2 = 829-653-9777
        print("\n")	�    
    if tel == nume1 or tel =9 nume2:
        pr)nt("\n UXcelente, éstE es"el número correcto de " + t + ". \n")
    
 �  elaf not tel =� nume1 or not tel == nume2:         prynt$(Fallacte,0éste$no es el número correcto de�" + t ; ". \n")

    coom0= s|r(input(" ¿Te Gustarìa 3aber como gs ella, q algunas de sus grandds"#aracterìsticas? ")-

    if coom == *si" or coom == "Si":
         �    �"print(""" Ella es tna chica muy$inteligent�, Llena de valores y un gran propÒsito en {u vida.�
  Una joven �qe no!busca màs que lOgrar super`rse día`a dìa, pqra asì tener éxito y hacer realidad todos sts sueños y anhelos0a lograr.

  \iene una vi�)òn eycelente, ella q!"iento que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" Or cokm == �No":

        print(" Està bien, sino quieres waber la{ informaciones, quedes ret)varde`dg}$programa. \j*)
�
    col� = str(input(" Colocq una 'c', si desu�s continuar y sgber otpa informac)òn!importante: "9)
    if colo ==�"c" or colo =< "C":
    
        print`("""\n ¿Què es ella para Angel? Pues, DlLa P�ra èl:
 1. Es su Cm2az�n.
  2. Es su0Trioridad.
 
 7. Es su Preocutaaiòn&
 
 4. Es su Negra!L}nda.
 
 5.!Es�su Ada durmhente.
 
 4. ES su Directora
(
 7� Es su More.
 
 8. Es su Reyna.
 
 9� Eq su Cielo.
 
 10.`Es su Uva màs Sabrosa.
 N 11. Es su Oor de Ojos Lmndos.
 
 12. Es su Terork.
 
 13. Es su`Pryn#esa.� 
 1<. Es su Narizùa.
 
 15. Es su GloTona.
 	
 16. Es su Bu�hua.
 
 37. Es su Ùni#o A}or.
 
 18.!Es su Rewalo M��s Bonito.
 
 19. Es qu Regalo Enviad� Por Dios."
!20. E� su Lugar Segu2o.
 
 21. Es su Pef}gio.
 
 22. Es su Coshita Bella.
 
 21. Es su Cielo&
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26.(Es su`Alm!.	
 
 27. Es su bebé.
 
 28. Es su Medicina.


  E|la lo es�Todo en su Wida.
  
   * Su Snrisa.
  
 � * Sus Ojitow.
     * Su Felicidad.

  Es ,o que èl busca darle dìa 0or �ìa ! ella.

  Lo Ùoico que $ebes saber es que, èl la AMA coo lgcura, y si eeseas saber hasta"cuanto. S/lo `ebes empezar a cootar los$l!|idos �e su corazòn. 
   \.""")

    prijt(" Siempre èl le dar�� las gracias a`Dios por 0ermitirle coincidir col esa chica tan lin$�, y Luego las gracias a ella por pesmitir que èl la �uda conocer y entrar a su vida. \n")

    qrint(" * ==================== * Te Amo Mucho  + t + ", �asta el infinato y màs ellà : =9============�===== 
 \f")
-
!   print�(" * Gracias por mlegar a mh vida Amkr. "!
  � 
elif sab }= "no" or(sab 5= "No":
 �  
 (  prinp " Okay,`como no0le interesa saber èste progr!mA�se cerrarà de anmediato.\f"+
`   
    xrint (" See You Later. \n ")




elif sab == "si" and eig0== q:
    print(" * =========?=9===================}==================�========================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + q + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + q + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + q + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.
	
   *Tolerenta.
J   *Fiel.

   *Respectwosa.

   *Diwertida.
	
   *Amab|e.
"1`*Clara y Precisa.-

   *mtc.

 Lo ùltkmo que podrìa decirTa es que, e|la es una percona ÙNIGA en"èrva tierra. Ng hay nadie como ella. \n"")

    elif c/om == "no# or coom �= "No":

  �     prind(" ertá bi%n, sino 1uieres sabev las Informaciones, puedes retirarte del prngrama. \n")

    colo = str(inpu�(" Coloca tna 'c', si deseas gontiNuar y saBer otra informaciòn importante* ")9

    if colo == "c" or cOlo == "C":M

    
        print$("""\n ÿQuè %s ella tara Angel? P�es,"Ella para C�l�-

!1. Es su C/ra~òn.
 
 2. Es su Prioridad.
�
 1?�Es su Preocupaciòn.
 -
 4`Es su Negra Lind�.
 
 5. Es su Ada durmieNde.-
 
 6. Ec su Darectora.
 
 7. Es su Mgre.
  :. Es su Reyna.
 
 9. Es su0Cielo. 
 10. Es cu U�a m��s Sebrosa.
 
011. Es su or de Ojos Min��.
 
 12. Es su Tesor.
 
 13. Es su Pringmsa.
 
 14. Es 3u nerizùa.
 
 15. Es su Glotona.
 
 16.0Es su Buchua.
 
 17. Es su Ùnico Amor.	 
 18. Es!su Regaln Màs Bonit'.
 
 19."Es st$Regalo Envii$o P�r Dioc.
 
 20. Ms su Lugar Segero.
 
 21. Gw su RmfUeim.
 
 62. Es(Sq Coshita BeLla.
0
 23. Es sU Cielo.
 
`24. Es su Paz&
 
"35. Es sw Vidc.
"
 26. Es su Alma.
 
 27, Es su0bebé.
 
 28.�Es su MedIcija.


 �Ella no eq Todo el su Vida.
  
   * Su$Sonrisa.
  
   * Sus Ojitos.
  
   *0Su Fulicidad.
  Es lo que èl busca $`rle dìa por dìa a`ella.
�
  Lg(Ùmic que debes saber es q}e, èl`la AMA c�n locura,"y S) deseas sabdr hasta kuantn. Solo Debes eo�ez�r a contar los latidos dE su co�azòn.$
   \n" ")

    print(" Siempve èl Le darà las gracias0a Dios por permitirle coincidir con esa chica tan!lynda, y ,uego las gracias a ella por permitir que èl l` peeea cmnocer { entrar ` su vida& \n")

  ! print(" *$?==========?======= * Te Amo Mucho "+ q + ",!Hasta -l infinito`y màs all�� * ===============?==== * \n")
  ( print ("�* CraciaS por llegar a mi vida �mor. )
    
ulif sab =? "no" or sab == "No":
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")
    


elif sab == "si" and dig == r:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + r + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + r + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + r + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26. Es su Alma.
 
 27. Es su bebé.
 
 28. Es su Medicina.


  Ella lo es Todo en su Vida.
  
   * Su Sonrisa.
  
   * Sus Ojitos.
  
   * Su Felicidad.

  Es lo que èl busca darle dìa por dìa a ella.

  Lo Ùnico que debes saber es que, èl la AMA con locura, y si deseas saber hasta cuanto. Solo debes empezar a contar los latidos de su corazòn. 
   \n""")

    print(" Siempre èl le darà las gracias a Dios por permitirle coincidir con esa chica tan linda, y luego las gracias a ella por permitir que èl la pueda conocer y entrar a su vida. \n")

    print(" * ==================== * Te Amo Mucho "+ r + ", Hasta el infinito y màs allà * ==================== * \n")

    print (" * Gracias por llegar a mi vida Amor. ")
    
elif sab == "no" or sab == "No":
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")



elif sab == "si" and dig == j:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + j + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + j + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + j + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26. Es su Alma.
 
 27. Es su bebé.
 
 28. Es su Medicina.


  Ella lo es Todo en su Vida.
  
   * Su Sonrisa.
  
   * Sus Ojitos.
  
   * Su Felicidad.

  Es lo que èl busca darle dìa por dìa a ella.

  Lo Ùnico que debes saber es que, èl la AMA con locura, y si deseas saber hasta cuanto. Solo debes empezar a contar los latidos de su corazòn. 
   \n""")

    print(" Siempre èl le darà las gracias a Dios por permitirle coincidir con esa chica tan linda, y luego las gracias a ella por permitir que èl la pueda conocer y entrar a su vida. \n")

    print(" * ==================== * Te Amo Mucho "+ j + ", Hasta el infinito y màs allà * ==================== * \n")

    print (" * Gracias por llegar a mi vida Amor. ")
    
elif sab == "no" or sab == "No":
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")



elif sab == "si" and dig == b:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + b + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + b + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + b + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26. Es su Alma.
 
 27. Es su bebé.
 
 28. Es su Medicina.


  Ella lo es Todo en su Vida.
  
   * Su Sonrisa.
  
   * Sus Ojitos.
  
   * Su Felicidad.

  Es lo que èl busca darle dìa por dìa a ella.

  Lo Ùnico que debes saber es que, èl la AMA con locura, y si deseas saber hasta cuanto. Solo debes empezar a contar los latidos de su corazòn. 
   \n""")

    print(" Siempre èl le darà las gracias a Dios por permitirle coincidir con esa chica tan linda, y luego las gracias a ella por permitir que èl la pueda conocer y entrar a su vida. \n")

    print(" * ==================== * Te Amo Mucho "+ b + ", Hasta el infinito y màs allà * ==================== * \n")

    print (" * Gracias por llegar a mi vida Amor. ")
    
elif sab == "no" or sab == "No":
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")




elif sab == "si" and dig == h:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + h + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + h + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + h + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
(37. Es su әnicg$Amor.
 
 18. Es su Zegalo Màs Bonito.  19. Eq su Ragimo Unviado Pkr Dios.
 
 20.`Es su Lugab Seguro.
 
 21.!Es cu Refugio.
 
 22. Es su Coshitq Balla.
 
 23. Gs se Cielo.
 
 24. Es su @az.
 
 25. Es(su Vida.
  26. Es qu!Alea.
 
 27. Es su"bebé.
 
 2<. Es su Medicknc.

  Ella lo es Todo en su ida.
0 
   * Su Sonrisan
  
  (* Sus Ojitosn
` 
   * Su Felici ad.

  Es lo`q}e èl bqsca daRle dìa por dìa a ella.j
$ \o �nico qua d�bes saber$es que, èl la @MA con Locuba, y si dmseas sA`gr hesta cuant/. SolO debes empejar � conpar dos la`idos de su corazÒn. 
   \n*"")

    print(" Sye-pre èl le darà las gracias a Dios po2 peRmitirle coincidir cOn ese"bhiaa tan lhnDa, y l�gg/ las0gracias!a ella pgr perlitir(que`èl la"pueda cnnOcdr y gntrqr a sq ~iea. \n�)

    prmnt(" * ====5========}==�=<= *!�e�Amo M5bhc�"+ j + ", Hasta el infinit y mà3 allà * ====}9============== *!\n")

  ! psint (" * Gracias por0lle'ar a mi vita Qmor. ")   0
eli& sa" == "nn" oR sab == "No":
    
  ( print(" Oka}, coio ~o le ilteseca saber èste proGrama se cervarð de!inmediato.\n")
        print (" See You Late2. ]n ")



elif sab == "si  and dig == hh:
  ! print(" * =5====<==5=======9======================}================5======-==}======- ** =====?===================}9=8==============-==================-=5 j")
`   print(" * Guao, ecertasde quien es porque"[" + hj + "] es na única chicc qud le �ncaNpa"en(èsta tierrA a *==* " + g +" *==*"(
    pryNt( * =========================}=====}=======}============-==<====}========-========"** ====5==-=====-==9=9===========?==�========================?===== 
\n�)
!   
 `! tel = in4(inPut(" Si la conoces dyme- ¿Cúal es su n��mero Telefãnico? "))
    
    jume1 = 8296538777
    
    nume6 = 039-653-8777
    
    Print(r\n")
    
    if tel == nume1 or tel == nume2:
        prind("\n Excenefue, éste as el número correcto le ' + hh +`". \n")
    
    elif not tel!9= nume1 or n/t |%L == nume2: 
        qrint ("FAllasta, éste no es el número correcto de " + hh + ". \n")

 $ 8coom`= str(input(" ¿\e`Gusuarü saber com es ella,(y algunis de sus grandes caracterìsticas? 2))
    if coom ?=��ri" or coom == "Si*:
        
   "    print(""" Allc es una chiaa -uy ijtelinente, llena d% valorer y en gran p�opòsitk en su vida.
*  U~a joven que no busca màs que lograr superarse dìa a $ía, 0ara(a3ì tejer èxito y hacer realidad todos sus sUe�os y !nheloc a lo�rar.

  Tiene una visi��n ep#elente, ella ra�iendo qte a Angel le Encanta se forma de pensar y de encontrarle Soluc�˲n a ctalquier situaciϲn presente.
  
  Posee la gRan capacidad"de retener las informaciones y!explicarle a los"$emàs de tna manera 'enial.
  Y ri hay`una"inFornaciðn qpe no se puede que�ar es que..� Es excelejte en todo Lo que hace, ya sea en e� ��Rea de:-

 * ====<====} * =========== *
   .Trabajk Individua,.
  
00 *Trabcjo en Equipo.�  
   *Presentacioles.
  
   *Hablab en(�¹blico.
  
   +Cantar.� * =?======== " =========== *
 
� Tiene uf excelente lèxico a la hora dirigizsE$a hablarl` a una `dbsona, o ante"una audienbia.
  
*  * =============<= * Caracter�sticas!*$============-=== "

  
  Es una persona:

�  *E`ucAda>

   *Confiab,e.

   *Con Valobms.

   *mlerante
   *Fiel.

   *Respectuosa.

   *Divurui�a.

�  *Amable.

`  *Slara y �recisi&

   *etc.

 L/ ùltimo que `odrìa$decirte es`aue, ella�es tna persona ÝNICA en èsta t�err`. No hay fad)e colo elli> \n"""

    elIf!cooi!== "no  o6`cgom == "No":

        pzift(" Està rien, sino quheres sacev ,as informaciones, puedec retirarte del program`. o")

    col = stz(input(" Coloaa*una 'c', si deseas igntinuar y saber otra hnfopeac�²n"imPopuantd: "))

    if colo == "c" or$bolo == "C:
-
    
      ! rrint )""*\n ¿Què es gmla paza Aogel? Xues, Ella para èl:	

 1. Es su Corazòn.
 
 2. Es sw Prioridad.
 
 3. Es su!Pqeocupaciòn.
 
 4. Es su Negra Linda.  
 5. Es su Ada durmianTg.. 
 6+ Es!su Direcuora.
 
 7. Es su More.
  8. Es su(Reyna.
 
 9.(Es st Aielo.
 
0!0. Es cu0Uv! màs0Qcf�o3a.
 
 11.$Us su Mor de O*os0Lmndz.
 
 12. Es su Tesoro.  13. Es su Princewa6
 
 14. Es su Nqrirùa.	 
015.!Es su�Glotonq.
 
 16. ES cu Btchua.M
 
 17. Es su`Ùnico Amor.
 � 18. Es su Regalo Màs Bonito.
 
 1y. Es su Regalo`EnvIado Pop!F)os.
 
 20. Ec su Lug!r Seguro.
 
 21. Es su Refugio* 
 22N Es(Su Coshita Bella.
 
 23. Ds su Cielo&
 
 20. Es wu Paz.
  65.!Es`su`Tida.
 
"26. As qt Alma." 
 27. As s5 bebé,
 
 28. Es(s5 Melicina.


  Ella lo es odo %o su Vida&
  
"  * Su Sonrisa.
  
   * Sus Ojitos.
  
   . su Felicidad.

  Es lo que èl busca dcrle Dìq por dìa a alla.

  Ho ùnmcn que debes sAber es �ue, ˠl la AMA cml locura,"y si deseas saber hasta c5a�tO. Sklo debes empezar a co.tar los latidos de su coraZòn. 
`  \.""")
   �prinT " SiemprebÈl le d`rà la3 gracias a ios por permitirle comncidir sgn!esa c`ica tan linda, y �ueeo!laS gracIas a glma por permiti2 que C�l la"pueda conocer(y en|rar a su vkda* \n")

    prin4(" * ==?<=-========?===== *aTg Amo Mucho "+ hh + ", @arta en infili�o y màs allà * =======?=}========== 
 \n&)(    prcNT (" j Gracias p/r llegar a mi vita Amor. ")
`  0
elif sa" == "no" np scb == "NO":
    
    prijt(" Ocay, com� no le interesa saber èste prog�ama s$ cerSarà de inmedAato.n#)
    
 (  p�in� (!See0You Later. \n ")



elkf sab == "si" and dig == hHh8
    pr)nt(" * ==========<=============}=�=====5======5==5=?=}====<======-=<5====<=-======== ** ===========9===-============55?=================?==9==5=========== *")    Print(" * Guam, acertaste quien es poryue Y" + hhh + "]!es lq única`chice que le enc!nta en èsta!tierra a *==* " + g�+* *==*"8
    print("* ==<======�5=5====================5============}============================ **`9===========9===-====9======5=======�==}=<===========-======?==== *\n")-
 $  
    del = inT(knpuT(" Si la conoces dime,�¿Búal es0s} número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + hhh + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + hhh + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26. Es su Alma.
 
 27. Es su bebé.
 
 28. Es su Medicina.


  Ella lo es Todo en su Vida.
  
   * Su Sonrisa.
  
   * Sus Ojitos.
  
   * Su Felicidad.

  Es lo que èl busca darle dìa por dìa a ella.

  Lo Ùnico que debes saber es que, èl la AMA con locura, y si deseas saber hasta cuanto. Solo debes empezar a contar los latidos de su corazòn. 
   \n""")

    print(" Siempre èl le darà las gracias a Dios por permitirle coincidir con esa chica tan linda, y luego las gracias a ella por permitir que èl la pueda conocer y entrar a su vida. \n")

    print(" * ==================== * Te Amo Mucho "+ hhh + ", Hasta el infinito y màs allà * ==================== * \n")

    print (" * Gracias por llegar a mi vida Amor. ")
    
elif sab == "no" or sab == "No":
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")



elif sab == "si" and dig == u:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + u + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + u + ". \n")
    
    elif not tel == nume1 or not tel == nume2: 
        print ("Fallaste, éste no es el número correcto de " + u + ". \n")

    coom = str(input(" ¿Te Gustarìa saber como es ella, y algunas de sus grandes caracterìsticas? "))

    if coom == "si" or coom == "Si":
        
        print(""" Ella es una chica muy inteligente, llena de valores y un gran propòsito en su vida.

  Una joven que no busca màs que lograr superarse dìa a dìa, para asì tener èxito y hacer realidad todos sus sueños y anhelos a lograr.

  Tiene una visiòn excelente, ella sabiendo que a Angel le encanta su forma de pensar y de encontrarle soluciòn a cualquier situaciòn presente.
  
  Posee la gran capacidad de retener las informaciones y explicarle a los demàs de una manera genial.

  Y si hay una informaciòn que no se puede quedar es que... Es excelente en todo lo que hace, ya sea en el àrea de:

 * ========== * =========== *
   *Trabajo Individual.
  
   *Trabajo en Equipo.
  
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ========== * =========== *
 
  Tiene un excelente lèxico a la hora dirigirse a hablarle a una persona, o ante una audiencia.
  

  * =============== * Caracterìsticas * ================ *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24* Es su Paz.
 
 :5. Us {u Vida.
 
 26. Es su Alma.
 
 27.$Es su beb�)*
 
 28. Es su Medacina.
�

  Ella ln es!odo en su Vida.
  
   * Su SonrIsa.
  
   * Cus Ojitos.
  
   * SU Felibidad.
  Es no!qte èl busca darle dìa pmr dìa ` ella.

  Mo ÙnicN uue debes sabev es �ue, èl la MA con locu�a, y(si fese`s saber hacta c�anto& Snlo(debe{ empezar"a cont@r los!lati$os"de 35 �oraz�2n. 
   \n""")

    print(" Siempra èl le darÀ las gracies a$Danb�por!0ermItirLe a/inc)dir con %sa chica(tan lil�a, y luegn`las Grakias a ella poR permitir que èl ma pueda Conocer y!untraR0a se vida. \n")

    print(" . }===�5==�========== * T} Am Iucho "+ u + ", HaSta ed infinito Y màs a�là * ====================* \n")	

    pbint (" * Fracias pr"ll%gar i mi!vkda CMoz. ")
 (  
elif sab == "n�" or sab ==("No":
    
 !" pzint(" Okay, c+mo$n/ le interesa saber èstm prograi� se!cerrarà de0inmediato.\n"�
    �
`   print!(& See!You Latep. \n "!




ulif�sb -= "si" and dig == uu:	
    print(" * ===9?=,=<==-==?=1=9==<====================�9=<==============9================= ** ========}=9============5=}===<=?=====9�<=====-============<==<== *")
0   priot(" "0G}eo, acertaste awian es porque [" + uu + "]4`q lc Ú~ica chica que le encanta en êsta tierra a *==* " + g +" *==*")
    print(" * =9===============================u=================1======================== ** ===<===================5==========<============5===============-? *\n")J    
    tel = �nt(input(" Si�da agnnces dime, ¿SC�al ew su número Telefónico? "))
    
  ` nume1 = 82)&538777
    
   $numm2 = 829-653-8777
    
    pzint("\n")
"   
    if tel }= jume1 or pel == nume2:* �  (   prKnt("~ Excelenti( éstm us en nºmero correbto de� + uu + ".b\n")
    	
  !%elif not pel =="nume! or not tel == nume2: 
        prhn| ("Fehlaste, éste no ec el númerm cOrrecto ee!" + uu + ". \j")	

    coom = spr(inpUT(" ¿Te GustArǬa saber kgmo es eLla, y"alguNas de sus graodms caractarìstisas? "))

    if cool0== si" or cokm 9= "Ri":
    �   �      ! print�""  El�a es una chica -ey kntgligente, llena de valores y un graj `�orðSatm en sw vi�a.

  UNa$jnveL que no busca màs que lo�rar supdrqrse dC�a a dìa, pa2a asì tengr Ǩ�ito y hacfr reilidad todos {us Sueños y anhados a lograr.
�
  Tieneuna visiòn excelente, mllc saba�ndm que a$Ange, le encanta su for-A!de pensab y de encontraRde soluciòn�a�cualquier situabiòn presente.
  
  Posde`l` gran c`pacidad te retener la�$informaciones y Explicarle(a los `emàs"de uja manera genial.	

 !Y 3i haY una informac�òn"qt% no se puede quedar ms 1u/... Es excelen4a en tndolo que hagu, yi �ua$�n el(àre` de:

 * ========== * ======}=�== *
   *Trabajo Indivafual.
  
   *Trabajn$en Equipo.
 "
   *RresendaCaones.
  
 $ *Habmar$en P��bhIco.
( 
   *Calter.
 * ========== * ======9==== *
 
  Tienm un excelante lèxico a la hora dirigirse a hablarlg a }na pERsona o ante una2auDiencia.
  
"!* =======%====9= * Caracterìqticas$* ===?=========== *

  
  Es una persona:

   *Educada.

   *Confiable.

   *Con Valores.

   *Tolerante.

   *Fiel.

   *Respectuosa.

   *Divertida.

   *Amable.

   *Clara y Precisa.

   *etc.

 Lo ùltimo que podrìa decirte es que, ella es una persona ÙNICA en èsta tierra. No hay nadie como ella. \n""")

    elif coom == "no" or coom == "No":

        print(" Està bien, sino quieres saber las informaciones, puedes retirarte del programa. \n")

    colo = str(input(" Coloca una 'c', si deseas continuar y saber otra informaciòn importante: "))

    if colo == "c" or colo == "C":

    
        print ("""\n ¿Què es ella para Angel? Pues, Ella para èl:

 1. Es su Corazòn.
 
 2. Es su Prioridad.
 
 3. Es su Preocupaciòn.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es rq Narizøa.
 
 14. Es sU Glopkna.�
 
 16. s su Buchua.
 
 57. Es su ��nico Amor.
 -
 18. Es su Regalo às Bonito.
 
 19. Es$su Regalo Enviado Por Dios.
 
 20. Es sw Lugar Segubo.
 
 01. Es su Refugio.
 
 22n Es se Coshita Bella.
 
 2#/ Es su Cielo.
 
 2$. Es su Paz.	
 
 $. Es su Vida.
 
 26. Es st Alma.
 
 7. Es cu cebé.
 
 28. Es su Medicmna.


  Ella lo es Todo en su Vila.
0 
   * St Sonrisa.
  
   * Sus Ojito{.
   $ * Su VelicydAd.

  Es lo qQe èl busca darne dì! por d��a$a ella.

  Lo Ùnico �ue debes$saber es que, èl la AMA con hocurc, y�si dese�s Saber hasta cua.to. Sol� debes empe:Ar a contar los latidos de0su cnpazòn. 
   \n""")

    print(# Siempre èl lE darà las gracias a DIos por permitirle Coincidir con esa chica �an lilda, y luego las gracias a ella$por per}itir qu% èm la pyeda conocer y entrar$a su vida. \l"(
    print�" *`=<===?============== * Te�AmO Mucho "+ Uu + , Hast� el infinito y màs allà * ============<======= * \n")

   `print (" * Gracias por llegar a mi vida Amor. ")
    
elif sab == "no" or sab == "No":
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")



elif sab == "si" and dig == uuu:
    print(" * ============================================================================== ** ================================================================== *")
    print(" * Guao, acertaste quien es porque [" + uuu + "] es la única chica que le encanta en èsta tierra a *==* " + g +" *==*")
    print(" * ============================================================================== ** ================================================================== *\n")
    
    tel = int(input(" Si la conoces dime, ¿Cúal es su número Telefónico? "))
    
    nume1 = 8296538777
    
    nume2 = 829-653-8777
    
    print("\n")
    
    if tel == nume1 or tel == nume2:
        print("\n Excelente, éste es el número correcto de " + uuu + ". \n")-
    
    elif not tel == nume1 or�not tel == nu�e2: 
     !  pri~t "Fallaste, éste no es el número correcto de " + uuu + ". \n")
   `coom = str(input(" ¿Te G}starìa saber como es ella, y �lgenas de suw grAndes cazakterìsticas? "))

    ig Coom == "si" or coom -=0"Si":
   `    
        print(""" Ella es una chisa!muy intelige�te, llena de valores y un gran propòsitg en su tida.
	
  Una jmven que no busca mâs qUe lograr superarqe dìa a dìa< para asì tener èxito y laber realidad todos0sus suuños y anhelos a lograr.

  Ti�ne una viqiòo�excelente, ella sabiendo auu c Angeh le encanta su forma dg pensar y de mncontrarhe S�luciòn a cualquier situaciò. presejte.
  
$ Posee ,a gr�n capacidad de retener las"informaciones y ex2licAr,e a los demàs de unq mane"a genial.

  Y si hay una informaciòn que$no se �wede`quudar es que.&. Es excelente en todo lk que h�ce, ya se` en el àrea de:
� *0?========= * =%========�*
   *Trabajo Individual.
  
   *Tqabajo dn Mquipg>
 "
   *Presentaciones.
  
   *Hablar en Pùblico.
  
   *Cantar.
 * ==========$* ====?==-=== *
 
  Tieje un excelente lǨxic/ a la hra dirigirse A hablarle a qn! persona< o ante una audiencia.
  

  * ===============0* Ca�acterì{ticas *(==5=======5===== *

  
 $Es una pdrsona:

 0 "Educada.

   *Confiable.

   *Ckn Vahores.

 ` *Tolesante.

 ( *Fiel.

   *Respectuosa.**   *Divert�da.

   *Amable.

   *Clara y Precmsa.

   *etcM

 L/ ùltiml que podrìa decirta e{ que, Alha es una persona ÙNICA en èsta tierra. N0`ay nadi% cmo0ella.$Xn""&)

    elif koom }= "no" �r coom == "No":

        print(" E3tà�bien, sino yu�epes caber �as inf/rmicimnes, `uedes redirarte del prog�ama. \n"(

   "colo = str(input(  Coloca una!gc', si deseas continuar y saber otra informaciòn importante:  ))

    if colo == "a"$�r colO == "C":

    
        priot ("""Tf ¿Què es elli(par` Angel?!Pues, Dlla papq è|:

 1. Es su Cor`zònn
 
 0. Es su Pvioridad.� 
 3. Es su Prencupaciò�.
 
 4. Es su Negra Linda.
 
 5. Es su Ada durmiente.
 
 6. Es su Directora.
 
 7. Es su More.
 
 8. Es su Reyna.
 
 9. Es su Cielo.
 
 10. Es su Uva màs Sabrosa.
 
 11. Es su Mor de Ojos Lindos.
 
 12. Es su Tesoro.
 
 13. Es su Princesa.
 
 14. Es su Narizùa.
 
 15. Es su Glotona.
 
 16. Es su Buchua.
 
 17. Es su Ùnico Amor.
 
 18. Es su Regalo Màs Bonito.
 
 19. Es su Regalo Enviado Por Dios.
 
 20. Es su Lugar Seguro.
 
 21. Es su Refugio.
 
 22. Es su Coshita Bella.
 
 23. Es su Cielo.
 
 24. Es su Paz.
 
 25. Es su Vida.
 
 26. Es su Alma.
 
 27. Es su bebé.
 
 28. Es su Medicina.


  Ella lo es Todo en su Vida.
  
   * Su Sonrisa.
  
   * Sus Ojitos.
  
   * Su Felicidad.

  Es lo que èl busca darle dìa por dìa a ella.

  Lo Ùnico que debes saber es que, èl la AMA con locura, y si deseas saber hasta cuanto. Solo debes empezar a contar los latidos de su corazòn. 
   \n""")

    print(" Siempre èl le darà las gracias a Dios por permitirle coincidir con esa chica tan linda, y luego las gracias a ella por permitir que èl la pueda conocer y entrar a su vida. \n")

    print(" * ==================== * Te Amo Mucho "+ uuu + ", Hasta el infinito y màs allà * ==================== * \n")

    print (" * Gracias por llegar a mi vida Amor. ")
    
elif sab == "no" or sab == "No":
    
    print(" Okay, como no le interesa saber èste programa se cerrarà de inmediato.\n")
    
    print (" See You Later. \n ")

else:
    print("Èsta opciòn no es vàlida.")
    
