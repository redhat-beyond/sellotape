# Architecture

## High-level design
* Unregister users will encounter a landing page that explains the platform and let them sign-in easily.
Resigtration is required in order to connect your streams information and/or to stay up to date with streamers that you follow, as would be expected from a basic social network.
It is not necessary though for viewing schedueld streams of other users, as we encourage more listeners and an easy access to different streams of registered users. Also, it is not necessary to view the Trending Live page of currently live streams.

* If user x _is_ registered (and logged in), then the following will be presented on the main page:
    * (Infinite) feed of future scheduled streams of users that user x follows.
    * When there are no more available shceduled streams to display then show previous streams of users that user x follows.
    * Explore streams by subject/tag searching

* Accessing a specific user page will show:
    * User info and a _follow_ button
    * _Listen live now link_ button if indeed a live stream is occurring at the moment.
    * Display archeieve of previous streams

## Technological stack 

#### Backend:

* **MVC design pattern with Django framework**.
* Database: _SQLite_.
    Note: the following db structure may change upon needs.
    * `Profile` table:
        * `user_id`, `first_name`, `last_name`, `username`, `email`, `password`, `city`, `country`, `avatar`, `youtube_link`, `twitch_link`
        * Primary key: `user_id`
    * `UserFollowers` table:
        * `user_follower_id`, `user_id`, `follower_id`
        * Primary key: `user_follower_id`
        * `user_id` and `follower_id` are foreign keys referencing `user_id` in `users` table.
    * `Streams` table:
        * `id`, `author`, `title`, `description`, `link`, `airs_on`, `ends_on`, `added_on`, `genre`
        * Primary key: `id`
        * `author` has a foreign key referencing `user_id` in `users` table.

#### Frontend:
* DTL (Django template langauge)
* HTML
* [Boostrap 4](https://getbootstrap.com/)

#### Environment:
* Vagrant with `fedora/32-cloud-base` virtual box.
* Python packages managed by [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/).

#### CI/CD:
* GitHub Actions workflow to run a linter test (Flake8), unit and functional tests using Django built-in testing framework.
