books = []
# { "book_id": "1", "book_name": "파이썬책" }
# [ {},{},{} ]
while True:
    print("== 도서관리 시스템 ==")
    print("1. 도서 등록")
    print("2. 전체 도서 조회")
    print("3. 도서 삭제")
    print("q. 종료")

    selected_menu = input("메뉴를 선택 >>")
    if selected_menu == "1":
        print("도서 등록 메뉴")
        book_id = input("도서 아이디 >")
        book_name = input("도서 이름 >")

        # [{},{},{}..{}]
        is_duplicated = False
        for book in books:
            if book["book_id"] == book_id:
                is_duplicated = True
                print("중복 아이디입니다")
                break

        if is_duplicated:
            continue

        new_book = {
            "book_id": book_id,
            "book_name": book_name
        }

        books.append(new_book)
        print(f"{book_name} 등록 완료")

    elif selected_menu == "2":
        # bool([]) -> False
        # if [] -> if False
        # if 0 -> if False
        # if "" -> if False
        if not books:
            print("등록된 도서가 없습니다")
            continue

        for book in books:
            book_id, name = book["book_id"], book["book_name"]
            print(f"{book_id}: {name}")

    elif selected_menu == "3":
        target_id = input("삭제한 도서 id 입력 >")

        found = False
        for book in books:
            if book["book_id"] == target_id:
                found = True
                books.remove(book)
                print(f"{book["book_id"]}번호 삭제 완료")

        if not found:
            print("해당 id의 도서는 존재하지 않습니다.")

    elif selected_menu == "q":
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력입니다.")
        continue