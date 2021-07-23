# Context of the project
Content creation is crucial when you want to launch your site. It is necessary to identify the keywords on which you want to position yourself and in a second step to create the content associated with these keywords.

In addition to this, you need to know more about it.

The first step of your work will be the creation of the list of keywords as well as the list of questions to be answered through the articles to be created.

In addition to this, you need to know more about it.

### Step 1 - Creation of the list of keywords
To do this, you will create a function using the following query: https://importsem.com/query-google-suggestions-api-with-python/ (configure in English). At the end of this function you will retrieve a list of keywords linked to the input keyword.

Example: get_list_kw ("yoga") => ["yoga", "yoga with adriene", "yoga mat", "yoga nidra", "yoga poses", "yoga pants"] Here we will take only 5 more keywords of the one sent in the request.

### Step 2 - Identify the questions
In a second step you will retrieve the questions that users ask themselves following the words each keyword retrieved with the people_also_ask library: https://pypi.org/project/people-also-ask/

### Step 3 - Collect the answers to the questions
Still with the people_also_ask library, you will use the get_answer method to retrieve the answer to the questions in step 2.

The first 3 steps consist in creating the data which will structure the text generator. You will find an example on the structure of the expected data in the resource part.

### Step 4 - Generate text for each row of your data set
Here you will use either GPT-J or GPT-2 Large to generate content for each question-answer combination to obtain content for all of the keywords. For this you will have to use Google collab which will provide you with the appropriate development environment for this resource-intensive task.
