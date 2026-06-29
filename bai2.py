from fastapi import FastAPI

app = FastAPI()

books = [

  {

    "id": 1,

    "title": "Python Basic",

    "author": "Nguyen Van A",

    "category": "programming",

    "year": 2022,

    "is_available": True

  },

   {

    "id": 2,

    "title": "Web API Design",

    "author": "Tran Van B",

    "category": "web",

    "year": 2021,

    "is_available": False

  }

]


@app.get('/books/available')
def books_available():
    result = []

    for i in books:
        if i["is_available"] == True:
            result.append(i)

    return result
        

@app.get("/books/borrowed")
def books_borrowed():
    result = []

    for i in books:
        if i["is_available"] == False:
            result.append(i)

    return result