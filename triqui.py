from machine import Pin as pin,ADC,I2C
from utime import sleep_ms
from ssd1306 import SSD1306_I2C
import framebuf


color = 1
color2 = 0


sensorx = ADC(pin(32))   # pines usados el 35,34,33,36, 39 , 32, 
sensory = ADC(pin(33))   # pines usados el 35,34,33,36, 39 , 32, 

sensorx.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensorx.width(ADC.WIDTH_12BIT) # establecer resolución
sensory.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensory.width(ADC.WIDTH_12BIT) # establecer resolución


ancho = 128
alto = 64
i2c = I2C(0, scl=pin(22), sda=pin(23))
oled = SSD1306_I2C(ancho, alto, i2c)
# print(i2c.scan())

boton = pin(13,pin.IN, pin.PULL_UP)
led = pin(2,pin.OUT)



matriz = [["-", "-", "-"],
          ["-","-","-"], 
          ["-","-","-"]]

matrix_length = len(matriz)
for i in range(matrix_length):
    print(matriz[i])

movimientoX = 16
movimientoY = 15
filas = 0
columnas= 0
contador = 0
cambiarLetra = 1

#m =  matriz[filas][columnas]

while True:
    
    print("volver")

    matriz2 = matriz
    
    led.value(boton.value())

    x=sensorx.read()
    y=sensory.read()
    #oled.fill(1)
    oled.text("TRIQUI", 41, 00,color)

    #verticales
    oled.line(42,10,42,64,1)
    oled.line(85,10,85,64,1)
    
    #Horizontales
    oled.line(0,27,128,27,1)
    oled.line(0,47,128,47,1)

    #x
    #oled.line(0,10,38,25,1)
    #led.line(0,25,38,10,1)

    #equis = oled.text("X", movimientoX, movimientoY,color)

  #Izquierda
    if x>3600:
      movimientoX = movimientoX-44 
      columnas = columnas-1

      if columnas<0:
        columnas = 0
      if movimientoX<16:
        movimientoX=16
      
      if matriz[filas][columnas] == "X" or matriz[filas][columnas] == "O":
          print("if")
          while matriz[filas][columnas] == "X" or matriz[filas][columnas] == "O":
              
              oled.text(matriz[filas][columnas], movimientoX, movimientoY,color) #izquierda
              oled.text(matriz[filas+1][columnas], movimientoX, movimientoY+20,color) #abajo
              oled.text(matriz[filas][columnas+1], movimientoX+44, movimientoY,color) #derecha
              oled.text(matriz[filas-1][columnas], movimientoX, movimientoY-20,color) #arriba
      else:
          oled.text(matriz[filas][columnas], movimientoX, movimientoY,color)
      
      if matriz[filas][columnas+1] != "X" and matriz[filas][columnas+1] != "O":
        oled.fill_rect(movimientoX + 44,movimientoY,10,10,color2)
      sleep_ms(400)
      
  #Derecha
    elif x<150:
      movimientoX = movimientoX+44 
      columnas = columnas+1

      if columnas>2:
        columnas = 2
      if movimientoX>104:
        movimientoX=104

      oled.text(matriz[filas][columnas], movimientoX, movimientoY,color)

      if matriz[filas][columnas-1] != "X" and matriz[filas][columnas-1] != "O":
        oled.fill_rect(movimientoX - 44,movimientoY,10,10,color2)
      sleep_ms(400)

  #Arriba
    if y>3600:
      movimientoY = movimientoY-20 
      filas = filas-1

      if filas<0:
        filas=0
      if movimientoY<15:
        movimientoY=15
          
      oled.text(matriz[filas][columnas], movimientoX, movimientoY,color)

      if matriz[filas+1][columnas] != "X" and matriz[filas+1][columnas] != "O":
        oled.fill_rect(movimientoX,movimientoY+20,10,10,color2)
      sleep_ms(400)
      
      
  #Abajo    
    elif y<150:
      movimientoY = movimientoY+20
      filas = filas+1
      
      if filas>2:
        filas=2
      if movimientoY>56:
        movimientoY=56

      oled.text(matriz[filas][columnas], movimientoX, movimientoY,color)
      if matriz[filas-1][columnas] != "X" and matriz[filas-1][columnas] != "O":
        oled.fill_rect(movimientoX,movimientoY-20,10,10,color2)
      sleep_ms(400)
      
      if boton.value()==0:
        matriz[filas][columnas]="X"
        sleep_ms(150)
        
