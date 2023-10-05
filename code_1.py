import string

def cleanToken(token):
    # Remove punctuation and convert to lowercase
    cleaned_token = token.translate(str.maketrans('', '', string.punctuation)).lower()
    return cleaned_token
def buildInvertedIndex(docs):
    inverted_index = {}
    for doc_id, doc_text in enumerate(docs):
        tokens = doc_text.split()
        for token in tokens:
            cleaned_token = cleanToken(token)
            if cleaned_token not in inverted_index:
                inverted_index[cleaned_token] = set()
            inverted_index[cleaned_token].add(doc_id)
    return inverted_index
def findQueryMatches(index, query):
    query_terms = query.split()
    matching_docs = set()
    for term in query_terms:
        cleaned_term = cleanToken(term)
        if cleaned_term in index:
            matching_docs.update(index[cleaned_term])
    return list(matching_docs)
def readDocs(dbfile):
    with open(dbfile, 'r') as file:
        docs = file.readlines()
    return docs
def mySearchEngine(dbfile):
    # Read and process the database file
    documents = readDocs(dbfile)
    inverted_index = buildInvertedIndex(documents)

    while True:
        # Take input
        query = input("Enter query sentence (RETURN/ENTER to quit): ")

        # Check for quit condition
        if not query:
            break

        # Perform the query and display the results
        matches = findQueryMatches(inverted_index, query)
        print(f"Found {len(matches)} matching pages")
        for doc_id in matches:
            print(f"Document {doc_id}: {documents[doc_id]}")

if __name__ == "__main__":
        mySearchEngine("sampleWebsiteData.txt")
