## LeetCode Saver

A tool that helps you save your LeetCode solutions to your local storage.

### Challenges

For each LeetCode question page, there are three major sections: Description, Code, and Testcase.
The ideal approach is to take the HTML of the Code section and save the code snippet either as HTML or in some other processed format.
However, inside of that scrollable Code section on the LeetCode webpage,
the code is dynamically loaded and the HTML source code is only available for what is visible in the window.

### Approach 1

Given a LeetCode question list, we manually copy and paste code snippet after each unique question title.

### Approach 2

We use Selenium to visit each question's page and automatically select the solution and generate a list of problem-solution pairs.