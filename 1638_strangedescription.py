# https://acm.timus.ru/problem.aspx?space=1&num=1638&locale=en

bookLength, coverLength, bookStart, bookFinish = input().strip().split()
bookStart, bookFinish = int(bookStart), int(bookFinish)
ateBook = bookFinish - bookStart
ateBook = abs(ateBook) + 1
print(ateBook)