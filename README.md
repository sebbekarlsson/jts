# Jinja Template Server
> Serve jinja templates, very useful for mocking up prototypes.

## Install
> To install, you will need python. Then simply run:

    python setup.py install

## Usage
> Once installed, you can simply run `jts` in a directory you would like to serve.  
> Like this:
    
    cd /home/me/workspace/myproject
    jts .

> Now the server is available at `http://localhost:5000` :D

### Flask functions
> You can expect to be able to do normal flask stuff in your templates, such as
`url_for` and things like that :)
