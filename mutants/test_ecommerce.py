import pytest
from e_commerce import validar_voucher


class TestValidarVoucher:
    """Testes para a função validar_voucher"""
    
    def test_valor_exato_limite_inferior(self):
        """Testa valor exato no limite inferior (50.00)"""
        assert validar_voucher(50.00) == True
    
    def test_valor_exato_limite_superior(self):
        """Testa valor exato no limite superior (500.00)"""
        assert validar_voucher(500.00) == True
    
    def test_valor_abaixo_limite_inferior(self):
        """Testa valor abaixo do limite inferior"""
        assert validar_voucher(49.99) == False
        assert validar_voucher(0.00) == False
        assert validar_voucher(-10.00) == False
    
    def test_valor_acima_limite_superior(self):
        """Testa valor acima do limite superior"""
        assert validar_voucher(500.01) == False
        assert validar_voucher(1000.00) == False
    
    def test_valor_dentro_do_intervalo(self):
        """Testa valores dentro do intervalo válido"""
        assert validar_voucher(100.00) == True
        assert validar_voucher(250.50) == True
        assert validar_voucher(499.99) == True
    
    def test_valor_limite_inferior_mais_um_centavo(self):
        """Testa valor um centavo acima do limite inferior"""
        assert validar_voucher(50.01) == True
    
    def test_valor_limite_superior_menos_um_centavo(self):
        """Testa valor um centavo abaixo do limite superior"""
        assert validar_voucher(499.99) == True
    
    def test_valor_limite_inferior_menos_um_centavo(self):
        """Testa valor um centavo abaixo do limite inferior"""
        assert validar_voucher(49.99) == False
    
    def test_valor_limite_superior_mais_um_centavo(self):
        """Testa valor um centavo acima do limite superior"""
        assert validar_voucher(500.01) == False
    
    def test_valores_com_precisao_decimal(self):
        """Testa valores com diferentes precisões decimais"""
        assert validar_voucher(50.001) == True
        assert validar_voucher(499.999) == True
        assert validar_voucher(49.999) == False
        assert validar_voucher(500.001) == False
    
    def test_valores_inteiros(self):
        """Testa valores inteiros"""
        assert validar_voucher(50) == True
        assert validar_voucher(500) == True
        assert validar_voucher(49) == False
        assert validar_voucher(501) == False
    
    def test_valores_extremos(self):
        """Testa valores extremos"""
        assert validar_voucher(float('inf')) == False
        assert validar_voucher(float('-inf')) == False
        # NaN não deve ser considerado válido
        import math
        assert validar_voucher(float('nan')) == False
