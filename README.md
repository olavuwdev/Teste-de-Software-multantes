# Teste de Software - Análise de Mutantes

Este projeto contém uma implementação da função `validar_voucher` para um e-commerce, junto com testes abrangentes que eliminam os mutantes gerados pelo mutmut.

## Estrutura do Projeto

```
.
├── src/
│   ├── __init__.py
│   └── e_commerce.py          # Implementação da função validar_voucher
├── tests/
│   ├── __init__.py
│   └── test_ecommerce.py      # Testes para eliminar mutantes
├── requirements.txt           # Dependências do projeto
├── .mutmut.cfg               # Configuração do mutmut
└── README.md                 # Este arquivo
```

## Função Implementada

A função `validar_voucher(valor: float) -> bool` verifica se um valor de compra é elegível para um voucher de desconto.

**Regra de Negócio**: O voucher só é válido para compras com valor entre R$ 50,00 e R$ 500,00, inclusive.

## Como Executar

### Instalar Dependências
```bash
pip install -r requirements.txt
```

### Executar Testes
```bash
python -m pytest tests/
```

### Executar Mutmut
```bash
# Executar mutação
mutmut run

# Ver resultados
mutmut results
```

## Testes Implementados

Os testes foram projetados para eliminar todos os mutantes possíveis gerados pelo mutmut:

1. **Testes de Limites**: Valores exatos nos limites inferior (50.00) e superior (500.00)
2. **Testes de Valores Inválidos**: Valores abaixo de 50.00 e acima de 500.00
3. **Testes de Valores Válidos**: Valores dentro do intervalo
4. **Testes de Precisão**: Valores com diferentes precisões decimais
5. **Testes de Valores Extremos**: Infinito, -infinito e NaN
6. **Testes de Valores Inteiros**: Conversão implícita de int para float

## Análise de Mutantes

O objetivo é que todos os mutantes sejam eliminados pelos testes, resultando em um score de 100% no `mutmut results`.
