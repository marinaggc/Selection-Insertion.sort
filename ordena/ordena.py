import time
import sys
import os

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        conteudo = f.read()
        tokens = conteudo.replace(',', ' ').split()
        return list(map(int, tokens))

def salvar_ordenado(nome_arquivo_saida, lista):
    with open(nome_arquivo_saida, 'w') as f:
        f.write('\n'.join(map(str, lista)))  # cada número em uma nova linha

def main():
    if len(sys.argv) != 2:
        print("❌ Uso: python ordena.py <arquivo.in>")
        return

    nome_arquivo = sys.argv[1]

    try:
        original = ler_arquivo(nome_arquivo)
    except Exception as e:
        print(f"[ERRO] Falha ao ler {nome_arquivo}: {e}")
        return

    print(f"\n🧪 Testando arquivo: {nome_arquivo} - {len(original)} números")

    # Selection Sort
    arr1 = original[:]
    inicio1 = time.time()
    selection_sort(arr1)
    fim1 = time.time()
    tempo1 = (fim1 - inicio1) * 1000

    nome_saida1 = f"saida_selection_{os.path.basename(nome_arquivo).replace('.in', '')}.txt"
    salvar_ordenado(nome_saida1, arr1)

    # Insertion Sort
    arr2 = original[:]
    inicio2 = time.time()
    insertion_sort(arr2)
    fim2 = time.time()
    tempo2 = (fim2 - inicio2) * 1000

    nome_saida2 = f"saida_insertion_{os.path.basename(nome_arquivo).replace('.in', '')}.txt"
    salvar_ordenado(nome_saida2, arr2)

    print(f"  Selection Sort: {tempo1:.3f} ms → Salvo em '{nome_saida1}'")
    print(f"  Insertion Sort: {tempo2:.3f} ms → Salvo em '{nome_saida2}'")

    if tempo1 < tempo2:
        print("  → Selection Sort foi mais rápido.")
    elif tempo2 < tempo1:
        print("  → Insertion Sort foi mais rápido.")
    else:
        print("  → Ambos tiveram tempos iguais.")

if __name__ == "__main__":
    main()
