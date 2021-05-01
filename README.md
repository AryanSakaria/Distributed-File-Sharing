# Distributed-File-Sharing

A client-server pipeline implemented with pyro5, tinyDb and serpent for multi-user file sharing

## Description
- The project has two components, the server side and client side. All files uploaded are stored in the directory where the server resides. A client can be run from any location, and files relative to the client directory can be specified to be uploaded to the directory. Files downloaded from the server reside on the clients local directory

- The project uses the tinyDB library to store user data

## Features
- There are several features implemented. See ![here](/problem_statement.pdf) for full description of commands.
	- `Create account` : to create an account if it doesn't already exist

	- `login` : to login an existing account
	- `list_files` : to list files residing on the server that the user currently logged in has uploaded.

	- `list_users` : to list all registered users on the server.

	- `list_user_files user` : to list files that other users have uploaded.

	- `download file` : to download a file a user uploaded locally.

	- `upload file` : to upload a file to the server
	- `download user file` : to download a file another user has uploaded.

	- `logout` : logout and close client instance.


- Automatic syncing

## How to run
- Needed python libraries :
	- sys
	- Pyro5
	- serpent
	- os
	- tinydb
	

- 
## Scope of improvement
- Delete functionality : Deleting files
