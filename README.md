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
* Backend:
    * **MVC design pattern with Django framework**.
    * Database: TBD.
        * users table
        * user_followers table
        * streams table
    * Live audio streaming: [Django Channels](https://channels.readthedocs.io/en/latest/introduction.html) is under consideration - the subject is under research.

* Frontend:
    * React
    * HTML/Sass

* Environment:
    * Vagrant (specific virtual box not yet determined)
    * Python packages conifuged via `requirements.txt`

* CI/CD:
    * GitHub Actions workflow to run lint, unit and functional tests with pylint and PyTest.

#### Team Members
Guy Itzhaki, Tarel Madar, Gal Lapid, Alon Weissfeld, Omri Rosner
