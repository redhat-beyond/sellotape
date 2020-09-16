# sellotape

Sellotape is a modern audio podcast platform.
It introduces an accessible way to listen to podcast and streams.

It serves as a simple social network, helping streamers and listeners to easily access and expose their live content as it centralizes streams from many popular streaming sources.

As a podcaster/streamer, you can expose yourself better - by providing centralized information on previous, present and future streams.

As a listener, you can follow your favorite streamers and keep up to date with their streams.

## Ideology 
The platform strives to be a simple social network as users can follow and engage with each other.
Our philosophy is that there should be no alienation between a streamer and a listener, and we engage and strive to push the interaction between them as possible.

## High-level design
* Unregister users will encounter a landing page that explains the platform and let them sign-in easily.
Resigtration is required in order to connect your streams information and/or to stay up to date with streamers that you follow, as would be expected from a basic social network.
It is not necessary though for viewing schedueld streams of other users, as we encourage more listeners and an easy access to different streams of registered users.

* If user x _is_ registered (and logged in), then the following will be presented on the main page:
    * (Infinite) feed of future scheduled streams of users that user x follows.
    * When there are no more available shceduled streams to display then show previous streams of users that user x follows.
    * Trending streams of users that user x doesn't follow
    * Explore streams by subject/tag searching

* Accessing a specific user page will show:
    * User info and a _follow_ button
    * _Listen live now link_ button if indeed a live stream is occurring at the moment.
    * Display archeieve of previous streams

## Technological stack 

#### Backend:

* **MVC design pattern with Django framework**.
* Database: _PostgreSQL_.
    Note: the following db structure may change upon needs.
    * `users` table:
        * `user_id`, `first_name`, `last_name`, `username`, `email`, `password`, `city`, `country`, `avatar`
        * Primary key: `user_id`
    * `user_followers` table:
        * `user_follower_id`, `user_id`, `follower_id`
        * Primary key: `user_follower_id`
        * `user_id` and `follower_id` are foreign keys referencing `user_id` in `users` table.
    * `streams` table:
        * `id`, `author`, `link`, `airs_on`, `ends_on`, `added_on`
        * Primary key: `id`
        * `author` has a foreign key referencing `user_id` in `users` table.

#### Frontend:
* DTL (Django template langauge)
* HTML/Sass

#### Environment:
* Vagrant (specific virtual box not yet determined) for development.
* Python packages managed by [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/).

#### CI/CD:
* GitHub Actions workflow to run lint, unit and functional tests with pylint and PyTest.
* Static type checker using [Mypy](http://mypy-lang.org/).

#### Team Members
Guy Itzhaki, Tarel Madar, Gal Lapid, Alon Weissfeld, Omri Rosner

## Setting up a development environment using Vagrant
1. Install VirtualBox and Vagrant.
2. Clone this repository.
3. Open a shell prompt, and switch to the location of the repository.
4. Run 'vagrant up'. Once it finished, you're all set!

## Setting up superuser
A superuser is automatically created in the provisioning scripts, you can change the default username and password in there BEFORE running `vagrant up`.
The defaults are currently 'admin', '123456'.

# Shortcuts/Aliases
For you convenience, we've set up a few aliases to ease up Start/Stop/Restart actions of the project.
Usage: `start_sellotape`, `stop_sellotape`, `restart_sellotape` to start/stop/restart sellotape.
Upon project creation, `start_sellotape` is run automatically.