#         #Filas
#     if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X":
#       oled.line(0,18,128,18,1)
#     
#     if matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X":
#       oled.line(0,38,128,38,1)
# 
#     if matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X":
#       oled.line(0,58,128,58,1)
# 
#     #Columnas
#     if matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X":
#       oled.line(20,10,20,64,1)
#     
#     if matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X":
#       oled.line(63,10,63,64,1)
#     
#     if matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X":
#       oled.line(106,10,106,64,1)
#     
#     #Diagonales
#     if matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X":
#       oled.line(0,10,128,64,1)
# 
#     if matriz[2][0] == "X" and matriz[1][1] == "X" and matriz[0][2] == "X":
#       oled.line(0,64,128,10,1)
    
    #_________________________________________________________________________________________
      
    if boton.value()==0:
        
        matriz[filas][columnas]="X"
        sleep_ms(400)
        
        #Filas
        if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X":
          oled.line(0,18,128,18,1)
        
        if matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X":
          oled.line(0,38,128,38,1)

        if matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X":
          oled.line(0,58,128,58,1)

        #Columnas
        if matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X":
          oled.line(20,10,20,64,1)
        
        if matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X":
          oled.line(63,10,63,64,1)
        
        if matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X":
          oled.line(106,10,106,64,1)
        
        #Diagonales
        if matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X":
          oled.line(0,10,128,64,1)

        if matriz[2][0] == "X" and matriz[1][1] == "X" and matriz[0][2] == "X":
          oled.line(0,64,128,10,1)
        
        oled.show()
        
        cambiarLetra = cambiarLetra + 1
        
        modulo = cambiarLetra % 2
     
        while modulo == 0:
            
            x=sensorx.read()
            y=sensory.read()
            
            #Izquierda
            if x>3600:
              movimientoX = movimientoX-44 
              columnas = columnas-1

              if columnas<0:
                columnas = 0
              if movimientoX<16:
                movimientoX=16
                
              if matriz[filas][columnas] == "X" or matriz[filas][columnas] == "O":
                  print("if")
                  
                  reubicacion = matriz[filas][columnas]
                  
                  while reubicacion == "X" or reubicacion == "O":
                      
                      oled.text(matriz[filas][columnas], movimientoX, movimientoY,color) #izquierda
                      reubicacion = matriz[filas][columnas]
                      oled.text(matriz[filas+1][columnas], movimientoX, movimientoY+20,color) #abajo
                      reubicacion = matriz[filas][columnas]
                      oled.text(matriz[filas][columnas+1], movimientoX+44, movimientoY,color) #derecha
                      reubicacion = matriz[filas][columnas]
                      oled.text(matriz[filas-1][columnas], movimientoX, movimientoY-20,color) #arriba                 
                      reubicacion = matriz[filas][columnas]
                      
              else:
                  oled.text(matriz[filas][columnas], movimientoX, movimientoY,color)
              
              print("salio")
              
              if matriz[filas][columnas+1] != "X" and matriz[filas][columnas+1] != "O":
                oled.fill_rect(movimientoX + 44,movimientoY,10,10,color2)
              sleep_ms(400)
              
          #Derecha
            elif x<150:
                
                print(":O")
                movimientoX = movimientoX+44 
                columnas = columnas+1

                if columnas>2:
                    columnas = 2
                    
                if movimientoX>104:
                    movimientoX=104

                oled.text(matriz[filas][columnas], movimientoX, movimientoY,color)

                if matriz[filas][columnas-1] != "X" and matriz[filas][columnas-1] != "O":
                    oled.fill_rect(movimientoX - 44,movimientoY,10,10,color2)
                    sleep_ms(400)

          #Arriba
            if y>3600:
              movimientoY = movimientoY-20 
              filas = filas-1

              if filas<0:
                filas=0
              if movimientoY<15:
                movimientoY=15
                  
              oled.text(matriz[filas][columnas], movimientoX, movimientoY,color)

              if matriz[filas+1][columnas] != "X" and matriz[filas+1][columnas] != "O":
                oled.fill_rect(movimientoX,movimientoY+20,10,10,color2)
              sleep_ms(400)
              
              
          #Abajo    
            elif y<150:
              movimientoY = movimientoY+20
              filas = filas+1
              
              if filas>2:
                filas=2
              if movimientoY>56:
                movimientoY=56

              oled.text(matriz[filas][columnas], movimientoX, movimientoY,color)
              if matriz[filas-1][columnas] != "X" and matriz[filas-1][columnas] != "O":
                oled.fill_rect(movimientoX,movimientoY-20,10,10,color2)
              sleep_ms(400)
              print(":)")
      
            if matriz[filas][columnas] != "X" and matriz[filas][columnas] != "O":

                if boton.value()==0:
                    
                    matriz[filas][columnas]="O"
                    sleep_ms(150)
                    cambiarLetra = cambiarLetra + 1
                    
                    modulo = cambiarLetra%2
                    
                    if matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O":
                      oled.line(0,18,128,18,1)
                    
                    if matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O":
                      oled.line(0,38,128,38,1)

                    if matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O":
                      oled.line(0,58,128,58,1)

                    #Columnas
                    if matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O":
                      oled.line(20,10,20,64,1)
                    
                    if matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O":
                      oled.line(63,10,63,64,1)
                    
                    if matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O":
                      oled.line(106,10,106,64,1)
                    
                    #Diagonales
                    if matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O":
                      oled.line(0,10,128,64,1)

                    if matriz[2][0] == "O" and matriz[1][1] == "O" and matriz[0][2] == "O":
                      oled.line(0,64,128,10,1)  

                    #Filas
                    if matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O":
                      oled.line(0,18,128,18,1)
                    
                    if matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O":
                      oled.line(0,38,128,38,1)

                    if matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O":
                      oled.line(0,58,128,58,1)

                    #Columnas
                    if matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O":
                      oled.line(20,10,20,64,1)
                    
                    if matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O":
                      oled.line(63,10,63,64,1)
                    
                    if matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O":
                      oled.line(106,10,106,64,1)
                    
                    #Diagonales
                    if matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O":
                      oled.line(0,10,128,64,1)

                    if matriz[2][0] == "O" and matriz[1][1] == "O" and matriz[0][2] == "O":
                      oled.line(0,64,128,10,1)
                   
            oled.text(matriz[filas][columnas], movimientoX, movimientoY,color)
            oled.show()
            
        
    #_________________________________________________________________________________________



    oled.text(matriz[filas][columnas], movimientoX, movimientoY,color)
    oled.show()
