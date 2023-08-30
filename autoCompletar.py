def searchWordsStarting(root, prefix):
    if root is None:
        return []

    results = []

    # Verificar se o prefixo é menor que o nó atual para otimizar a busca
    if prefix <= root.key:
        if root.key.startswith(prefix):
            results = [root.key]

        left_results = searchWordsStarting(root.left, prefix) 
        results = results + left_results

    right_results = searchWordsStarting(root.right, prefix)
    results = results + right_results

    return results

