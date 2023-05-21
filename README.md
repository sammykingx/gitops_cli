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

- `fetch` :  displays a list of user repository

__options__:

- `delete`: deletes a repository from users github account

__This command (`delete`) is only able to delete repository owned by a user based on the permissions assinged to the token__

__options__:

- `fork`: Forks a repository

## Test
Tested on the following Ubuntu distro
	- `Ubuntu 22.04`
	- `Ubuntu 20.04`
	- `Ubuntu 18.04`
	- `Ubuntu 16.04`

Tested with python versions `3.10.*` `to 3.6.*`
