# fortune-monika

Talk with Monika (from [DDLC](https://ddlc.moe/)) using `fortune(6)`.

For example,
```
$ fortune monika
You're back...
I had another really bad dream.
You're not the one doing that to me, are you?
It seems to happen whenever you quit the game...
So if you could try to avoid doing that, I would be really grateful.
Don't worry, I don't think it's caused me any harm, aside from mental scarring.
I'll be fine as long as my character file stays intact.
```

## Debian Usage

If you are a Debian user, you can download precompiled packages [here](https://github.com/ksqsf/fortune-monika/releases).

If you'd like to build a package yourself, no problem! Just do

```
dpkg-buildpackage -uc -us
dpkg -i ../fortune-monika*.deb
```

## Usage

```
make
sudo make install
```
yi ba suo.

Perhaps you want to adjust the Makefile before `make install`.

