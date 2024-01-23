# Testing-User-Authentication
A personal project to test basic user authentication using Selenium and Pytest.
### Project Purpose
This was a personal project completed in December 2023 - January 2024. My goal for this project was to gain experience working with Selenium, browser drivers, Python, and Pytest. Additionally, I wanted to gain experience with Test Automation by creating simple but useful test cases that would automate one of two browsers (Firefox or Microsoft Edge), and pass or fail based on the expected result.

This project was inspired by a LinkedIn Learning course I took on Test Automation. For reference, this course can be viewed [here](https://www.linkedin.com/learning/paths/getting-started-in-test-automation-engineering).
### Development and Experience
My development for this project was completed in my free time over a period of 2 months. I took that time to write the code for the project, as well as research the issues I encountered and research best practices for test automation project design/structure. While I had prior knowledge of selenium and test automation, this was my first opportunity to gain hands-on experience writing code that automated a browser. My work started with downloading the browser drivers and adding them to my path so that they could be called from the project. For this project, I used geckodriver and msedgedriver. After this setup was completed, I created the structure for my project by identifying each of the pages and elements I would need to define and use for this test. Finally, I wrote the code for the pages, elements, methods, and tests. After I had created code that ran in the way I had intended it to, I spent the next week revising and restructuring code. I asked myself questions like: Are there any sections of my code that are repetitive? If so, can these be restructured into methods and called as needed? What code is needed in the testing class? Are there any sections of code that can be rewritten more clearly or concisely? Is my code neat and readable? Is my code commented throughout? After I had answered these questions, and adjusted the code as needed, I published it to my GitHub.
### Functionality
This project tests a basic login page provided by the following website https://the-internet.herokuapp.com/. The login page used can be accessed by clicking the [Form Authentication](https://the-internet.herokuapp.com/login) link. My project tests if the user can:
- Login with a valid username and password.
- Login with a valid username and invalid password.
- Login with an invalid username and valid password.

By checking the text in the flash messages, I was able to create assertions for the expected conditions for each of these scenarios and pass or fail accordingly.
### Skills Gained
As a quick summary, the skills/tools I gained experience with from this project were:
- Python
- Test Automation
- Selenium
- Geckodriver and MSEdgeDriver
- Pytest

To go into a bit more depth... I learned a lot from this project, and I have plans to continue my work in a future project where I can get a bit more complex with my tests and continue learning. While the functionality of this project is simple, I believe that the skills I learned while working can be applied to my work in the future. I learned how to structure a project for automating and testing a browser using the Page Object Model. I learned how to download browser drivers and add them to my computer path so that they can be called as needed. I learned how to create a (parent) page which is inherited by other (child) pages, and the benefit of doing so. These are just a few of the things I am taking away from this experience.
