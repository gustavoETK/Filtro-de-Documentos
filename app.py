
import os
import re
from pathlib import Path
from datetime import datetime

PASTA = "docs"
HOJE = datetime.today()
EXTENSOES = {".txt", ".pdf", ".docx"}

PESOS = {
    "urgente": 5, "crítico": 5, "prazo": 5,
    "atenção": 4, "emergência": 4, "revisar": 4, "analisar": 4,
    "verificar": 3, "atualizar": 3
}

def calcular_score_palavras(texto):
    texto = texto.lower()
    return sum(peso for palavra, peso in PESOS.items() if palavra in texto)

def extrair_data(texto):
    match = re.search(r"\b(\d{2}/\d{2}/\d{4})\b", texto)
    if match:
        try:
            return datetime.strptime(match.group(1), "%d/%m/%Y")
        except ValueError:
            pass
    return None

def calcular_bonus_idade(data_doc):
    if data_doc is None:
        return 0
    dias = (HOJE - data_doc).days
    semanas = dias // 7
    return min(semanas, 5)

def definir_prioridade(score):
    if score >= 10: return "ALTA"
    if score >= 6:  return "MÉDIA"
    return "BAIXA"

def extrair_texto(arquivo):
    caminho = Path(PASTA) / arquivo
    ext = caminho.suffix.lower()
    try:
        if ext == ".txt":
            return caminho.read_text(encoding="utf-8")
        elif ext == ".pdf":
            import fitz
            doc = fitz.open(caminho)
            texto = "".join(p.get_text() for p in doc)
            doc.close()
            return texto
        elif ext == ".docx":
            import docx
            doc = docx.Document(caminho)
            return "\n".join(p.text for p in doc.paragraphs)
        return ""
    except Exception as e:
        return f"[ERRO AO LER ARQUIVO: {e}]"

def processar_arquivos():
    resultados = []
    for arquivo in os.listdir(PASTA):
        caminho = os.path.join(PASTA, arquivo)
        if not os.path.isfile(caminho):
            continue
        if Path(arquivo).suffix.lower() not in EXTENSOES:
            continue

        conteudo = extrair_texto(arquivo)
        score_palavras = calcular_score_palavras(conteudo)
        data_doc = extrair_data(conteudo)
        bonus_idade = calcular_bonus_idade(data_doc)
        score_final = score_palavras + bonus_idade

        preview = conteudo.strip()[:200] + "..." if len(conteudo) > 200 else conteudo.strip()
        resultados.append({
            "arquivo": arquivo,
            "prioridade": definir_prioridade(score_final),
            "score": score_final,
            "data_doc": data_doc.strftime("%d/%m/%Y") if data_doc else "sem data",
            "conteudo": preview
        })
    return sorted(resultados, key=lambda x: x["score"], reverse=True)

def exibir_resultados(resultados):
    print("\nResultados da análise\n")
    for r in resultados:
        preview = r["conteudo"][:150] + "..." if len(r["conteudo"]) > 150 else r["conteudo"]
        print(f"[{r['prioridade']}] [Score: {r['score']}] [Data: {r['data_doc']}] {r['arquivo']}")
        print(f" {preview}\n")

def salvar_txt(resultados, filtro=None):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    if filtro:
        dados = [r for r in resultados if r["prioridade"] == filtro]
        nome_arquivo = f"relatorio_{filtro.lower().replace('é','e')}.txt"
    else:
        dados = resultados
        nome_arquivo = "relatorio_todos.txt"

    destino = Path.home() / "Downloads" / nome_arquivo
    with open(destino, "w", encoding="utf-8") as f:
        titulo = f"Relatório de análise — {filtro if filtro else 'Todos'}"
        f.write(f"{titulo}\nData: {agora}\nTotal: {len(dados)} arquivo(s)\n")
        f.write("-" * 60 + "\n\n")
        for r in dados:
            conteudo = r["conteudo"][:400] + "..." if len(r["conteudo"]) > 400 else r["conteudo"]
            f.write(f"[{r['prioridade']}] Score: {r['score']} ({r['data_doc']}) - {r['arquivo']}\n")
            f.write(f"{conteudo}\n")
            f.write("-" * 60 + "\n\n")
    print(f"Relatório salvo em: {destino}")

def menu_exportacao(resultados):
    print("=" * 60)
    print("Deseja exportar o relatório?")
    print("  [1] Somente ALTA")
    print("  [2] Somente MÉDIA")
    print("  [3] Somente BAIXA")
    print("  [4] Exportar todos")
    print("  [0] Cancelar")

    opcao = input("\nEscolha uma opção: ").strip()
    if opcao == "1":
        salvar_txt(resultados, filtro="ALTA")
    elif opcao == "2":
        salvar_txt(resultados, filtro="MÉDIA")
    elif opcao == "3":
        salvar_txt(resultados, filtro="BAIXA")
    elif opcao == "4":
        salvar_txt(resultados)
    elif opcao == "0":
        print("Exportação cancelada.")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    resultados = processar_arquivos()
    menu_exportacao(resultados)
    print("\nProcesso finalizado!")
    input("\nPressione Enter para sair...")
