# Spacer
## Command line tool to fix CSS indentation (2 spaces for tabs)

![running spacer on sample .scss file](spacer_animation.gif)

Sometimes I'd find myself copy-pasting large amounts of CSS from one file to another. I mainly use Vim, and when I'd paste into a Vim window, the indentation would get messed up from my `.vimrc`:

```
set tabstop=4
set softtabstop=0
set expandtab
set shiftwidth=2
set smarttab
```

So I could find-and-replace with `%s/  //g` but after that I'd still be manually fixing the spaces. So I took the time to make this bit of code which seems to work OK for fixing that one issue for me.

## Installing
```
git clone https://github.com/louisritchie/spacer
cd spacer
cp spacer.py /usr/bin/spacer
spacer YOUR-CSS-FILE

```
