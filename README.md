# ctf-nc-framework #
A tiny framework to run python challenges in raw TCP.

### Installing ###
Just clone this repo and you're already down for business!
Wanna test it out? Just run `./ctfnc prod`.

### How to ###

Code your own challenge in `src/main.py`.
There, you'll need to define a `main` function that has two
parameters: `stdin` and `stdout`.

- You should use the `stdin.readline().strip()` to get your input.
- You should use `stdout.write()` to output something. Remember to send `\n`s to the function!
- In case you want to output without sending a `\n`, use `stdout.flush()`.
- Do NOT use `input` or `print` for reasons other than debugging.

After that, you can test it using `./ctfnc dev`. You should be able to use it through your terminal.

With that working, try using `./ctfnc prod`. it will start listening on a TCP socket (by default, 9001),
and be able to serve your challenge up to 10 users at the same time (also configurable -- see below).

### Configuration ###
All configuration lies in `config/config.py`, although every single one of them is overwritable by env vars
with the same name. for example, the config `CTFNC_PORT` is overwritable by the env var `CTFNC_PORT`.
