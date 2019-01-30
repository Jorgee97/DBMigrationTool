# DatabaseMigrationTool
This is a python project which I developed for learning purposes, It still need a lot to be done, and the code is not as clean as it should be, even tho, I spect that I could help someone at any moment.

The main concept of the project is being able to migrate databases like SQLServer to PostgreSQL, or from MySQL to PostgreSQL, or any other.

# Screenshot
![alt text](https://github.com/Jorgee97/DBMigrationTool/tree/master/pictures/gui.png)

# Current Features
At the moment the project only provides a solution to migrate from SQLServer to PostgreSQL. What does this cover?
- Migration of tables, this includes constrains (primary and foreign keys)
- Migration of data, this will migrate any data from SQLServer tables to the newly created PostgreSQL ones.

# Future Features
I will be working on the next features:
- Migration of Views (this is missing on the actual state of the project)
- Add new available migrations, this would include mssql_mysql, mysql_postgresql, postgresql_mysql, postgresql_mssql
- The code will be getting some refactoring for better aproach SOLID techniques

If someone wants to help with it, it would be awesome, I know the code is not the best, but any pull request will be of huge help, also recommendations or critic.

# Notes and comments
As I said before, this is a learning project, but my intent is to make it usefull for everybody, as a learning purpose, or bussines purpose.

If you want to leave some recommendations or just want to chat I will be glad to hear, just send me an email to ingjorgegomez@outlook.com.
Does this project was help you on any way and want to thank me? well, you can send me an email or if you feel it, you can buy me a coffee  http://ko-fi.com/jorgegomez

# License
```
  MIT License

  Copyright (c) 2019 Jorge Gomez

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
```
