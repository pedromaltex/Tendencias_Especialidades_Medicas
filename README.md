# 🎯 Colocações Especialidades Médicas 🩺

Bem-vindo à **aplicação interativa que torna os dados de colocações médicas fascinantes!** Explora a evolução das colocações em diferentes especialidades médicas em Portugal e descobre como te posicionas em relação aos últimos colocados por ano.

---

## 🌟 Funcionalidades Principais

* Escolhe as tuas **especialidades favoritas** e descobre tendências ao longo dos anos.
* Filtra por **instituição/local** e vê o panorama detalhado.
* Usa o slider para indicar a **tua posição** e vê imediatamente como te comparas com os últimos colocados.
* Gráficos interativos que tornam a análise **visual e intuitiva**.
* Linha horizontal a destacar a tua posição para rápida referência.
* Design responsivo e **gráfico full-width** para uma experiência envolvente.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Streamlit**: interface web super interativa
* **Pandas**: manipulação eficiente de dados
* **Plotly**: gráficos dinâmicos e interativos

---

## 📂 Estrutura do Projeto

```
.
├── app.py                 # Código principal da aplicação Streamlit
├── config.py              # Configuração, incluindo caminho para o CSV
├── dados.csv              # CSV com os dados das colocações
└── README.md
```

---

## 🚀 Como Executar

1. **Instalar dependências**

```bash
pip install streamlit pandas plotly
```

2. **Executar a aplicação**

```bash
streamlit run app.py
```

3. Abre o navegador e **mergulha nos dados**!

---

## 📊 CSV Esperado

O CSV deve conter as seguintes colunas obrigatórias:

* `Ano`: Ano da colocação
* `Especialidade`: Nome da especialidade médica
* `Local`: Instituição ou local
* `Numero_Ordem`: Posição do último colocado

---

## 👏 Créditos

Desenvolvido por **Pedro Maltez** | Dados fornecidos por **Fábio Fernandes**

---

## 💡 Observações

* Combina múltiplas especialidades e locais para descobrir padrões interessantes.
* A linha da **posição do utilizador** oferece uma visualização imediata da tua colocação comparativa.

Prepara-te para explorar dados médicos de uma forma **interativa e envolvente!**
