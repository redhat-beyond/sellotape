# sellotape

Sellotape is a modern audio podcast platform.
It introduces an accessible way to listen to podcast and audio streams.

As a podcaster/streamer, you can create your private radio. By accessing your user endpoint, anyone who wants to listen can join your podcast, live djset, or whatever it is you want it to be heard.

As a listener, you can follow your favorite streamers and keep up to date with their streams.

## Ideology 
The platform strives to be a simple social network as users can follow each other and go live whenever they wish to do so. Our philosophy is that there should be no alienation between a streamer and a listener, and we engage and strive to push the interaction between them as possible.

## High-level design
* Unregister users will encounter a landing page that explains the platform and let them register easily.
However, resigtration is required in order to stream and/or to stay up to date with streamers that you follow, as would be expected from a basic social network.
It is not necessary for merely listening to a live poadcat, as we encourage more listeners and an easy access to different streams of registered users.

* If user x _is_ registered (and logged in), then the following will be presented on the main page:
    * (Infinite) feed of future scheduled streams of users that user x follows.
    * When there are no more available shceduled streams to display then show previous streams of users that user x follows.
    * Trending streams of users that user x doesn't follow
    * Explore streams by subject/tag searching
    * Go live to invoke a live audio stream at user x's endpoint.

* Accessing a specific user page will show:
    * User info and a _follow_ button
    * _Listen live now_ button if indeed a live stream is occurring at the moment.
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
        * `user_id`, `follower_id`
        * Primary key: (user_id, follower_id)
        * Each of the above columns has a foreign key referencing `user_id` in `users` table.
    * `streams` table:
        * `stream_id`, `creator_id`, `date`, (link to archived stream?)
        * Primary key: `stream_id`
        * `creator_id` has a foreign key referencing `user_id` in `users` table.
* Live audio streaming:
    A 3rd party library would come in handy, and we are researching the matter.
    However, a tool to note here is [Django Channels](https://channels.readthedocs.io/en/latest/introduction.html) which requires more 'hands on' implementation but could possibly serve our puporse in a more pure and clean manner.

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
