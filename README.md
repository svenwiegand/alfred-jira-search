# Jira Search for Alfred
This [Alfred](https://www.alfredapp.com/) workflow allows you to search for Jira issues, boards, filters and projects from Alfred's search bar using search suggestions.

[Alfred](https://www.alfredapp.com/) (alfredapp) is a productivity tool for macOS that provides a more sophisticated and extandable alternative to macOS' integrated spotlight search.

![Screenshot](https://github.com/svenwiegand/alfred-jira-search/blob/master/screenshot.png?raw=true)

## Install & Setup
**Note:** I haven't implemented OAuth authentication yet, so you will need an API token to use this workflow. Follow these steps to create an API token:

1. Open Jira
2. Click on your avatar in the upper right corner and choose "Account settings"
3. Choose "Security" in the left navigation panel
4. Click "Create and manage API tokens"
5. Create a new API token, give it a useful label like "Jira search" and note down the token shown to you

Now download the `.alfredworkflow` file an double click it, to import the workflow into Alfread.

Set the three required variables (see below):

- `domain`: This is your atlassian domain, where your Jira cloud instance is reachable (e.g. `mycompany.atlassian.net`).
- `username`: This is your user's username in Jira.
- `password`: This is the API token you've created above.

Now your done.

## Using jira search
Bring up the Alfread search bar and type `jira` to activate this plugin. You then have to type one of these keywords or choose them from the suggestion list to specify what you want to search for:

- `issue`: Searches `key` and `text` of the issues for your query
- `board`: Searches for boards matching your query
- `filter`: Searches for filters matching your query
- `project`: Searches for projects matching your query