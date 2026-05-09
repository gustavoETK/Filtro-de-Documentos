<div align="center">

# 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![PyMuPDF](https://img.shields.io/badge/PyMuPDF-fitz-orange?style=flat)
![python-docx](https://img.shields.io/badge/python--docx-0.8+-blue?style=flat)

- **Python 3.8+**
- [`os`](https://docs.python.org/3/library/os.html), [`re`](https://docs.python.org/3/library/re.html), [`pathlib`](https://docs.python.org/3/library/pathlib.html), [`datetime`](https://docs.python.org/3/library/datetime.html) — bibliotecas padrão
- [`PyMuPDF (fitz)`](https://pymupdf.readthedocs.io/) — leitura de PDFs
- [`python-docx`](https://python-docx.readthedocs.io/) — leitura de arquivos Word
 
</div>
---

# 📂 Automação com Python — Analisador de Documentos

> Ferramenta de automação que lê, analisa e prioriza documentos (`.txt`, `.pdf`, `.docx`) com base em palavras-chave e data de criação, gerando relatórios organizados automaticamente.

# 🧠 Como funciona

O script percorre uma pasta chamada `docs/`, lê o conteúdo de cada arquivo suportado e calcula uma pontuação de prioridade com base em dois critérios:

- **Palavras-chave** presentes no conteúdo (ex: `urgente`, `crítico`, `prazo`)
- **Idade do documento** — arquivos mais antigos recebem bônus de prioridade

Ao final, exibe os resultados ordenados por score e permite exportar um relatório `.txt` para a pasta `Downloads`.

---

## 📁 Estrutura do Projeto

```
Automação-com-Python/
│
├── docs/                  # Pasta com os documentos a serem analisados
│   └── exemplos de txt, pdf e docx
│
├── README.md
└── app.py                 # Script principal
```

---

## ⚙️ Funcionalidades

- ✅ Leitura de arquivos `.txt`, `.pdf` e `.docx`
- ✅ Análise de conteúdo por palavras-chave ponderadas
- ✅ Bônus de prioridade por antiguidade do documento
- ✅ Classificação automática: **ALTA**, **MÉDIA** ou **BAIXA**
- ✅ Exportação de relatório `.txt` filtrado por prioridade
- ✅ Menu interativo no terminal

---

## 🔑 Palavras-chave e Pesos

| Palavra-chave | Peso |
|---------------|------|
| `urgente`, `crítico`, `prazo` | 5 |
| `atenção`, `emergência`, `revisar`, `analisar` | 4 |
| `verificar`, `atualizar` | 3 |

> O bônus por idade é somado ao score de palavras, com no máximo +5 pontos (1 ponto por semana de antiguidade).

**Critérios de classificação:**

| Score | Prioridade |
|-------|------------|
| ≥ 10 | 🔴 ALTA |
| 6 – 9 | 🟡 MÉDIA |
| < 6 | 🟢 BAIXA |

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/gustavoETK/Automa-o-com-Python.git
cd Automa-o-com-Python
```

### 2. Instale as dependências

```bash
pip install pymupdf python-docx
```

> `pymupdf` é necessário para leitura de PDFs. `python-docx` para arquivos `.docx`. Arquivos `.txt` não requerem bibliotecas adicionais.

### 3. Adicione seus documentos

Coloque os arquivos que deseja analisar dentro da pasta `docs/`.

### 4. Execute o script

```bash
python app.py
```

### 5. Escolha a exportação

O menu interativo permite exportar o relatório filtrado por prioridade ou exportar todos de uma vez.

```
Deseja exportar o relatório?
 [1] Somente ALTA
 [2] Somente MÉDIA
 [3] Somente BAIXA
 [4] Exportar todos
 [0] Cancelar
```

O relatório será salvo automaticamente em `~/Downloads/`.

---

## 📋 Exemplo de saída

```
Resultados da análise

[ALTA]  [Score: 12] [Data: 15/03/2025] contrato_urgente.docx
  Documento crítico com prazo para revisão até o final do mês...

[MÉDIA] [Score: 7]  [Data: sem data]  pendencias.txt
  Verificar itens listados e atualizar planilha de controle...

[BAIXA] [Score: 2]  [Data: 10/01/2025] notas_gerais.pdf
  Anotações diversas sobre o projeto em andamento...
```

---

## 👤 Autor

**Gustavo** 

---

> 💡 **Dica:** Adapte a lista de `PESOS` no início do `app.py` para incluir palavras-chave relevantes ao seu contexto de uso.
