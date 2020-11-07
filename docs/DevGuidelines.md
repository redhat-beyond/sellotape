# Developement Guidelines
Thank you for your interest in making Sellotape better. 

## Spinning Up
We use [Vagrant](https://www.vagrantup.com/) to set up our virutal environment. To properly run the project, make sure that you have VirtualBox and Vagrant installed on your machine. Then:
1. Clone this repository
2. Open a shell prompt, and switch to the location of the repository
3. Run `vagrant up` which will create the virtual machine according to the Vagrantfile. Once it's finished, you're all set!
4. Open your browser and navigate to `0.0.0.0:8000`. Voila! :smirk:

### Setting Up a Superuser
A superuser is automatically created in the provisioning scripts that are run by Vagrant during the bootstrao process. You can change the default username and password in there _before_ running `vagrant up`.
The defaults are currently `admin`, `123456`.

### Shortcuts/Aliases
For you convenience, we've set up a few aliases to ease up Start/Stop/Restart actions of the project.
After SSHing to the virtual machine (using `vagrant ssh`) you can run the following commands:
* `start_sellotape`, `stop_sellotape`, `restart_sellotape` to start/stop/restart sellotape.
Note that upon project creation, `start_sellotape` is run automatically.

### Synced Files
We don't expect you to fix bugs or develop new features on the virutal machine :stuck_out_tongue_closed_eyes: &nbsp; All the files in the repository are copied to a 2-way-synced (shared) folder on the virtual machine under the `/vagrant/` folder. Develop locally on your host machine while the server will restart itself at any file change.

## Conventions
Take a look at the [architecture document](Architecture.md) to understand the project's technological stack and design. We follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide and use [Flake8](https://flake8.pycqa.org/en/latest/) as our enforcement linter. So before submitting any Pull Requests, make sure you pass the linter by running `flake8 . --count --max-line-length=127`.

## Testing
We encourage you to develop in [TDD](https://en.wikipedia.org/wiki/Test-driven_development). Make sure that you add tests to any new feature you want to add. If you're fixing a bug, first make sure that there is a test failing for that use case (if it does not exist then add it). Then work on your fix until that test passes. The tests should reside in a `tests` folder under the plugged Django application your working on. So, if your're adding a test to the `main_app`, you would test it by executing `pipenv run python3 sellotape_dj/manage.py test main_app`.