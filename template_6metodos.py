import cv2

#se leen las imagenes de entrada  
orig = cv2.imread("Cheems.png")

#crea una copia de la imagen 
image = orig.copy()

template = cv2.imread("CheemsTemplate.png")

#transforma la imagen de cvr a escala de grises 
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

#son los diferentes vectores que se puede hacer en las imagenes 
methods = [cv2.TM_SQDIFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]

        
#recorre cada uno de los procedimientos 
for method in methods:
    #realiza los procedimientos necesarios
    res = cv2.matchTemplate(image_gray, template_gray, method=method)
    #visualiza el valor mas alto o el valor mas bajo para un mejor emparejamiento
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)

    #sirve para saber que si se usa el metodo TM_SQDIFF o TM_SQDIFF_NORMED,
    # y entrega las cordenadas del valor minimo  
    if method == cv2 .TM_SQDIFF or method == cv2.TM_SQDIFF_NORMED:
        x1,y1 = min_loc
        x2,y2 = min_loc[0] + template.shape[1],min_loc[1] + template.shape[0]
    #Da las cordenadas en el valor maximo 
    else:
        x1,y1 = max_loc
        x2,y2 = max_loc[0] + template.shape[1],max_loc[1] + template.shape[0]


    #crea un rectangulo en la pocicion de la imagen cortada
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3 )

    #visualiza las imagenes
    cv2.imshow("Image", image)
    cv2.imshow("Template", template)
    #es la copia de la image
    image = orig.copy()
    cv2.waitKey(0)
cv2.destroyAllWindows()



