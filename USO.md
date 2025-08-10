# Instruções Rápidas de Uso

## Ativar Ambiente Virtual
```bash
source .venv/bin/activate
```

## Executar Testes
```bash
python -m pytest tests/ -v
```

## Executar Mutmut
```bash
# Executar mutação
mutmut run

# Ver resultados
mutmut results --all true
```

## Resultado Esperado
- **4 mutantes gerados**
- **4 mutantes eliminados (killed)**
- **Score: 100%**

## Estrutura Final
```
.
├── src/e_commerce.py          # Função validar_voucher
├── tests/test_ecommerce.py    # 12 testes abrangentes
├── requirements.txt           # Dependências
├── .mutmut.cfg               # Configuração
└── README.md                 # Documentação
```
