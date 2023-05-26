# Question 18

### **Question:**

> **_A website requires the users to input username and password to register. Write a program to check the validity of password input by users._**

> **_Following are the criteria for checking the password:_**

- **_At least 1 letter between [a-z]_**
- **_At least 1 number between [0-9]_**
- **_At least 1 letter between [A-Z]_**
- **_At least 1 character from [$#@]_**
- **_Minimum length of transaction password: 6_**
- **_Maximum length of transaction password: 12_**

> **_Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma._**

> **_Example_**

> **_If the following passwords are given as input to the program:_**

```
ABd1234@1,a F1#,2w3E*,2We3345
```

> **_Then, the output of the program should be:_**

```
ABd1234@1
```

---

### Hints:

> **_In case of input data being supplied to the question, it should be assumed to be a console input._**

---


# Question 19

### **Question:**

> **_You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:_**

- **_1: Sort based on name_**
- **_2: Then sort based on age_**
- **_3: Then sort by score_**

> **_The priority is that name > age > score._**

> **_If the following tuples are given as input to the program:_**

```
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
```

> **_Then, the output of the program should be:_**

```
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
```

---

### Hints:

> **_In case of input data being supplied to the question, it should be assumed to be a console input.We use itemgetter to enable multiple sort keys._**

---

# Question 20

### **Question:**

> **_Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n._**

> **_Suppose the following input is supplied to the program:_**

```
7
```

> **_Then, the output should be:_**

```
0
7
14
```
---

### Hints:

> **_Consider use class, function and comprehension._**

---