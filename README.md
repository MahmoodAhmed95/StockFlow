# StockFlow-Alpha
Inventory Management for Micro Home-Based Businesses (HBB)
-----------------------------------------------------------------

## Project Overview
StockFlow is a one-week Proof-of-Concept project that aims to simplify inventory management and streamline the point of sale (POS) process for micro home-based businesses (HBBs). This system is designed to help HBB owners efficiently control their inventory and manage sales operations. In this initial phase of development, our primary focus will be on creating the Inventory Module and POS Module.

## Planning Stage

## Project Management Approach

At StockFlow, we believe that effective project management is key to delivering a successful software solution. We follow an Agile approach, which promotes flexibility, collaboration, and customer-centric development. Here's how we manage our project:

### Planning and Task Breakdown
  ![Tasks Breakdown](Documentation/Images/TasksBreakdown.png)
We break our project into small, manageable tasks, which are akin to mini-goals. These tasks are designed with the user in mind, ensuring that we address their needs and expectations. For example, "Users want to log in."

### Automated Kanban Board
  ![Kanban Board](Documentation/Images/Kanban.png)
To keep track of our work, we use an automated Kanban board within GitHub. This digital to-do list comprises columns representing different stages of tasks, "Icebox," "Current Sprint," "In progress," "Reviewing," "Done," and "Postponed / Canceled." This visual representation helps us understand what needs to be done, what's currently in progress, and what has been completed.

### GitHub Issue System
  ![GitHub Issue](Documentation/Images/GitHubIssues.png)
We utilize GitHub's issue system to describe and manage each task comprehensively. Think of it as a centralized hub for all task-related information. Here, we discuss what needs to be done, how to test it, and who is responsible for its completion.

### Assigning Tasks
  ![Tasks Assigning](Documentation/Images/TaskAssigning.png)
Documentation\Images\TaskAssigning.png
Every task is assigned to a team member, ensuring clear accountability. This practice ensures that everyone knows who is responsible for what, ultimately leading to a more organized and efficient workflow.

### Benefits of Our Approach

Our project management approach offers several advantages:

- **Step-by-Step Progress:** Breaking the project into smaller tasks allows us to make steady progress, providing a sense of accomplishment with each completed task.

- **Adaptability:** Agile methodologies make it easier for us to adapt to changes in requirements or priorities as we work on the project.

- **Organization:** Our use of Kanban boards and GitHub issues helps us stay organized, ensuring that no task slips through the cracks.

- **Efficient Teamwork:** Assigning tasks and using collaborative tools promotes teamwork and ensures that work is distributed evenly among team members.

- **Quality Results:** Our approach prioritizes delivering high-quality software that meets user needs and expectations.

We believe that by following these project management principles, we can efficiently develop StockFlow and provide an exceptional solution for micro home-based businesses.


 
## Planning Documents:

### User Stories
- As a user, I want to log in to the system to access inventory management and POS features.
- As a user, I want to CRUD (Create, Read, Update, Delete) the products catalog in my system so that I can maintain an organized product listing.
- As a user, I want to CRUD (Create, Read, Update, Delete) the products in my system so that I can manage product details and stock levels efficiently.
- As a user, I want to CRUD (Create, Read, Update, Delete) the vendors in my system for better supplier management.
- As a user, I want to CRUD (Create, Read, Update, Delete) the Received Notes so that I can effectively control and update inventory based on incoming shipments.
- As a user, I want to CRUD (Create, Read, Update, Delete) the customers in my system to maintain a record of clients and their information.
- As a user, I want to CRUD (Create, Read, Update, Delete) the delivery notes to track and control outgoing shipments.
- As a user, I want to use the POS to register fast and quick sales invoices with visual product representation (pictures and colors) for a user-friendly experience.

### Admin Stories (To Be Added)

### WireFrames (Coming Soon)
Sketches of each screen's user interface for the major functionality of the application.
### Entity-Relationship-Diagram (ERD)
 A diagram of the app's models (one per data entity) and the relationships between them.
### Technologies Used

- **Frontend:** React.js + Django
- **Backend:** Django Python
- **Database:** Postgres
- **Other Tools:** [List any additional tools or libraries]


## Git Guidelines and Conventions

Effective version control is not just a best practice; it's a fundamental aspect of collaborative software development. At StockFlow, we prioritize a robust version control process as it plays a vital role in the success of our project.

By combining the best practices of DevOps with our Git guidelines and conventions, we create a powerful and efficient development workflow that fosters collaboration, reliability, and agility. These practices enable us to deliver high-quality software and maintain a robust, stable, and scalable application for our users.

### Working with Branches

1. **Pull from the main repo:** Before starting any work, ensure your local repository is up-to-date with the origin remote:
```
git pull origin main
```

2. **Create a New Branch for Your Design/Feature/Bug:** Create a new branch for the specific task you're working on. Name it descriptively and include the issue number in the branch name using #:
- For design: `git checkout -b "design/design-name#123`
- For feature: `git checkout -b "feature/feature-name#123`
- For bug: `git checkout -b "bug/bug-name#123`

3. **Work on Your Task:** Make changes, write code, and complete your feature on the new branch.

4. **Commit Your Changes AND Commit Often:** Add and commit your changes to the local branch:
```
git add .
git commit -m "..."
```

5. **Pull the main AND resolve conflicts:** Before pushing your changes, make sure to pull from the origin to get the latest updates and resolve any conflicts with the main branch.

If you encounter conflicts, resolve them locally before creating a Pull Request. Ensure that your changes do not compromise any functionality as the main version is working correctly:
```
git pull origin main
```

### Pushing to Remote and Creating a Pull Request

1. **Push to Remote and Create a Pull Request:** Push your feature branch to the remote repository and create a pull request on the GA GitHub webpage:
If it is the first push from the branch : 
```
git push --set-upstream origin "feature/feature-name#123"
```
from the 2nd push you can use
```
git push "feature/feature-name#123"
```

Open the repository on the [StockFlow Pulls webpage](https://git.generalassemb.ly/StockFlow/StockFlow-Alpha/pulls). Click on the "Compare & pull request" button for the feature branch you just pushed.

2. **Review the changes in the pull request:** Mention the issue number in the pull request description to link it to the issue. Use `Closes #123` to indicate that the pull request will resolve the issue.

3. **Click on "Create pull request."**

### Switching Branches

On Your PC:

- After your pull request is approved and merged or if you need to switch to another branch, follow these steps:

1. **Get Latest Changes and Switch to Another Branch:** Merge the latest changes from the origin remote and switch to the main branch or another branch as needed:
```
git pull origin main
git checkout main # To switch to the main branch
git checkout "feature/another-feature-name#123" # To switch to another feature branch
```