# Day39  Personal Search Engine 

documents = []

while True:

    print("\nPERSONAL SEARCH ENGINE")
    print("1. Add Document")
    print("2. Search Documents")
    print("3. View All Documents")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        title = input("Enter document title: ")

        content = input(
            "Enter document content: "
        ).lower()

        document = {
            "title": title,
            "content": content
        }

        documents.append(document)

        print("\nDocument indexed successfully.")

    elif choice == "2":

        if len(documents) == 0:
            print("\nNo documents available.")
            continue

        query = input(
            "\nEnter search query: "
        ).lower()

        query_words = query.split()

        results = []

        for document in documents:

            score = 0

            for word in query_words:

                score += (
                    document["content"]
                    .count(word)
                )

            if score > 0:

                results.append({
                    "title": document["title"],
                    "score": score
                })

        if len(results) == 0:

            print("\nNo matching documents found.")

        else:

            results.sort(
                key=lambda item: item["score"],
                reverse=True
            )

            print("\nSEARCH RESULTS\n")

            for result in results:

                print(
                    f"{result['title']} "
                    f"| Relevance Score: "
                    f"{result['score']}"
                )

    elif choice == "3":

        if len(documents) == 0:
            print("\nNo documents indexed.")

        else:

            print("\nINDEXED DOCUMENTS\n")

            for document in documents:

                print(
                    f"Title: {document['title']}"
                )

                print(
                    f"Content: "
                    f"{document['content']}\n"
                )

    elif choice == "4":

        print("\nClosing Personal Search Engine.")
        break

    else:
        print("\nInvalid choice.")
        