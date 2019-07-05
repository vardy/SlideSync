# Image Folder Sync Service

Simple thing for small project with overkill README :)

## Building server

```
$ docker build -t slide_server .
$ docker run -p 3000:3000 slide_server
```

After building you may call the `run` command on all subsequent runs. Port 3000 can be replaced by any available port on the *left* side of the `-p` option's argument, eg. `-p 8080:3000`.

*Warning:* This will publish (open) the server's port 3000 publicly in order to receive incoming requests for the server's images.

## Client

### Setup credentials

The IP address of the server running the SlideSync server service is hard-coded. By default it is `localhost:3000`. Update on line 8 of `get_images.py`. The port is set when running the server with the `$ docker run -p xx:xx` command.

### Building

**With Docker:**

```
$ docker build -t slide_client .
$ docker run slide_client # Call this command on all subsequent runs
```

**Without Docker:**

```
$ python3.7 get_images.py
```

### Result

All images within the server's `/images` directory will be transfered to the client's `/images` directory to mirror it 1:1. Images will be removed from the client's directory once it has been removed on the server (upon subsequently running the client).

## License

This project is licensed under the GNU GPLv3.    
This license is copy-left and conducive to free, open-source software.

Project license: https://github.com/vardy/SlideSync/blob/master/LICENSE    
License details: https://choosealicense.com/licenses/gpl-3.0/#