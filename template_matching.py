from re import template
import cv2
     
#se leen las imagenes de entrada       
image = cv2.imread("Gato.png")
template =cv2.imread("GatoTemplate.png")

#transforma la imagen de cvr a escala de grises 
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

#realiza los procedimientos necesarios 
res = cv2.matchTemplate(image_gray, template_gray, cv2.TM_SQDIFF)

#visualiza el valor mas alto o el valor mas bajo para un mejor emparejamiento 
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

#imprime en consola los valores minimo y maximo y en X,Y
print(min_val, max_val, min_loc, max_loc)

#ayuda a dibujar un rectangulo en la imagen y da la pocicion en X,Y
x1,y1 = min_loc
x2,y2 = min_loc[0] + template.shape[1], min_loc[1] + template.shape[0]

#crea un rectangulo en la pocicion de la imagen cortada
cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),3)

#visualiza las imagenes 
cv2.imshow("Cheems", image)
cv2.imshow("CheemsTemplate",template)
cv2.waitKey(0)
cv2.destroyAllWindows()