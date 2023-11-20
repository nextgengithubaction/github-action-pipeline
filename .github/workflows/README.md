## Contents of .github/workflows folder

### `Dotnet_Build_Sonar_Scan.yml` is a GitHub workflow that does the following:
- Builds the Dotnet App and Scans it using SonarQube Scan uploading the results to SonarQube Quality Gate

### `Sonar_Python_Jira.yml` is a GitHub workflow that does the following:
- Retrieves SonarQube Quality Gate status and creates JIRA Issues if any vulnerabilities are detected

### `blazemeter.yml` is a GitHub workflow that does the following:
- perform Blazemeter testing on the codebase and publishes the results in a specified UI

### `cd-integrated.yml` is a GitHub workflow that does the following:
- calls all the CD workflows and runs them as a single integrated workflow

### `ci_githubaction_main.yml` is a GitHub workflow that does the following:
- calls all the CI workflows and runs them as a single integrated workflow

### `codeql.yml` is a GitHub workflow that does the following:
- performs CodeQL analysis on the codebase and uploads the results to GitHub under the Security tab

### `create-jira-issue.yml` is a GitHub workflow that does the following:
- logs in to Jira instance
- creates Jira issues based on inputs passed to it for the project key, issue type, title and description

### `dependabot_scanning.yml` is a GitHub workflow that does the following:
- performs Dependency review on the pull requests and code base
- creates pull requests for outdated versions 
- uploads the results to GitHub under Security Dependabot alerts tab
 
### `get-codeql-vulnerability-details.yml` is a GitHub workflow that does the following:
- calls and executes the `codeql-create-jira-issue.py` script and passes the json output to the next workflow

### `checkmarx.yml` is a GitHub workflow that does the following:
- performs Checkmarx analysis on the codebase and uploads the results to GitHub under the Security tab

### `jfrog.yml` is a GitHub workflow that does the following:
- builds the codebase and publishes the artifacts to JFrog Artifactory
- also performs Aqua Trivy scanning on the artifacts before uploading them to JFrog Artifactory
