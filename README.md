# gitops_cli

A cli tool that enables you interact with github without having to use the github GUI.

## Pre-Installation Process
Before you begin the installation process, first create your token and grant the below permissions to it.

- [click to create token](https://github.com/settings/tokens)

- grant the following permissions during the creation
	- tick the `repo` box
	- tick the `delete_repo` box

_Please make sure this permissions are ticked during token creation  to enable gitops cli work properly_

## Installation process

- clone the repository to your terminal
```bash
$ git clone https://github.com/sammykingx/gitops_cli
```
- change your directory to the gitops_cli
```bash
$ cd gitops_cli
```
- run the installation script
```bash
gitops_cli$ ./install.sh
```
- When the installation prompts you to input token, copy-pate your token
```bash
gitops_cli$ Enter your github token (press ENTER to ignore):
```
please note without your token been giving the necessary permissions, gitops won't work as expected.

## Usage
```bash
gitops < SUB_COMMAND | ARGS >
```
### SUB_COMMAND
- `create` : creates the repository for the gituser

__options__:
- `-d: description` => The description for the repository `optional`
	
- `-h: help` => Displays the help message with list of available options for the create command

- `-n: name` => name of the repository to create `required`
- `-p: private` => Visibility status of the repository (default = False)

Only use the `-p` option when you wish to create a private repository else ignore

Code example
```bash
$ gitops create -h
# shows the available options

$ gitops create -n name_of_repo -d "description of the repo"
# creates the repository <name_of_repo> with description <description_of_repo>

```
HTTP STATUS CODE WHEN IT FAILS
	| Status code	| Description |
	| :---:		| :---	      |
	| 201        	| created the repository |
	| 304		| not modified |
	| 400		| Bad request |
	| 401		| Requires authentication |
	| 403		| Forbidden |
	| 404		| Resource not found |
	| 422		| validation failed |

example of successfull repo creation with gitops
```bash
$ gitops create -n test_repo1 -d "testing repo creation with gitops"
calling appropriate handler
repo succesfully created
=> repo url: https://githubs.com/sammykingx/test_repo1
```

- `fetch` :  displays a list of user repository

__options__:
- as of now no options is add to the fetch command
Just run the command to get a list of all repos.

cexample command usage
```bash
$gitops fetch
```

NOTE: This command list all repo affiliated to the user including repository in which the user is a collaborator

- `delete`: deletes a repository from users github account

__This command (`delete`) is only able to delete repository owned by a user based on the permissions assinged to the token__

__options__:
- `-u user`: The name of the github user `required`
- `-r repo`: The name of the repository  `required`

example command usage
```bash
$gitops delete -u sammykingx -r test_repo1
calling appropriate handler
Repo successfully deleted for user sammykingx
```

STATUS CODES RETURNED ON ERROR
	| Status code	| Description |
	| :---:		| :---	      |
	| 307		| Temporary redirect |
	| 404		| Resource not found |

- `fork`: Forks a repository
__options__:

- `-o owner`: The account owner of the repository `required`
- `-r repo`: The name of the repo to fork `required`

### Args
- `-h help`: shows the help message
- `-v version`: shows the version number

## Tests
Tested on the following Ubuntu distro
- `Ubuntu 22.04`
- `Ubuntu 20.04`
- `Ubuntu 18.04`
- `Ubuntu 16.04`

Tested with python versions:
- `3.10.*`
- `to 3.6.*`
