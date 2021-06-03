# Jira Search for Alfred
This [Alfred](https://www.alfredapp.com/) workflow allows you to search for Jira issues, boards, filters and projects from Alfred's search bar using search suggestions.

[Alfred](https://www.alfredapp.com/) (alfredapp) is a productivity tool for macOS that provides a more sophisticated and extandable alternative to macOS' integrated spotlight search.

<img src="https://raw.githubusercontent.com/svenwiegand/alfred-jira-search/master/res/screenshot.png" alt="Screenshot" width="480"/>

**Attention:** This is my first Alfread workflow and my first and only Python code – so please be forgiving…

## Install & Setup
**Note:** I haven't implemented OAuth authentication yet, so you will need an API token to use this workflow. Follow these steps to create an API token:

1. Open Jira
2. Click on your avatar in the upper right corner and choose "Account settings"
3. Choose "Security" in the left navigation panel
4. Click "Create and manage API tokens"
5. Create a new API token, give it a useful label like "Jira search" and note down the token shown to you

[Download the workflow file](http://www.packal.org/workflow/jira-search) an double click it, to import the workflow into Alfread.

Set the three required variables (see below):

- `domain`: This is your atlassian domain, where your Jira cloud instance is reachable (e.g. `mycompany.atlassian.net`).
- `username`: This is your user's username in Jira.
- `password`: This is the API token you've created above.

Now your done.

## Using jira search
Bring up the Alfread search bar and type `jira` to activate this plugin. You can then choose between these search modes:

- `board`: Search for boards by name
- `filter`: Search for saved Jira filters by name
- `issue`: Search for issues by key or text content filter by additional properties (see below)
- `jql`: Search for issues using JQL
- `project`: Search for projects by name

### `issue` Search
If you type in an issue key (for example `PRJ-1234`) the workflow will suggest the matching issue, so that you can jump directly to it.

If you type in anything else the workflow will search for issues containing the text in one of their text fields. 
In this mode you can narrow down the result list using the following filter syntax:

- `@prj`: Will only list matching issues of the Jira project with the name or project key `prj`
- `#bug`: Will only list matching issues of the issue type `bug`

In both cases you can use question marks to specify names with spaces like `#"my complex issue type"`.

You can combine all of this. For example

```
receiving mail @mail #"external bug"
```

Will search for all issues of type `external bug` containing the words `receiving` and `mail` in the Jira project `mail`.