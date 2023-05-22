import cv2
import serial

# Inicialização da comunicação serial
ser = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta serial correta do Arduino

# Carregamento do modelo de detecção facial
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicialização da captura de vídeo
cap = cv2.VideoCapture('eu2.mp4')  # Índice '0' para câmera padrão, pode variar dependendo do sistema

while True:
    # Captura de frame
    ret, frame = cap.read()
    
    # Conversão para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detecção de faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Verifica se um rosto foi detectado
    if len(faces) > 0:
        # Envia um sinal para acender o LED no Arduino
        ser.write(b'1')  # Envia o sinal '1' para acender o LED
    else:
        # Envia um sinal para apagar o LED no Arduino
        ser.write(b'0')  # Envia o sinal '0' para apagar o LED
    
    # Loop sobre as faces detectadas
    for (x, y, w, h) in faces:
        # Desenha um retângulo ao redor da face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    # Exibir a imagem resultante
    cv2.imshow('Face Detection', frame)
    
    # Verificação de tecla de saída (pressione 'q' para sair)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Envia um sinal para apagar o LED antes de encerrar
ser.write(b'0')

# Liberação dos recursos
