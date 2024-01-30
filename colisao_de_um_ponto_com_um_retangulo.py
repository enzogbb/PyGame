def colisao_ponto_retangulo(x_ponto, y_ponto, x_retangulo, y_retangulo, largura_retangulo, altura_retangulo):
    # Calcula as coordenadas do canto inferior direito do retângulo
    x_retangulo_direito = x_retangulo + largura_retangulo
    y_retangulo_inferior = y_retangulo + altura_retangulo
    
    # Verifica se o ponto está dentro do retângulo
    if x_ponto >= x_retangulo and x_ponto <= x_retangulo_direito and y_ponto >= y_retangulo and y_ponto <= y_retangulo_inferior:
        return True
    else:
        return False