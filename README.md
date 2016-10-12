When you paste into VIM it preserves all newlines and spaces in your clipboard, ie it doesn't format it at all
So you often end up with crazy newline and indent staircases when copying into Vim.
I will fix it with the Vim command:
`:%s/  //g`
but then I'm left having to manually fix the spacing. F*ck that! That can be done in very few python lines and used on the command line.
