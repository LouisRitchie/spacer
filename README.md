# Spacer
## Command line utility to format your messed up CSS structure

Sometimes I'd find myself copy-pasting large amounts of CSS from one file to another. I mainly use Vim, and when I'd paste into a Vim window, the indentation would get messed up from my `.vimrc`:

```
set tabstop=4
set softtabstop=0
set expandtab
set shiftwidth=2
set smarttab
```

So I could find-and-replace with `%s/  //g` but after that I'd still be manually fixing the spaces. So I took the time to make this bit of code which seems to work OK for fixing that one issue for me.

If you place the `spacer.py` file somewhere in your `$PATH` (`echo $PATH` to see it), you can do `spacer.py MY-CSS-FILE.css` and it will put indent it use two spaces for a tab. 

Happy spacing.
