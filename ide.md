# VSCode

* vscode-hacker-typer - [github](https://github.com/jevakallio/vscode-hacker-typer) - vscode extension
* vscode-data-wrangler - [github](https://github.com/microsoft/vscode-data-wrangler) - vscode extension
* vscodium - [github](https://github.com/VSCodium/vscodium)
* zasper - [github](https://github.com/zasper-io/zasper) - IDE for Jupyter notebooks

Tutos

* FCC VS Code Tutorial – Become More Productive (6h) - [youtube](https://www.youtube.com/watch?v=heXQnM99oAI)
* Exploring the Dev Container Ecosystem - [youtube](https://www.youtube.com/watch?v=AVVGGe_zQkc)
* How to develop like a Senior Software Engineer - [youtube](https://www.youtube.com/watch?v=FxXyoRyzxoU)
* Working with Multiple Dev Containers in VS Code - [youtube](https://www.youtube.com/watch?v=bVmczgfeR5Y)
* [user-interface](https://code.visualstudio.com/docs/getstarted/userinterface) - [youtube](https://www.youtube.com/watch?v=nORT3-kONgA)

## launching from the command line

open command palette, then search: `shell command` 

## regex

Find and Replace
```
(\w+)
"$1",
```

## share config

Sharing configurations in Visual Studio Code (VSCode) can be done through the use of a `.vscode` settings folder that can be added to your project. Here's how to do it:

1. Under your workspace folder, create a new folder named `.vscode` if it doesn't exist.
2. Inside the `.vscode` folder, create a new file named `settings.json`.
3. Save this file and commit it to your project. When others clone and open this project in VSCode, these settings will be applied.
4. Define your settings. For example:

```json
{
  "editor.tabSize": 2,
  "editor.wordWrap": "on",
  "files.exclude": {
    "**/.git": true,
    "**/.svn": true,
    "**/.hg": true,
    "**/CVS": true,
    "**/.DS_Store": true
  }
}
```

Remember, this only shares settings that are specific to the VSCode editor. You can't share extensions or globally defined user settings this way.

## share extension

To share extensions, you can recommend them in the workspace by creating an `extensions.json` file in the `.vscode` folder. You can list extensions by their identifier in this file. However, this won't automatically install them, it will only prompt other users to install them when they open the workspace. Here's an example:

```json
{
  "recommendations": [
    "ms-vscode.vscode-typescript-tslint-plugin",
    "esbenp.prettier-vscode"
  ]
}
```

As for sharing user settings, there is no built-in way to do this in VSCode. User settings are global to all instances of VSCode and are not meant to be shared between projects. However, you can share them manually by copying the `settings.json` file from your User folder and sending it to others. They can then replace their own `settings.json` file with yours. You can access your User `settings.json` by going to File > Preferences > Settings and clicking on the `{}` icon in the top right.

## dev container

To use VSCode Dev Container to work on an Odoo application with a PostgreSQL database, follow these steps:

1. Install the Docker extension in VSCode.
2. In your project folder, create a `.devcontainer` directory.
3. Inside the `.devcontainer` directory, create a `Dockerfile` with the necessary setup. You can refer to existing Docker images for Odoo applications.
4. Still in the `.devcontainer` directory, create a `devcontainer.json` file. This file configures the settings for your container. An example configuration is:

```json
{
  "name": "Odoo",
  "dockerFile": "Dockerfile",
  "settings": {
    "terminal.integrated.shell.linux": "/bin/bash"
  },
  "appPort": 8069,
  "extensions": ["your-required-extensions"]
}
```

1. Open your project in VSCode, then press F1 and select the "Remote-Containers: Reopen Folder in Container" command.

This will build your Docker container based on the `Dockerfile` you created and start a VSCode server inside the container. Your project will be mounted into the container and your extensions and settings will be loaded. Now you can work on your Odoo application inside a containerized environment.

As for the PostgreSQL database, you can either install it inside the Docker container along with Odoo, or you can use a separate Docker container for PostgreSQL and connect to it from the Odoo container. In either case, you will need to adjust your `Dockerfile` and `devcontainer.json` to include the necessary instructions for installing and configuring PostgreSQL.

---

Yes, you can use a Docker Compose file with VSCode Dev Container. Instead of a `Dockerfile`, you would create a `docker-compose.yml` file in the `.devcontainer` directory. In your `devcontainer.json`, you would specify the path to the Docker Compose file and the service to use. Here's an example `devcontainer.json`:

```json
{
  "name": "Your Project",
  "dockerComposeFile": "docker-compose.yml",
  "service": "your-service-name",
  "settings": {
    "terminal.integrated.shell.linux": "/bin/bash"
  },
  "extensions": ["your-required-extensions"]
}
```

This setup allows for more complex container configurations, such as using different containers for your application and database.

# VIM

https://en.wikipedia.org/wiki/Vim_(text_editor)

```
" .vimrc example
"" double quote should be used to comment working code

set number
set relativenumber
set tabstop=4
set shiftwidth=4
set autoindent
set mouse=a
colorscheme slate
```

.  repeat the last command
:reg  register


# Navigate - normal mode

## go to the first line of the file
:1
ctrl + home
gg

## go to the last line of the file
:%
ctrl + end
G

3G: jump to the third line
:123 - jump to the 123th line

= auto indent the line
gg=G auto indent the entire file

zz center the screen

# jump to the pair parenthese
%

# jump to next symbol
t(: jump before the next (
f(: jump to the next (
* jump to the next same word

# jump to the previous symbol
T(
F(
# jump to the previous symbol

ma: mark the position with the caracter 'a'
'a: jump to the marker 'a'

# search
/pattern find the next pattern
n next item
N previous item

?pattern find the previous pattern (reverse of /pattern)


# jump 

# (w)ord - jump to the next word
!= b

# 

ci( copy until the next character '('

:%s/find_pattern/replace_pattern/g  global find and replace

# Edit mode

every key can be combined with a number

## undo
u

## redo
CTRL + R

## (d)elete
dd: delete the line
5d: delete the 5 next lines
dw: delete word
d0: delete until the begining to the line
d%: delete the inner paranthese
dt(: delete everything until the next (

## (y)ank = copy

## (p)aste
p: after
P: before

## (r)eplace - instead of delete + insert

# (v)isual mode

# CTRL + v - visual block mode - column mode
