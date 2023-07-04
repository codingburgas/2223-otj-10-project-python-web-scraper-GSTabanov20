[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ZTfGFEPa)
# 2223-10: On the job training (OTJ) project

# Library Managment System
This document describes the OTJ project for 10th graders. **It will be updated frequently**.

# 1. Assignment Goals
A library management system (LMS) aims to automate all library activities. It is a software that helps manage all the primary functions of library management. With the help of a library management system, we can organize, handle, and maintain the record of numerous books and the members in a comprehensive and systematic way.

A librarian can use this software to track the number of books in the library. They can also use it to retain several records including, the new books, borrowed books with due dates, the member who borrowed books, returned books, fine on the late returned books, etc. In short, the library management system stores and updates the complete library database.

LMS also supports maintaining the physical library. The user can keep track of the position of the book in the library and can search for whether or not the specific book is currently available in the library. Therefore, LMS helps organize and retrieve library data in an efficient manner.

# 2. Expectations from the interviewee
There are multiple components of the LMS, each with its own specific requirements and constraints. Let’s look at some of the main expectations that the interviewer will want to hear you discuss in more detail during the interview.

## 2.1. Efficient searching
Searching for books is one of the most crucial functions of LMS. The user must be able to search for any book. Different users may want to search for a book through different methods. Therefore, the interviewer can ask questions like these:
* Would the user be able to search for a book using attributes other than the book name?
* How will the user be able to search for a book by its author name, publication date, etc.?
* How will the user search a specific category of books like magazines, journals, newspapers, etc.?

## 2.2. Versatility
Before designing the system, it is mandatory to specify the actors of the system. Hence, the interviewer can ask about the actors of the system as follows:
* Can the software only be used by a librarian or by all library members?

## 2.3. Book reservation
Another significant feature of LMS is the reservation of the book.
* What is the mechanism of book reservation?
* Can a member reserve a book again if it is already reserved?
* How does the status of the book change when a member returns a book?

## 2.4. Book renewal
Similar to the book reservation, the interviewer can ask about the book renewal functionality with a question like this:
* What is the mechanism of book renewal if a member wants to hold a book for a longer period of time?

## 2.5. Fine management
There is another question that the interviewer may be interested to ask:
* How is the calculation and deduction of fines handled if the book is returned late?

# 3. Requirements for the Library Management System
For LMS (Library Management System), the requirements have been defined below:

## Stage One 
* R1: The system should be able to store the information about books and members of the library. Moreover, the complete log of the book borrowing process should also be stored.
* R2: Every book is supposed to have a unique identification number and other details including a rack number to help locate the book physically.
* R3: Every book should have an associated ISBN, title, author name, subject, and publication date.

## Stage Two 
* R4: There can be multiple copies of the book. Each copy will be recognized as a book item.
* R5: There can be two types of users, i.e., the librarian and the members.
* R6: Every user must have a library card with a unique card number.

## Stage Three 
* R7: One member can issue a maximum of 10 books at a time.
* R8: The member can issue a book for a maximum of 15 days.
* R9: Each book item can only be reserved by a single member.
* R10: The system should be able to keep a record of who issued or reserved a particular book and on which date.

## Stage Four 
* R11: The system should allow the user to renew the reserved book.
* R12: The system should send a notification if the book is not returned within the due date.
* R13: If the book is currently not available, then the member should be able to reserve it for whenever it is available.
* R14: The system should allow the user to search a book by its title, author name, subject, or publication date.

# Base requirements

* Programming language: C++
* Visual Studio 2022 (latest release)
* Git for Windows (latest release)
* Skill for working with Git from command line (CLI) & Git extension in Visual Studio
* Following the best practices for C++ / Git / GitHub is a mandatory requirement

Additional requirements will be added later.
