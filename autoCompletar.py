def searchWordsStarting(root, prefix):
    results = []
    if root is None:
        return results
        
    if root.key.startswith(prefix):
        results.append(root.key)
        
    if prefix < root.key:
        results.extend(searchWordsStarting(root.left, prefix))
    else:
        results.extend(searchWordsStarting(root.right, prefix))
        
    return results
